from django.contrib import admin
from api.models import Category, Post, Comment

# Register your models here.
admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Comment)