from django.db import models
from django.utils.safestring import mark_safe

# Create your models here.
class MenuItem(models.Model):
    name=models.CharField(max_length=100)
    parent = models.ForeignKey('MenuItem',null=True)
    link=models.CharField(max_length=200)
    def __unicode__(self):
        return mark_safe('<a href="{0}">{1}</a>'.format(self.link,self.name))
