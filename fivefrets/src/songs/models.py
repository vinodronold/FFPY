from django.conf import settings
from django.db import models
from chords.models import Chord


class Album(models.Model):
    name = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name)


class Composer(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name)


class Singer(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return str(self.name)


class Song(models.Model):
    PROCESS_STATUS_VALUES = (
        (0, 'SUCCESS'),
        (1, 'NOT STARTED'),
        (2, 'PROCESSING'),
        (3, 'MORE THAN SETUP DURATION'),
        (4, 'YOUTUBE ID DOWNLOAD ERROR'),
        (5, 'BEAT PROCESS ERROR'),
        (6, 'Invalid Youtube ID'),
    )
    youtube = models.SlugField(max_length=100)
    name = models.CharField(max_length=100, default='PROCESSING . . .')
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, null=True, blank=True)
    bpm = models.DecimalField(
        max_digits=6, decimal_places=2, default=0)
    process_status = models.PositiveSmallIntegerField(
        default=1, choices=PROCESS_STATUS_VALUES)
    lyric = models.TextField(blank=True)
    album = models.ForeignKey(Album, blank=True, null=True)
    composer = models.ForeignKey(Composer, blank=True, null=True)
    singers = models.ManyToManyField(Singer, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.name)

    def get_success():
        return Song.objects.filter(process_status__exact=0)

    def get_songchord_list(self):
        return SongChord.objects.filter(song_id__exact=self.id)

    def get_song_chords(self):
        return SongChord.objects.filter(song_id__exact=self.id).exclude(chord_id__exact=25).order_by('chord_id').distinct('chord_id')

    def get_song_meta(self):
        info = ''
        if self.album:
            info = '%s | ' % (self.album)
        if self.composer:
            info = '%s%s | ' % (info, self.composer)
            info = info + \
                ' | '.join(singer.name for singer in self.singers.all())
        return info


class SongChord(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    chord = models.ForeignKey(Chord)
    modified_chord = models.ForeignKey(
        Chord, related_name='modified_chord', blank=True, null=True)
    beat_position = models.FloatField(default=-1)
    start_time = models.FloatField(default=-1)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return str(self.chord)

    def guitar(self):
        return self.chord.primary_guitar()
