from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class TimeStamped(models.Model):
    created_at = models.DateTimeField(editable=False)
    updated_at = models.DateTimeField(editable=False)

    def save(self, *args, **kwargs):
        if not self.created_at:
            self.created_at = timezone.now()

        self.updated_at = timezone.now()
        return super(TimeStamped, self).save(*args, **kwargs)

    class Meta:
        abstract = True

class Image(TimeStamped):
    title = models.CharField(max_length=128, unique=True, blank=False)
    url = models.CharField(max_length=512)
    description = models.TextField(blank=True)
    pub_date = models.DateTimeField('Published at')
    upvotes = models.IntegerField(default=0)        #upvotes i downvotes dodani direktno u image
    downvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.title

    def comments_count(self):
        return self.image.comment_set.count()    # vraca broj komentara pomocu menagera comment_set, zato sto je komentar preko foreign keya (lin 38) povezan gore na image
                                            
    def vote_score(self):
        upvotes = self.vote_set.filter(upvote=True).count()   # vote_set je menadzer svih voteova vezanih na image i s njim mozemo radit razlicita filtriranja
        downvotes = self.vote_set.filter(upvote=False).count()
        return upvotes - downvotes
    
    # u modelu ova metoda prima usera jer model ne vidi req, brine se samo o business logici (kako su podatci spremljeni i kako se njima pristupa),
    # ne zna koji je user ulogiran zato sto on ne vidi requestove, zato mu iz viewa moramo kao parametar poslat usera koji je ulogiran
    # view ce pomocu req, session cookiea prepoznat koji je to user ulogiran i onda cemo u vote by metodu unutar image modela
    # poslat tog usera i onda preko njega mozemo vidit jel on voteao
    # i sad u vote_by zelimo vratit taj vote ako je user voteao
    def vote_by(self, user):    
        if user.is_authenticated:   # user kojeg smo poslali jer ga model inace ne vidi
            return Vote.objects.filter(user=user, image=self).first()   # dobit cemo vote za svaki image ako je user ulogiran (za taj image i tog usera daj mi vote), kad budemo pozivali pozivat cemo sa image.vote_by(request.user) u viewu i onda znamo da nam vraca vote koji je napravio taj user
        else:
            return None

class Comment(TimeStamped):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)  
    text = models.TextField(blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.text[:80]

    def author(self):   # implementacija ce nam bacat gresku (jer smo trazili field autora na raznim mjestima a tog fielda vise nemamo, migracija ce ga obrisat) pa umjesto da je autor field, rec cemo da je to metoda (da si olaksamo, posto autor i user su ista stvar, za autora cemo koristit user name)
        return self.user.username   # self.user jer sam user kao var ne postoji nego je to ovaj user definiran na samom komentaru (lin 53)


# Image i Comment nasljeduju TimeStamped, a model TimeStamped nasljeduje models.Model
# - na ovaj nacin napravili smo svoju apstraktnu klasu (vidimo po class Meta abstract=True)
#   sto znaci da mozemo napravit model kojeg nasi modeli nasljeduju i taj model onda uvijek ima 
#   implementiranu neku odredenu funkcionalnost 
#       -> TimeStamped omogucuje da si napravimo created_at i updated_at polja i overloadamo save(..) metodu
#       -> svaki put kad se snimi nas model mi cemo postavit polje u bazi created_at i updated_at 
#       -  created_at postavljamo samo prvi put (provjeravamo nije li on vec postavljen, ako nije, postavimo),
#           a updated_at postavljamo svaki put kad se ovaj model snimi 

#       -> na taj nacin i Image i Comment (i svi ostali koji bi nasljedivali TimeStamped) dobivaju polja created_at i updated_at
#       - onda bez ikakvog truda znamo u kojem je trenutku kreiran nas model (nas zapis u bazi kad nesto snimimo) i da li je mijenjan
#       - to vidimo kad npr. u detail pogledamo ispis podataka za komentare, mi ispisujemo podatak created_at, ali on se ne nalazi u formi za submit komentara
#         nego zbog nasljedene TimeStamped klase omogucen je taj ispis

#       ovo nije po defaultu u djangu ali je korisna stvar jer na ovaj nacin npr radi Ruby on Rails gdje svaki model
#       automatski dobije created_at i updated_at sto je dobra praksa

class Vote(TimeStamped):
    image = models.ForeignKey(Image, on_delete=models.CASCADE) # on delete cascade -> ako se obrise image na koji je nas vote (preko fk) vezan, onda ce baza sama pobrisati taj vote, jer si baza ne smije dopustiti situaciju tipa da imamo image1 i vote (koji referencira na fk image1) i kad obrisemo image1 da vote ostane visiti u zraku
    user = models.ForeignKey(User, on_delete=models.CASCADE)   # isto, ak obrisemo usera, brisu se svi njegovi voteovi
    upvote = models.BooleanField(null=False, default=True)     # ako postoji vote provjeravamo jel upvote, ako nije radi se o downvoteu (ako nitko nije glasao, zapis vote u tablici nece ni postojati), moramo rec da ne dozvoljavamo da bude null, a default moramo definirati

    class Meta:
        constraints = [  # mora bit jedinstvena kombinacija, constraint mora imat naziv i polja koja moraju bit jedinstvena su image i user
            models.UniqueConstraint(name='user_vote', fields=['image', 'user'])  # osiguranje na razini baze koje osigurava da isti user ne moze staviti vise voteova
        ]
    def __str__(self):
        return f"{self.user.username} voted on {self.image.title}"  # f -> evaluacija teksta iz viticastih, radimo ispis voteanja
        
    def downvote(self):  # kad zelimo vidit jel nesto downvote (cisto da mozemo napisat if downvote umjesto if not upvote)
        return not self.upvote
