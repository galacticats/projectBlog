from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import Article
from . import forms

# Create your views here.
def article_list_view(request):
    articles = Article.objects.all().order_by('dateP').reverse()
    return render(request, 'articles/article_list.html', {'articles':articles})
    
def article_detail(request, slug):
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {"article":article})

@login_required(login_url='/accounts/login/')
def create_article(request):
    if request.method == "POST":
        form = forms.ArticleForm(request.POST, request.FILES)
        if form.is_valid():
            db_entry = form.save(commit=False)
            db_entry.author = request.user
            db_entry.save()
            return redirect('articles:articleDetail', slug=db_entry.slug)
    else:
        form = forms.ArticleForm()
    return render(request, 'articles/create_article.html', {'form':form})

@login_required(login_url='/accounts/login/')
def edit_article(request):
    db_entry = Article.objects.get(slug=request.POST.get('slug'))
    form = forms.ArticleEditForm(initial={'body':db_entry.body}, instance=db_entry)
    return render(request, 'articles/edit_article.html', {"slug":db_entry.slug, "form":form})

@login_required(login_url='/accounts/login/')
def save_changes(request): 
    slugLine = request.POST.get('editSlug')
    db_entry = Article.objects.get(slug=slugLine)
    if request.method == "POST":
        authentication_form = forms.ArticleEditForm(request.POST, request.FILES, instance=db_entry)
        if authentication_form.is_valid():
            authentication_form.save()
            return redirect('articles:articleDetail', slug=slugLine)
    #if it doesn't work, then go back to the form page
    return redirect('articles:editArticle')

@login_required(login_url='/accounts/login/')
def delete_article(request):
    if request.method == "POST":
        db_entry = Article.objects.get(slug=request.POST.get('slug'))
        db_entry.delete()
    return redirect('articles:articles')