from django.db import models

# Create your models here.
class MenuItem(models.Model):
    name=models.CharField(max_length=100)
    parent = models.ForeignKey('MenuItem',null=True)
    link=models.CharField(max_length=200)
    def __unicode__(self):
