from django.db import models
from django.utils.html import escape
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
    def url(self):
        return escape(self.title.replace(" ",'_'))

class Entry(models.Model):
    body = models.TextField()
    title = models.CharField(max_length=200)
    publish_date = models.DateField()
    tags = models.ManyToManyField(Tag)
    category = models.ForeignKey(Category)
    def __unicode__(self):
       return unicode(self.category)+":"+unicode(self.title)+" - "+str(self.publish_date)
    def url(self):
        return escape(self.title.replace(" ",'_'))
