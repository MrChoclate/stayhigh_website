from django.conf.urls import patterns, include, url
from django.contrib import admin

from django.views.generic import TemplateView

from index.views import *


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'hoc.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),

    url(r'^$', TemplateView.as_view(template_name="index.html"), name='index'),

    url(r'^crepes_admin$', 'index.views.crepes_admin', name='crepes_admin'),

    url(r'^captcha/', include('captcha.urls')),


    url(r'^crepes$', CrepeCommande.as_view(template_name="crepes.html"), name='crepes'),
    url(r'^thanks/crepes$', 'index.views.thanks_crepes', name='thanks_crepes'),


    url(r'^poles$', TemplateView.as_view(template_name="poles.html"), name='poles'),

    url(r'^voyages$', TemplateView.as_view(template_name="voyages.html"), name='voyages'),


    #url(r'^challenges/$', ChallengesList.as_view(template_name="challenges.html"), name='challenges'),
    url(r'^challenges/$', ChallengesList2, name='challenges'),

    url(r'^challenge/$', ChallengeCreate.as_view(template_name="challenges_new.html"), name='challenge'),

    url(r'^thanks/$', 'index.views.thanks', name='thanks'),

)
