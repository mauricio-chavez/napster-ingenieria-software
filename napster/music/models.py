"""Music app models"""

import os

from django.db import models


def music_model_filepath(instance, filename):
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
    name = models.CharField('Nombre', max_length=128)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name

    def extension(self):
        if self.__class__.__name__ == 'Song':
            _, ext = os.path.splitext(self.file.name)
        else:
            _, ext = os.path.splitext(self.image.name)
        return ext


class Artist(MusicModel):
    """Artist model with an image"""
    image = models.ImageField('Imagen', upload_to=music_model_filepath)

    class Meta:
        verbose_name = 'Artista'


class Album(MusicModel):
    """Album model with a image and an artist"""
    image = models.ImageField('Imagen', upload_to=music_model_filepath)
    artist = models.ForeignKey(
        verbose_name='Artista',
        to=Artist,
        on_delete=models.CASCADE
    )


class Song(MusicModel):
    """Song model with a album and a image"""
    file = models.FileField('Archivo', upload_to=music_model_filepath)
    album = models.ForeignKey(
        verbose_name='Álbum',
        to=Album,
        on_delete=models.CASCADE
    )

    class Meta:
        verbose_name = 'Canción'
        verbose_name_plural = 'Canciones'
