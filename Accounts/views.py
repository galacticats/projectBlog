from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User
from django.apps import apps
from django.contrib.auth.password_validation import validate_password
from urllib.parse import urlencode
from django.urls import reverse

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
    errorMessage = request.GET.get('errorMessage', None)
    account = User.objects.get(username=request.user)
    uname = account.get_username()
    Article = apps.get_model('Articles', 'Article')
    articles = Article.objects.filter(author=account)
    return render(request, 'accounts/accountPage.html', {'uname':uname, 'articles':articles, 'errorMessage':errorMessage})

@login_required(login_url="/accounts/login/")
def change_password_view(request):
    if request.method == 'POST':
        account = User.objects.get(username=request.user)
        user = authenticate(username=request.user, password=request.POST.get("oldPassword"))
        if user is not None:
            if request.POST.get("newPassword") == request.POST.get("confirmPassword"):
                account.set_password(request.POST.get("newPassword"))
                if validate_password(request.POST.get("newPassword"), request.user) is None:
                    account.save()
                    logout(request)
                    return redirect('home')
                else:
                    errorMessage="Your new password must have at least 8 characters, cannot be entirely numeric, cannot be too common, and cannot be too similar to your username."
            else:
                errorMessage="Your new passwords did not match."
        else:
            errorMessage="Your old password was incorrect."
        #if something was wrong with the old or new passwords, create an account page url with an error message and redirect the user there
        baseURL = reverse("accounts:account")
        queryString = urlencode({'errorMessage':errorMessage})
        url = '{}?{}'.format(baseURL, queryString)
        print(url)
        return redirect(url)

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