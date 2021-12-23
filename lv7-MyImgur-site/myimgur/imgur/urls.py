"""imgur URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include,path
from app import views   # importamo views jer zelimo u slucaju root urla okinuti views.index (zelimo poslat korisnika na index)
                        # cilj je da kad otvorimo localhost:8000 da odma otvori index, ne moramo pisat cijelu putanju 
urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
    path('images/', include('app.urls')),   # cijelu app.urls kacimo u images path jer onda svaka putanja sto pocinje s images gledat ce urlove s app.images
    path('', views.index, name='index'), 
]