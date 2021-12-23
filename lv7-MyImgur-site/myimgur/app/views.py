from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Image, Comment

# Create your views here.

def index(request):
    images = Image.objects.order_by('-pub_date')        # povlacenje objekata, sortiranje po pub dateu
    context = { 'images': images}                       # postavimo ih u kontekst
    return render(request, 'app/index.html', context)   # pomocu rendera prosljedujemo context u index.html kao i request

def detail(request, image_id):
    image = get_object_or_404(Image,pk=image_id)        # dohvaca obj iz Image modela preko pk onaj koji ima image_id
    context = {'image': image,                          # image je ovaj objekt sto se povlaci s get obj or 404
               'comments': image.comment_set.all(),     # povucemo sve komentare kako bi ih mogli ispisati unutar samog templatea
              }
    return render(request, 'app/detail.html', context)

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

