#!/usr/bin/env python
# coding: utf-8

from django.shortcuts import render, redirect, render_to_response

from django.template import RequestContext

from index.models import *

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

from django.core.urlresolvers import reverse_lazy, reverse

from django.contrib import messages

from django.contrib.auth.decorators import login_required






class ChallengeCreate(CreateView):
    model = Challenge
    fields = ['first_name', 'last_name', 'content',]
    success_url = '/thanks/'

class CrepeCommande(CreateView):
    model = CrepeCommande
    fields = ['first_name', 'last_name', 'nombre', 'salle']
    success_url = '/thanks/crepes'



@login_required
def crepes_admin(request):

    return render_to_response(
        "crepes_admin.html",
        {
            'request': request,
        },
        context_instance=RequestContext(request))


def ChallengesList2(request):
    challenges_v = Challenge.objects.filter( type='V')
    challenges_r = Challenge.objects.filter( type='R')
    challenges_p = Challenge.objects.filter( type='P')
    challenges_n = Challenge.objects.filter( type='N')

    return render_to_response(
        "challenges.html",
        {
            'request': request,
            'challenges_v' : challenges_v,
            'challenges_r' : challenges_r,
            'challenges_p' : challenges_p,
            'challenges_n' : challenges_n,
        },
        context_instance=RequestContext(request))


def thanks(request):
    messages.add_message(request, messages.INFO, 'Merci pour votre défi')
    return redirect('challenges')


def thanks_crepes(request):
    messages.add_message(request, messages.INFO, 'Votre commande a bien été prise en compte')
    return redirect('index')
