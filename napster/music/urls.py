"""Music app URL configuration"""

from django.urls import path

from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('top_songs', views.TopSongsView.as_view(), name='top_songs'),
]
