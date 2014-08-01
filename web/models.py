
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.
SUPPORTED_LANG = (
  (0, 'English'),
  (1, 'Traditional Chinese'),
  (2, 'Simplified Chinese'),
)

class Choice(models.Model):
  title = models.CharField(max_length=200)
  lang = models.IntegerField(default=1, choices=SUPPORTED_LANG)

class Poll(models.Model):
  title = models.CharField(max_length=200)
  choice = models.ForeignKey(Choice)
  content = RichTextField(blank=True)
  create_date = models.DateTimeField('created date')
  modify_date = models.DateTimeField('modified date')
  lang = models.IntegerField(default=1, choices=SUPPORTED_LANG)
