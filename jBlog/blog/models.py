from django.db import models
from django.contrib import admin
import textwrap
# Create your models here.
class Tag(models.Model):
    title = models.CharField(max_length=200)
    #entries = models.ManyToManyField("Entry")
    def __unicode__(self):
         return "{0}".format(self.title)

class Category(models.Model):
    title = models.CharField(max_length=200)
    def __unicode__(self):
         return "{0}".format(self.title)

class Entry(models.Model):
    body = models.TextField()
    title = models.CharField(max_length=200)
    publish_date = models.DateField()
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category)
    def __unicode__(self):
       return unicode(self.category)+":"+unicode(self.title)+" - "+str(self.publish_date)
    def stub(self):
       stb = '<div class="article">'
       stb += '<div class="article_header">{0}</div>'.format(self.title)
       stb += '<div class="article_main">{0}</div>'.format(textwrap.wrap(self.body,300)[0])
       stb += "</div>"
       return stb

