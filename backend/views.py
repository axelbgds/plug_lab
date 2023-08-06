from django.db import DatabaseError
from django.http import JsonResponse
from django.core.serializers import serialize
import json
from posts.models import Post
from django.db.utils import OperationalError
from rest_framework.permissions import IsAuthenticated  
from rest_framework.decorators import permission_classes

# Read post
@permission_classes([IsAuthenticated])
def list_posts(request):

  try:
    posts = Post.objects.all()  
  except OperationalError:
    return JsonResponse({'error': 'Unable to connect to DB'}, status=500)
  
  if not posts:
    return JsonResponse({'error': 'No posts found'}, status=404)

  posts_json = serialize('json', posts)
  return JsonResponse(posts_json, safe=False)

# ---------------------------------------

# Get post
@permission_classes([IsAuthenticated])
def get_post(request, id):

  try:
    post = Post.objects.get(id=id, active=True) 
  except Post.DoesNotExist:
    return JsonResponse({'error': 'Post not found'}, status=404)

  post_json = serialize('json', [post])
  return JsonResponse({'post': post_json}, status=200)

# ---------------------------------------

# Add post
@permission_classes([IsAuthenticated])
def add_post(request):

  data = json.loads(request.body)

  if not all([data.get('titre'), data.get('contenu')]):
    return JsonResponse({'error': 'Data missing'}, status=400)    

  try: 
    post = Post.objects.create(
      titre=data['titre'],
      contenu=data['contenu']  
    )
  except DatabaseError: 
    return JsonResponse({'error': 'Unable to create post'}, status=500)

  return JsonResponse(post.id, safe=False)

# ---------------------------------------

# Update post
@permission_classes([IsAuthenticated])
def update_post(request, id):

  data = json.loads(request.body)

  try:
    post = Post.objects.get(id=id)
  except Post.DoesNotExist:
    return JsonResponse({'error': 'Post not found'}, status=404)

  post.titre = data.get('titre', post.titre)
  post.contenu = data.get('contenu', post.contenu)
  post.save()

  post_json = serialize('json', [post])

  return JsonResponse({'post': post_json}, status=200)

# ---------------------------------------

# Delete post
@permission_classes([IsAuthenticated])
def delete_post(request, id):
  
  try:
    post = Post.objects.get(id=id)
  except Post.DoesNotExist:
    return JsonResponse({'error': 'Post not found'}, status=404)

  post.delete()

  return JsonResponse({}, status=204)
