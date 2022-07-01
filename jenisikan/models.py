from django.db import models

# Create your models here.

class JenisIkan(models.Model):   
    j_ikan = models.CharField(default="", max_length = 100, blank= False)
    g_ikan = models.TextField(max_length = 255, blank=False)
    h_kg = models.IntegerField(blank=False)
    h_ton = models.IntegerField(blank=False)

