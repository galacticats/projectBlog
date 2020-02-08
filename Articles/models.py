from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)
    date = models.DateTimeField(auto_now_add = True)
    author = models.ForeignKey(User, on_delete=models.SET_DEFAULT, default="[deleted]")
    body = models.TextField()
    slug = models.SlugField()
    picture = models.ImageField(default="defaultPic.png", blank="True")

    def __str__(self):
        return self.title
        
    def getSnippet(self):
        return self.body[:250] + "..."
