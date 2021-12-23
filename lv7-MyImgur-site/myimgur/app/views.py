from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Image, Comment
from .forms import ImageForm

# Create your views here.

def index(request):
    images = Image.objects.order_by('-pub_date')        # povlacenje objekata, sortiranje po pub dateu
    context = { 'images': images}                       # postavimo ih u context
    return render(request, 'app/index.html', context)   # pomocu rendera prosljedujemo context u index.html kao i request

def detail(request, image_id):
    image = get_object_or_404(Image,pk=image_id)        # dohvaca obj iz Image modela preko pk onaj koji ima image_id
    context = {'image': image,                          # image je ovaj objekt sto se povlaci s get obj or 404
               'comments': image.comment_set.all(),     # povucemo sve komentare kako bi ih mogli ispisati unutar samog templatea
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
    
    context = { 'form': form }          # posto nas template uvijek prima context trebamo tu var napravit
    return render(request, 'app/create_image.html', context)    # u render ide request, template i context


def comment(request, image_id):
    image = get_object_or_404(Image, pk=image_id)       
    try:
        comment = image.comment_set.create(
                   author=request.POST['author'],   # kreiranje komentara iz requesta (POST author i POST comm 
                   text=request.POST['comment'],    # iz req izvucemo i stavimo u var author i text)
                )
    except (KeyError, Comment.DoesNotExist):            # renderiramo ponovo detail samo ako se dogodi error
        # Redisplay the comment posting form.           # ako se  pri komentiranju dogodi error, onda ce se error msg postavit u context
        return render(request, 'app/detail.html', {     # i kad se on renderira onda ce taj isti detail.html pokazat error msg
            'image': image,
            'error_message': "Posting failed!",     
        })                                          
    else:
        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('app:detail', args=(image.id,)))
        # salje redirect na tu istu sliku i omogucuje da se ne posta dvaput isti komentar
        # zbog toga sto smo redirectali nazad na detail gdje taj komentar nije upisan i refresh nece okinit ponovo post req

