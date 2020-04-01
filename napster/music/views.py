"""Music app views"""

from django.shortcuts import render
from django.views.generic import TemplateView, ListView

from .models import Song


class IndexView(TemplateView):
    template_name = 'music/index.html'


class TopSongsView(ListView):
    model = Song
    template_name = 'music/top-songs.html'
