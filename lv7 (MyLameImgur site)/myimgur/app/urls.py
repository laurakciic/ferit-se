from django.urls import path

from . import views

app_name = 'app'    # sve rute ce bit u app (pocinjat ce sa app:index, app:detail, app:comment)
urlpatterns = [
    path('', views.index, name='index'),
    path('<int:image_id>/', views.detail, name='detail'),           # ako imamo images/broj/ onda to renderira detail
    path('<int:image_id>/comment', views.comment, name='comment'),  # ako imamo images/broj/comment onda se to salje na views.comment
]
