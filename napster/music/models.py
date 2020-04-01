"""Music app models"""

import os

from django.db import models


def image_filepath(instance, filename):
    """Returns a filename for music instance"""
    if instance.__class__.__name__ == 'Artist':
        path = 'artists/images'
    elif instance.__class__.__name__ == 'Song':
        path = 'songs'
    elif instance.__class__.__name__ == 'Album':
        path = 'albums'

    return os.path.join(
        path, f'{instance.name}{instance.extension()}'
        # path, f'{instance.id}_{instance.name}{instance.extension()}'
    )


class MusicModel(models.Model):
    """Abstract model to create concrete music models"""
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to=image_filepath)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def extension(self):
        _, ext = os.path.splitext(self.image.name)
        return ext


class Artist(MusicModel):
    """Artist model with an image"""
    pass


class Album(MusicModel):
    """Album model with a image and an artist"""
    artist = models.ForeignKey(to=Artist, on_delete=models.CASCADE)


class Song(MusicModel):
    """Song model with a album and a image"""
    album = models.ForeignKey(to=Album, on_delete=models.CASCADE)
