
from django.db import models
from web.utils.lang import SUPPORTED_LANG
from web.utils.opencc import convert
from ckeditor.fields import RichTextField

class Category(models.Model):
  title = models.CharField(max_length=200)
  lang = models.IntegerField(default=1, choices=SUPPORTED_LANG)

  def __unicode__(self):
    return "%(lang)s -- %(title)s" % {'title': self.title, 'lang': SUPPORTED_LANG[self.lang][1]}

  @classmethod
  def sync_simplified_copy(cls, title):
    title_s = convert(title.encode('utf-8'))
    category, created = cls.objects.get_or_create(title=title_s, lang=2)
    category.save()
    return created

class Article(models.Model):
  title = models.CharField(max_length=200)
  category = models.ForeignKey(Category)
  content = RichTextField(blank=True)
  create_date = models.DateTimeField('created date')
  modify_date = models.DateTimeField('modified date')
  lang = models.IntegerField(default=1, choices=SUPPORTED_LANG)

  def __unicode__(self):
    return "(%(lang)s) %(title)s" % {'title': self.title, 'lang': SUPPORTED_LANG[self.lang][1]}
