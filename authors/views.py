from django.shortcuts import render, render_to_response
from authors.models import Author
from django.contrib.syndication.views import Feed

def list_authors(request):
  authors = Author.objects.order_by('id')
  return render_to_response('authors/index.html', {'authors': authors})