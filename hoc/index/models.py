#!/usr/bin/env python
# coding: utf-8

from django.db import models

['first_name', 'last_name', 'nombre', 'salle']


class CrepeCommande(models.Model):
    first_name = models.CharField("Prénom", max_length=30, blank=False)
    last_name = models.CharField("Nom", max_length=30, blank=False)
    nombre = models.CharField("Nombre de crêpes", max_length=30, blank=False)
    salle = models.CharField("Votre lieu de livraison", max_length=30, blank=False)

    def __unicode__(self):
        return self.first_name + self.last_name + self.nombre

class Challenge(models.Model):
    first_name = models.CharField("Prénom", max_length=30, blank=True)
    last_name = models.CharField("Nom", max_length=30, blank=True)
    type = models.CharField(max_length=1, choices=[("V", "Défi validé :D"), ("R", "Défi rejeté :/"), ("P", "Défi en cours de validation ;)"), ("N", "Défi pas encore lu")], default="N")
    content = models.TextField("Le Défi", blank=False)

    def __unicode__(self):
        return self.first_name + self.content
