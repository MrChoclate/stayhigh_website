from django.db import models

class Challenge(models.Model):
    first_name = models.CharField(max_length=30, blank=True)
    last_name = models.CharField(max_length=30, blank=True)
    mail = models.EmailField(blank=True)
    content = models.TextField()
    