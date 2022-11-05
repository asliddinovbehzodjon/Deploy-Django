from django.contrib import admin
from .models import Post
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_filter = ['title']
    list_display = ['title']
    search_fields = ['title','body']