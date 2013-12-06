from django.shortcuts import render, render_to_response, RequestContext
from blog.models import Article, Author, Comment
from django.contrib.syndication.views import Feed
from django.views.decorators.csrf import csrf_protect

# home view
def home(request):
    articles = Article.objects.order_by('id')
    return render_to_response('home/index.html', {'articles': articles})

# author methods
def author_index(request):
    authors = Author.objects.order_by('id')
    return render_to_response('authors/index.html', {'authors': authors})

@csrf_protect
def author_new(request):
    return render_to_response('authors/new.html', context_instance=RequestContext(request))

def author_create(request):
    name = request.POST.get('name', '')
    author = Author(name=name)
    author.save()
    authors = Author.objects.order_by('id')
    return render_to_response('authors/index.html', {'authors': authors})

# article methods
def article_index(request):
    articles = Article.objects.order_by('id')
    return render_to_response('articles/index.html', {'articles': articles})

@csrf_protect
def article_new(request):
    return render_to_response('articles/new.html', context_instance=RequestContext(request))

def article_create(request):
    name = request.POST.get('name', '')
    title = request.POST.get('title', '')
    author = Author.objects.get(name=name)
    article = Article(title=title, author=author)
    article.save()
    articles = Article.objects.order_by('id')
    return render_to_response('articles/index.html', {'articles': articles})

# comment methods
def comment_index(request):
    comments = Comment.objects.order_by('id')
    return render_to_response('comments/index.html', {'comments': comments})
