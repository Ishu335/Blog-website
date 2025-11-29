from django.db import models

class Post(models.Model):
    post_title=models.CharField(max_length=60)
    post_author=models.TextField(max_length=10)
    post_categor=models.TextField(max_length=10)
    likes=models.IntegerField(blank=True,null=True)
    post_content=models.TextField()
    publish_date=models.DateTimeField(auto_now=True) # auto change will the post is create or update 
    
    def __str__(self):
        return self.post_title
