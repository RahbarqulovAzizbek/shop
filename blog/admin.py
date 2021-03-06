from django.contrib import admin
from .models import *


# Register your models here.
@admin.register(BlogPostModel)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'created_at']
    list_filter = ['created_at', 'tags']
    search_fields = ['title', 'tags', 'description']
    list_display_links = ['title']


@admin.register(BlogTegModel)
class BlogTagAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', ]
    search_fileds = ['title']
    link_display_links = ['title']


@admin.register(AuthorModel)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ['id', 'full_name']
    list_display_links = ['full_name']
    search_fields = ['first_name', 'last_name']
