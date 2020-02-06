from django.db import models

# Create your models here.
class Article(models.Model):
    title = models.CharField(max_length = 50)
    date = models.DateTimeField(auto_now_add = True)
    body = models.TextField()
    slug = models.SlugField()
    #picture = [look up later]


    def __str__(self):
        return self.title
        
    def getSnippet(self):
        return self.body[:250] + "..."
