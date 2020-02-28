"""Music app views"""

from django.shortcuts import render


def index(request):
    """Welcomes the user"""
    return render(request, 'music/index.html')


def top_songs(request):
    """Shows trending songs"""
    return render(request, 'music/top-songs.html')
