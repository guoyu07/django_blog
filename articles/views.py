from django.shortcuts import render, render_to_response, RequestContext
from articles.models import Article, Author
from django.contrib.syndication.views import Feed
from django.views.decorators.csrf import csrf_protect

def index(request):
  articles = Article.objects.order_by('id')
  return render_to_response('articles/index.html', {'articles': articles})

@csrf_protect
def new(request):
  return render_to_response('articles/new.html', context_instance=RequestContext(request))

def create(request):
  name = request.POST.get('name', '')
  title = request.POST.get('title', '')
  author = Author.objects.get(name=name)
  article = Article(title=title, author=author)
  article.save()
  articles = Article.objects.order_by('id')
  return render_to_response('articles/index.html', {'articles': articles})