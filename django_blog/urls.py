from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^authors/$', 'authors.views.index'),
    url(r'^authors/new$', 'authors.views.new'),
    url(r'^authors/create$', 'authors.views.create'),

    url(r'^articles/$', 'articles.views.index'),
    url(r'^articles/new$', 'articles.views.new'),
    url(r'^articles/create$', 'articles.views.create'),

    url(r'^$', 'authors.views.index'),
    url(r'', 'authors.views.index'),
)
