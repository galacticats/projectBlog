from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 100)
    date = models.DateTimeField(auto_now_add = True)
    author = models.CharField(max_length = 100, default="Anonymous")
    body = models.TextField()
    slug = models.SlugField()
    picture = models.ImageField(default="defaultPic.png", blank="True")

    def __str__(self):
        return self.title
        
    def getSnippet(self):
        return self.body[:250] + "..."
