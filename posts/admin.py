from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):

  list_display = ('titre', 'auteur', 'date_creation')
  
  actions = ['make_published', 'make_unpublished']

  def make_published(self, request, queryset):
    queryset.update(status='P')
  
  def make_unpublished(self, request, queryset):
    queryset.update(status='D')
  
  make_published.short_description = "Marquer sélectionnés comme publiés"
  make_unpublished.short_description = "Marquer sélectionnés comme dépubliés"