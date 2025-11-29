from django.contrib import admin
from .models import Post
# class 
class PostAdmin (admin.ModelAdmin):
    list_display=['id','post_title','post_author','post_categor']
    list_url=['id','post_title']
    list_filter=['publish_date']
    search_fields=['post_title']
# Register your models here.
admin.site.register(Post,PostAdmin)

