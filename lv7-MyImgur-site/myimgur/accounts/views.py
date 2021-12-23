from django.shortcuts import render

# Create your views here.
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views import generic

class SignUpView(generic.CreateView):
    form_class = UserCreationForm           # lazy jer jos nisu definirane rute (pri kreiranju class base viewa prvo se rado evaluacija parametara a kasnije se tek koristi kao view), a to se mora pokrenit u trenutku kad budemo generirali ovaj view
    success_url = reverse_lazy('login')     # ako je uspjesno kreiran sign up, reverse fja daje url za odredenu rutu prema njenom imenu
    template_name = 'registration/signup.html'  # naziv templatea kojeg cemo renderirat
    