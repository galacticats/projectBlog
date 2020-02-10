from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Article
from . import forms

# Create your views here.
def article_list_view(request):
    articles = Article.objects.all().order_by('date').reverse()
    return render(request, 'articles/article_list.html', {'articles':articles})
    
def article_detail(request, slug):
    article = Article.objects.get(slug = slug)
    return render(request, 'articles/article_detail.html', {"article":article})

@login_required(login_url='/accounts/login/')
def create_article(request):
    if request.method == "POST":
        form = forms.ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            db_Entry = form.save(commit=False)
            db_Entry.author = request.user
            db_Entry.save()
            return redirect('articles:articleDetail', slug=db_Entry.slug)
    else:
        form = forms.ArticleForm()
    return render(request, 'articles/create_article.html', {'form':form})

@login_required(login_url='/accounts/login/')
def edit_article(request):
    db_Entry = Article.objects.get(slug = request.POST.get('slug'))
    return render(request, 'articles/edit_article.html', {"article":db_Entry})

@login_required(login_url='/accounts/login/')
def delete_article(request):
    if request.method == "POST":
        db_Entry = Article.objects.get(slug = request.POST.get('slug'))
        db_Entry.delete()
    return redirect('articles:articles')

@login_required(login_url='/accounts/login/')
def save_changes(request): 
    return HttpResponse("Updating post and saving changes!")
