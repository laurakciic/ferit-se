from django.urls import path

from . import views

app_name = 'app'    # sve rute ce bit u app (pocinjat ce sa app:index, app:detail, app:comment)
urlpatterns = [     # naziv viewa i naziv rute nije povezan!
    path('', views.index, name='index'),
    path('<int:image_id>/', views.detail, name='detail'),           # (CRUD-R), ako imamo images/broj/ onda to renderira detail
    path('<int:image_id>/comment', views.comment, name='comment'),  # ako imamo images/broj/comment onda se to salje na views.comment
    path('<int:image_id>/upvote', views.upvote, name='upvote'),
    path('<int:image_id>/downvote', views.downvote, name='downvote'),
    path('new', views.create_image, name="create_image"),           # (CRUD-C), putanja: localhost8000/images/new, app:create_image
    path('<int:image_id>/edit', views.update_image, name="edit_image"),         # (CRUD-U)
    path('<int:image_id>/delete', views.delete_image, name="delete_image"),     # (CRUD-D)
]
