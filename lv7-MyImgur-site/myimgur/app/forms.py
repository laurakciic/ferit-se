from bootstrap_datepicker_plus.widgets import DateTimePickerInput
from .models import Image, Comment      # jer za njih cemo imat forme
from django.forms import ModelForm

# nova slika: 
#   1. forms.py -> ImageForm
#   2. views.py -> kazemo napravi taj ImageForm, u contextu ga spremi kao form i sad dalje mozes radit s tim form
#   3. u templateu create_image.html -> postavimo html str, includeamo base4_form koji smo slozili da koristi bootstrap i da nam prikazuje sva ona polja, help textove i errore koji se pojave za svako polje unutar forme
#                                    -> formu vidljivu iz contexta trebamo proslijedit u taj include i onda ju mozemo koristit (with form=form)

class ImageForm(ModelForm):
    class Meta:
        model = Image   # model koji gadamo
        fields = ['title', 'url', 'description', 'pub_date']    # fieldovi koje zelimo u formi
        widgets = { 'pub_date': DateTimePickerInput() }

class CommentForm(ModelForm):
    class Meta:
        model = Comment
        fields = ['text']
