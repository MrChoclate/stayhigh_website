from django.shortcuts import render
from index.models import *

from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView

from django.core.urlresolvers import reverse_lazy

class ChallengeCreate(CreateView):
    model = Challenge
    fields = ['first_name', 'last_name', 'mail', 'content']


class ChallengesList(ListView):
    model = Challenge
    context_object_name = 'challenges'
