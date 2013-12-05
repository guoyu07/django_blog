from django.shortcuts import render, render_to_response, RequestContext
from authors.models import Author
from django.contrib.syndication.views import Feed
from django.views.decorators.csrf import csrf_protect

def index(request):
  authors = Author.objects.order_by('id')
  return render_to_response('authors/index.html', {'authors': authors})

@csrf_protect
def new(request):
  return render_to_response('authors/new.html', context_instance=RequestContext(request))

def create(request):
  name = request.POST.get('name', '')
  author = Author(name=name)
  author.save()
  authors = Author.objects.order_by('id')
  return render_to_response('authors/index.html', {'authors': authors})