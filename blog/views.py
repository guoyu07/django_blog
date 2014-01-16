from django.shortcuts import render_to_response, RequestContext, redirect
from blog.models import Article, Author, Comment
from django.views.decorators.csrf import csrf_protect
from django.views.decorators.cache import cache_page
from django.core.cache import cache


# home view
def home(request):
    articles = Article.objects.order_by('id')
    return render_to_response('home/index.html', {'articles': articles}, context_instance=RequestContext(request))

# account view
def account_login(request):
    author_id = request.GET.get('author_id', None)
    if author_id is not None and author_id != '':
        author = Author.objects.get(id=author_id)
        request.session["author_name"] = author.name
        print "set session author_name %s" %request.session["author_name"]
        return redirect('/')
    else:
        authors = Author.objects.order_by('id')
        return render_to_response('accounts/login.html', {'authors': authors}, context_instance=RequestContext(request))

def account_logout(request):
    del request.session["author_name"]
    return redirect('/')

# author methods
def author_index(request):
    authors = Author.objects.order_by('id')
    return render_to_response('authors/index.html', {'authors': authors}, context_instance=RequestContext(request))

@csrf_protect
def author_new(request):
    return render_to_response('authors/new.html', context_instance=RequestContext(request))

def author_create(request):
    name = request.POST.get('name', '')
    author = Author(name=name)
    author.save()
    authors = Author.objects.order_by('id')
    return render_to_response('authors/index.html', {'authors': authors}, context_instance=RequestContext(request))

# article methods
@cache_page(60*2)
def article_index(request):
    articles = Article.objects.order_by('id')
    return render_to_response('articles/index.html', {'articles': articles}, context_instance=RequestContext(request))


def article_show(request):
    article_id = request.GET.get('id', '')
    comments_key = "comments_{}".format(article_id)
    article = cache.get(article_id)
    if not article:
        article = Article.objects.filter(id=article_id).first()
        comments =  article.comment_set.all()
        cache.set(article_id, article, 60*2)
        cache.set(comments_key, comments, 60*2)
    else:
        comments =  cache.get(comments_key)
    return render_to_response('articles/show.html', {'article': article, 'comments': comments}, context_instance=RequestContext(request))


@csrf_protect
def article_new(request):
    return render_to_response('articles/new.html', {}, context_instance=RequestContext(request))

def article_create(request):
    title = request.POST.get('title', '')
    content = request.POST.get('content', '')
    author = Author.objects.get(name=request.session["author_name"])
    article = Article(title=title, content=content, author=author)
    article.save()
    articles = Article.objects.order_by('id')
    return render_to_response('articles/index.html', {'articles': articles}, context_instance=RequestContext(request))

# comment methods
def comment_index(request):
    comments = Comment.objects.order_by('id')
    return render_to_response('comments/index.html', {'comments': comments}, context_instance=RequestContext(request))

def comment_create(request):
    article_id = request.POST.get('article_id', '')
    content = request.POST.get('content', '')
    article = Article.objects.get(id=article_id)
    author = Author.objects.get(name=request.session["author_name"])
    comment = Comment(content=content, author=author, article=article)
    comment.save()
    return redirect('/articles/show?id=%d'%article.id)


