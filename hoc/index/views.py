#!/usr/bin/env python
# coding: utf-8

from django.shortcuts import render, redirect

from django.template import RequestContext

from index.models import *

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

from django.core.urlresolvers import reverse_lazy, reverse

from django.contrib import messages







class ChallengeCreate(CreateView):
    model = Challenge
    fields = ['first_name', 'last_name', 'content',]
    success_url = '/thanks/'


class ChallengesList(ListView):
    model = Challenge
    context_object_name = 'challenges'
    fields = ['first_name', 'last_name', 'content',]


def thanks(request):
    messages.add_message(request, messages.INFO, 'Merci pour votre défi')
    return redirect('challenges')
