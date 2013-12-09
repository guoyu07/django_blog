from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'django_blog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^authors/$', 'blog.views.author_index'),
    url(r'^authors/new$', 'blog.views.author_new'),
    url(r'^authors/create$', 'blog.views.author_create'),

    url(r'^articles/$', 'blog.views.article_index'),
    url(r'^articles/new$', 'blog.views.article_new'),
    url(r'^articles/create$', 'blog.views.article_create'),
    url(r'^articles/show', 'blog.views.article_show'),

    url(r'^comments/$', 'blog.views.comment_index'),
    url(r'^comments/create$', 'blog.views.comment_create'),

    url(r'^accounts/login$', 'blog.views.account_login'),
    url(r'^accounts/logout$', 'blog.views.account_logout'),

    url(r'^$', 'blog.views.home'),
    url(r'', 'blog.views.home'),
)
