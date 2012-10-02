from django.db import models

# Create your models here.
class TokensBank(models.Model):
    c_token = models.CharField(max_length=60)
    c_expiry = models.DateTimeField()
    refresh_token =models.CharField(max_length=800)
    code=models.CharField(max_length=70)
    a_service = models.CharField(max_length=20)