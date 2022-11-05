from django.db import models

# Create your models here.
class Post(models.Model):
    title = models.CharField(max_length=200,verbose_name="Title",help_text="Enter title")
    body = models.TextField(verbose_name="Body",help_text="Enter post description")
    def  __str__(self):
        return self.title
    class Meta:
        verbose_name="Post "
        verbose_name_plural = "Posts "