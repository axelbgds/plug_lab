from django.contrib.auth.models import Group  
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.decorators import permission_classes
from django.http import JsonResponse


@permission_classes([IsAuthenticated, DjangoModelPermissions])
def list_posts(request):
  return JsonResponse({'message':'Liste des posts'})

@permission_classes([IsAuthenticated, DjangoModelPermissions])  
def get_post(request, id):
  return JsonResponse({'message':'Récupération du post {}'.format(id)})
  

@permission_classes([IsAuthenticated, DjangoModelPermissions])
def add_post(request):
  return JsonResponse({'message':'Ajout d\'un post'})

@permission_classes([IsAuthenticated, DjangoModelPermissions])
def update_post(request, id):
  return JsonResponse({'message':'Mise à jour du post {}'.format(id)})

@permission_classes([IsAuthenticated, DjangoModelPermissions])
def delete_post(request, id):
  return JsonResponse({'message':'Suppression du post {}'.format(id)})