#!/usr/bin/env python
# coding: utf-8

from django.db import models

class Challenge(models.Model):
    first_name = models.CharField("Prénom", max_length=30, blank=True)
    last_name = models.CharField("Nom", max_length=30, blank=True)
    type = models.CharField(max_length=1, choices=[("V", "Défi validé :D"), ("R", "Défi rejeté :/"), ("P", "Défi en cours de validation ;)"), ("N", "Défi pas encore lu")], default="N")
    content = models.TextField("Le Défi", blank=False, max_length=200)
    url_proof = models.URLField("Url vers la preuve", blank=True)
    type_proof = models.CharField("Type de la preuve", max_length=60, blank=True)


    def __unicode__(self):
        return self.first_name + self.content
