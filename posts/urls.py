from django.urls import path
from .views import list_posts, get_post, add_post, update_post, delete_post

urlpatterns = [

  path('posts/', list_posts),
  path('posts/<int:id>/', get_post),
  path('posts/add/', add_post),
  path('posts/<int:id>/update/', update_post),
  path('posts/<int:id>/delete/', delete_post),

]