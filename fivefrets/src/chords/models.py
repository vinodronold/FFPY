from django.db import models

class Chord(models.Model):
    CHORD_CHOICE = (
        ('1', 'A'),
        ('2', 'A#'),
        ('3', 'B'),
        ('4', 'C'),
        ('5', 'C#'),
        ('6', 'D'),
        ('7', 'D#'),
        ('8', 'E'),
        ('9', 'F'),
        ('10', 'F#'),
        ('11', 'G'),
        ('12', 'G#'),
        ('N', 'X')
    )
    CHORD_TYPE_CHOICE = (
        ('MAJ', 'Major'),
        ('MIN', 'Minor')
    )
    name = models.CharField(
        max_length=2,
        choices=CHORD_CHOICE
    )
    typ = models.CharField(
        max_length=5,
        choices=CHORD_TYPE_CHOICE
    )
    alt_name =  models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.get_name_display() + '-' + self.typ

    def get_chord(self):
        if self.typ == "MIN":
            return self.get_name_display() + "m"
        return self.get_name_display()

    def get_primary_diagram(self):
        primary_chord = 0
        for primary_chord_param in GuitarChord.objects.filter(chord_id__exact = self.id, primary__exact = True):
            primary_chord = primary_chord_param.diagram()
            return primary_chord

class GuitarChord(models.Model):
    chord = models.ForeignKey(Chord, on_delete=models.CASCADE, default=0)
    primary = models.BooleanField(default=False)
    fret = models.CharField(max_length=2, default=0)
    barre = models.CharField(max_length=2, default=0)
    string6 = models.CharField(max_length=2, default=0)
    string5 = models.CharField(max_length=2, default=0)
    string4 = models.CharField(max_length=2, default=0)
    string3 = models.CharField(max_length=2, default=0)
    string2 = models.CharField(max_length=2, default=0)
    string1 = models.CharField(max_length=2, default=0)

    def __str__(self):
        return self.chord.get_chord()

    def diagram(self):
        return str(self.fret) + ',' + \
               str(self.barre) + ',' + \
               str(self.string6) + ',' + \
               str(self.string5) + ',' + \
               str(self.string4) + ',' + \
               str(self.string3) + ',' + \
               str(self.string2) + ',' + \
               str(self.string1)

class Album(models.Model):
    name = models.CharField(max_length=100)
    year = models.PositiveSmallIntegerField(blank=True)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Composer(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Singer(models.Model):
    name = models.CharField(max_length=100)

    class Meta:
        ordering = ['name']

    def __str__(self):
        return self.name

class Song(models.Model):
    album = models.ForeignKey(Album, blank=True, null=True)
    composer = models.ForeignKey(Composer, blank=True, null=True)
    singers = models.ManyToManyField(Singer, blank=True)
    name = models.CharField(max_length=100)
    youtube = models.CharField(max_length=100)
    lyric = models.TextField(blank=True)

    def __str__(self):
        return self.name

    def get_songchord_list(self):
        songchord_list = SongChord.objects.filter(song_id__exact = self.id)
        return songchord_list, songchord_list.exclude(chord_id__exact = 25).order_by('chord_id').distinct('chord_id')

    def get_song_info(self):
        info = ''
        if self.album:
            info = '%s | ' % (self.album)
        if self.composer:
            info = '%s%s | ' % (info, self.composer)
        info = info + ' | '.join(singer.name for singer in self.singers.all())

        #info = "%s | %s" % (
        #    self.composer,
        #    " | ".join(singer.name for singer in self.singers.all())
        #)
        return info

class SongChord(models.Model):
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    chord = models.ForeignKey(Chord)
    modified_chord = models.ForeignKey(Chord, related_name = 'modified_chord', blank=True, null=True)
    beat_position = models.FloatField(default = -1)
    start_time = models.FloatField(default = -1)

    class Meta:
        ordering = ['id']

    def __str__(self):
        return self.chord.get_chord()

    def chord_diagram(self):
        return self.chord.get_primary_diagram()
