from django.db import models
from authors.models import Author

class Article(models.Model):
  author = models.ForeignKey(Author)
  title = models.CharField(max_length=30)
  content = models.TextField()
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True, auto_now_add=True)

  def __unicode__(self):
    return u'%s' %(self.name)

  class Meta:
    db_table = "articles"