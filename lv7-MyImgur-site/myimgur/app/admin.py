from django.contrib import admin
from .models import Image, Comment

class CommentInline(admin.StackedInline):
    model = Comment
    extra = 0

class ImageAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    #fields = ['title', 'url', 'pub_date', 'description']

# Register your models here.
admin.site.register(Image, ImageAdmin)
admin.site.register(Comment)
