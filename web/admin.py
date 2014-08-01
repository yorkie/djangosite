
import opencc
from django import forms
from django.contrib import admin
from web.models import Poll, Choice
from custom_widgets import ColourChooserWidget
from string import Template
from django.utils.safestring import mark_safe

# initial the t2s object
converter = opencc.OpenCC('t2s')

class ChoiceAdmin(admin.ModelAdmin):

  fields = ('title',)

  def save_form(self, request, form, change):
    title = form.cleaned_data.get('title')
    print converter.convert('haha')
    return super(ChoiceAdmin, self).save_form(request, form, change)

# Register your models here.
admin.site.register(Poll)
admin.site.register(Choice, ChoiceAdmin)