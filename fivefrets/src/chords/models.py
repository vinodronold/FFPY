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
    alt_name = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.get_name_display() + 'm' if self.typ == 'MIN' else self.get_name_display()

    def primary_guitar(self):
        for guitar_diagram in GuitarChord.objects.filter(chord_id__exact=self.id, primary__exact=True):
            return guitar_diagram.diagram()


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
        return str(self.chord)

    def diagram(self):
        return str(self.fret) + ',' + \
            str(self.barre) + ',' + \
            str(self.string6) + ',' + \
            str(self.string5) + ',' + \
            str(self.string4) + ',' + \
            str(self.string3) + ',' + \
            str(self.string2) + ',' + \
            str(self.string1)
