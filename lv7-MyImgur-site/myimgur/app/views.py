from django.shortcuts import render, get_object_or_404, resolve_url
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Image, Comment, Vote
from .forms import ImageForm, CommentForm

# Create your views here.

def index(request):
    images = Image.objects.order_by('-pub_date')        # povlacenje objekata, sortiranje po pub dateu
    votes = [ image.vote_by(request.user) for image in images ]     # vote_by ce nam vratit ili vote (ako vote postoji za tog usera) ili none ako ne postoji
    context = { 'images_with_votes': zip(images, votes)}            # postavimo ih u context, zip je ugradena fja koja spaja dva polja, na ovaj nacin cemo na istim mjestima (kad iteriramo kroz tu listu, kroz images_with_votes) dobit cemo po jedan image i njegov vote   
    return render(request, 'app/index.html', context)   # pomocu rendera prosljedujemo context u index.html kao i request

def detail(request, image_id):
    image = get_object_or_404(Image,pk=image_id)        # dohvaca obj iz Image modela preko pk onaj koji ima image_id
    context = {'image': image,                          # image je ovaj objekt sto se povlaci s get obj or 404
               'vote': image.vote_by(request.user), 
               'comments': image.comment_set.all(),     # povucemo sve komentare kako bi ih mogli ispisati unutar samog templatea
               'form': CommentForm(),   # buduci da nam je stavljanje komentara sa samog detail viewa, moramo kao i u comment form, ovdje dodati praznu formu 
              }
    return render(request, 'app/detail.html', context)

def create_image(request):              # image_id nije potreban jer kad pravimo novu sliku nemamo jos image_id
    if request.method == 'POST':        # ako je forma submitana
        form = ImageForm(request.POST)  # izgenerirat ce formu pomocu POST req
        if form.is_valid():
            saved_image = form.save()   # form.save() uzima podatke iz req, stavlja ih u model, pravi validaciju ako je forma ispravna (data ispravni), sprema u bazu i rezultat toga je image koji ce se spremit u var saved_image
            return HttpResponseRedirect(reverse('app:detail', args=(saved_image.id,)))  # saljemo ga na prikazanu sliku, args su primljeni argumenti
    else:
        form = ImageForm()              # ako nije POST req (ako nije submitana), izgenerirat ce novu praznu formu 
    
    context = { 'form': form, 'action': 'create' }   # posto nas template uvijek prima context trebamo tu var napravit, action create zbog razlike dvije akcije gumbova (create image/update image)
    return render(request, 'app/create_image.html', context)    # u render ide request, template i context

def update_image(request, image_id):
    image = get_object_or_404(Image, pk=image_id)
    if request.method == 'POST':        # ako je forma submitana
        form = ImageForm(request.POST, instance=image)  # pri kreiranju forme kreira sve fieldove potrebne za formu i buduci da smo je povezali preko instance sa image, znat ce koji je id te slike i nece pokusat napravit novu, nego ce presnimit podatke koji su se promijenili preko onih postojecih
        if form.is_valid():
            saved_image = form.save()   
            return HttpResponseRedirect(reverse('app:detail', args=(saved_image.id,)))  
    else:
        form = ImageForm(instance=image)  # ne radi se novi image nego ce presnimit podatke koji su se promijenili preko onih postojecih
    
    context = { 'form': form, 'action': 'update'}          
    return render(request, 'app/create_image.html', context)  # ne moramo mijenjat template koji se renderira jer ce on sadrzavat sva ista polja i on je minimalan

def delete_image(request, image_id):      # problem kako cemo pozvat delete metodu - konvencija je kad god se na serveru nesto mijenja treba bit post req, a njega ne mozemo dobit samo klikom na link, mora doc do submita forme 
    image = get_object_or_404(Image, pk=image_id)   # rjesenje je preko skrivenih formi 
    if request.method == 'POST' and request.user.is_authenticated:
        image.delete()
    return HttpResponseRedirect(reverse('app:index'))

def comment(request, image_id):         # na samom detail viewu cemo napravit tu formu i onda ce ovaj comment obradivat samo POST req
    if request.method == 'POST' and request.user.is_authenticated:
        image = get_object_or_404(Image, pk=image_id)
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)   # commit false govori da se ne sprema u bazu, napravit ce se instanca modela comment ali se nece snimit u bazu dok ga mi ne snimimo zbog toga sto mi u nasu formu ne upisujemo image, znamo za koji image submitamo komentar (zbog image_id)
            comment.image = image               # u instancu modela comment spremi ovaj image koji smo dobili iz get_obj_or_404
            comment.save()                      # sad je spremljeno u bazu
            return HttpResponseRedirect(reverse('app:detail', args=(comment.image.id,)))   # pokazujemo sliku na kojoj se nalazimo (app:detail)
        else:
            # u detail gore vidimo da context mora sadrzavat image i comments pa moramo da bi renderirali ponovo detail predat takav isti context
            return render(request, 'app:detail', {   
                'image': image,
                'comments': image.comment_set.all(),
                'form': form,       # buduci da nam je stavljanje komentara sa samog detail viewa, moramo tamo, kao i ovdje dodati praznu formu 
            })
    else:                           # ne mozemo racunat ni na koji image osim iz funkciji predanog image_id
        return HttpResponseRedirect(reverse('app:detail', args=(image_id,)))  

def vote(request, image_id, upvote):
    image = get_object_or_404(Image, pk=image_id)
    vote = Vote.objects.filter(user=request.user, image=image).first() # select * from vote where user.id = id usera iz req and where image_id = id slike, first() daje prvi element (isto kao limit 1)
    if vote:
        if vote.upvote == upvote:   # ako je dvaput kliknemo upvote ili downvote zelimo obrisat vote
            vote.delete()
            return None
        else:
            vote.upvote = upvote    # ako je napravio upvote i klikne na upvote, ovdje ce se pronac taj vote, postavit ce mu se ponovo upvote i to ce se spremiti
    else:
        vote = Vote(user=request.user, image=image, upvote=upvote)  # ako je vec voteao i klikne na downvote, onda ce se taj vote pronac i upvote se promijenit u downvote i to ce se spremit
    try:
        vote.full_clean()   # ciscenje modela - vrsenje validacije, ako vec postoji da je isti user voteao na isti image, onda ce se constraint iz admina okinit i ovdje
        vote.save()
    except:
        return None         # vracamo none da se nije ispravno spremilo
    else:
        return vote         # ako su obje naredbe prosle, vote je spremljen u bazu i vracamo taj vote

# upvote i downvote su akcije pa ih mozemo napravit kao buttone, ne moramo imat skrivenu formu koju smo okidali s jqueryjem nego mozemo direktno napravit formu koja poziva upvote i downvote akcije
def upvote(request, image_id):      # prima image_id jer smo ga urls.py isparsirali iz url-a, da bi se nesto promijenilo na serveru -> treba bit POST req, u tom slucaju onda mozemo napravit formu, i za svaki image napravimo formu i tu formu postamo
    if request.method == 'POST' and request.user.is_authenticated:
        vote(request, image_id, True)
    return HttpResponseRedirect(reverse('app:detail', args=(image_id,)))   # image_id jer smo njega dobili u req

def downvote(request, image_id):
    if request.method == 'POST' and request.user.is_authenticated:
        vote(request, image_id, False)
    return HttpResponseRedirect(reverse('app:detail', args=(image_id,)))
    