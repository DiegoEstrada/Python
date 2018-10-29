from django.contrib import admin

# Register your models here.
from album.models import Category, Photo

admin.site.register(Category)
admin.site.register(Photo)
