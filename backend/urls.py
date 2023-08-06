from django.urls import path
from . import views
from .views import list_posts, get_post, add_post, update_post, delete_post
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [

  path('api/v1/posts/', views.list_posts),
  path('posts/', list_posts),
  path('posts/<int:id>/', get_post),
  path('posts/add/', add_post),
  path('posts/<int:id>/update/', update_post),
  path('posts/<int:id>/delete/', delete_post),
  path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]