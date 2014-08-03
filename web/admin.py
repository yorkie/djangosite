
# coding=utf-8
import sys
from time import gmtime, strftime
from django.contrib.admin import widgets, helpers
from django import forms
from django.contrib import admin
from web.models import Category, Article
from web.utils.lang import SUPPORTED_LANG, is_traditional, is_simplified
from web.utils.opencc import convert
from string import Template
from django.utils.safestring import mark_safe

class CategoryAdmin(admin.ModelAdmin):
  fields = ('title', 'lang')

  def render_change_form(self, request, context, add=False, change=False, form_url='', obj=None):
    _context = context.get('original')
    if _context:
      context['adminform'].readonly_fields = self.fields
    return super(CategoryAdmin, self).render_change_form(request, context, add, change, form_url, obj)

  def save_model(self, request, obj, form, change):
    lang = form.cleaned_data.get('lang')
    title = form.cleaned_data.get('title')
    if is_traditional(lang):
      Category.sync_simplified_copy(title)
      obj.title = convert(title.encode('utf-8'), config='zhs2zht.ini').decode('utf-8')
    return super(CategoryAdmin, self).save_model(request, obj, form, change)

class ArticleAdmin(admin.ModelAdmin):
  fields = ('title', 'category', 'content', 'lang')
  readonly_fields = ('lang',)

  def save_model(self, request, obj, form, change):
    title = form.cleaned_data.get('title')
    lang = form.cleaned_data.get('category').lang
    obj.lang = lang

    try:
      o_form = form.initial
      o_title = o_form.get('title')
      o_category = o_form.get('category')

      if o_title:
        title = o_title
      if o_category:
        category = o_category
        lang = Category.objects.get(id=o_category).lang

      # simplified cn pass
      if not is_traditional(lang): raise

      # find the simplified title and save it
      s_title = convert(title.encode('utf-8')).decode('utf-8')
      s_category_title = convert(obj.category.title.encode('utf-8')).decode('utf-8')
      s_category = Category.objects.get(title=s_category_title)
      cur_time = gmtime()
      article, created = Article.objects.get_or_create(title=s_title, lang=2, defaults={
        'category': s_category,
        'create_date': strftime("%Y-%m-%d %H:%M:%S", cur_time),
        'modify_date': strftime("%Y-%m-%d %H:%M:%S", cur_time),
      })

      if not created:
        article_modify_date = article.modify_date
        article.modify_date = strftime("%Y-%m-%d %H:%M:%S", cur_time)
        article.title = s_title
        if article_modify_date > obj.modify_date: raise

      article.content = convert(form.cleaned_data.get('content').encode('utf-8')).decode('utf-8')
      article.save()

    except:
      pass

    if is_simplified(obj.lang):
      obj.title = convert(form.cleaned_data.get('title').encode('utf-8')).decode('utf-8')
      obj.content = convert(form.cleaned_data.get('content').encode('utf-8')).decode('utf-8')
    elif is_traditional(obj.lang):
      obj.title = convert(form.cleaned_data.get('title').encode('utf-8'), 
        config='zhs2zht.ini').decode('utf-8')
      obj.content = convert(form.cleaned_data.get('content').encode('utf-8'), 
        config='zhs2zht.ini').decode('utf-8')

    if not obj.create_date:
      obj.create_date = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    obj.modify_date = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    return super(ArticleAdmin, self).save_model(request, obj, form, change)

# Register your models here.
admin.site.register(Category, CategoryAdmin)
admin.site.register(Article, ArticleAdmin)