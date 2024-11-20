from django.shortcuts import render

# Create your views here.

def home(request):
  context = {}
  return render(request, 'home.html', context)

def about(request):
  context = {}
  return render(request, 'about.html', context)

def all_posts(request):
  context = {}
  return render(request, 'posts/posts.html', context)