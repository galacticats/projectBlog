from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout
from django.contrib.auth.models import User
from django.apps import apps

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('articles:articles')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form':form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            return redirect('articles:articles')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form':form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('home')

@login_required(login_url='/accounts/login/')
def account_view(request):
    account = User.objects.get(username=request.user)
    uname = account.get_username()
    Article = apps.get_model('Articles', 'Article')
    articles = Article.objects.filter(author=account)
    return render(request, 'accounts/accountPage.html', {'uname':uname, 'articles':articles})

@login_required(login_url="/accounts/login/")
def change_password_view(request):
    if request.method == 'POST':
        logout(request)
        #TODO: change password here
        return redirect('login')

@login_required(login_url="/accounts/login/")
def delete_account_view(request):
    if request.method == 'POST':
        account = User.objects.get(username=request.user)
        logout(request)
        #delete their articles
        Article = apps.get_model('Articles', 'Article')
        articles = Article.objects.filter(author=account)
        for article in articles:
            article.delete()
        #then delete the user
        account.delete()
        return redirect('home')