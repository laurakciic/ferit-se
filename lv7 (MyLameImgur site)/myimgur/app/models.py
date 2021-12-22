from django.db import models
from django.utils import timezone

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
        return image.comment_set.count()    # vraca broj komentara pomocu menagera comment_set
                                            # zato sto je komentar preko foreign keya (lin 38) povezan gore na image
    def votes(self):
        return self.upvotes - self.downvotes

class Comment(TimeStamped):
    image = models.ForeignKey(Image, on_delete=models.CASCADE)  
    text = models.TextField(blank=False)
    author = models.CharField(max_length=256, blank=False)

    def __str__(self):
        return self.text[:80]
    
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