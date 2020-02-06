from django.shortcuts import render

def homepage_view(request):
    return render(request, 'index.html')

def about_view(request):
    return render(request, 'about.html')
