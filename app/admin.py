
from django.contrib import admin
from app.models import Category, Image

@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}

admin.site.register(Image)