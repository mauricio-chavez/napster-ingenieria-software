"""Music app views"""

from django.views.generic import TemplateView

from django.shortcuts import render


class IndexView(TemplateView):
    template_name = 'music/index.html'


class TopSongsView(TemplateView):
    template_name = 'music/top-songs.html'
