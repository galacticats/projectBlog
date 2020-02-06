from django.shortcuts import render
from .models import Article

# Create your views here.
def article_list_view(request):
    articles = Article.objects.all().order_by('date').reverse()
    return render(request, 'articles/article_list.html', {'articles':articles})
    