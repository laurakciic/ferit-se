from django.urls import path

from . import views     # from . oznacava trenutni direktorij acc (app acc) tak da ce targetirat views iz acc

app_name = 'accounts'   # namespaceamo ga u accounts app
urlpatterns = [                                                    # vucemo SignUpView klasu koju renderiramo as_view
    path('sign-up', views.SignUpView.as_view(), name='signup'),    # unutar accounts view bit ce genericka klasa view koja ce odradivat ovaj sign up (djangova sign up forma)
    

]