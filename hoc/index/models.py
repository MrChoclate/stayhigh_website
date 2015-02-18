#!/usr/bin/env python
# coding: utf-8

from django.db import models

class Challenge(models.Model):
    first_name = models.CharField("Prénom", max_length=30, blank=True)
    last_name = models.CharField("Nom", max_length=30, blank=True)
    mail = models.EmailField("Email", blank=True)
    content = models.TextField("Le Défi", blank=False)

    def __unicode__(self):
        return self.first_name + self.content
