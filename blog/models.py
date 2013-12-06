from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return u'%s' %(self.name)

    class Meta:
        db_table = "authors"


class Article(models.Model):
    author = models.ForeignKey(Author)
    title = models.CharField(max_length=30)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return u'%s' %(self.title)

    class Meta:
        db_table = "articles"


class Comment(models.Model):
    author = models.ForeignKey(Author)
    article = models.ForeignKey(Article)
    content = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True, auto_now_add=True)

    def __unicode__(self):
        return u'%s' %(self.content)

    class Meta:
        db_table = "comments"