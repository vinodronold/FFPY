from django.contrib import admin
from django.forms import TextInput
from django.db import models
from .models import Chord, GuitarChord, Album, Composer, Singer, Song, SongChord

class GuitarChordInline(admin.TabularInline):
    model = GuitarChord
    formfield_overrides = {
        models.CharField: {
            'widget': TextInput(attrs={'size':'4'})},
    }

class ChordAdmin(admin.ModelAdmin):
    inlines = [
        GuitarChordInline,
    ]

class SongChordInline(admin.TabularInline):
    model = SongChord

class SongAdmin(admin.ModelAdmin):
    inlines = [
        SongChordInline,
    ]

admin.site.register(Chord, ChordAdmin)
admin.site.register(Album)
admin.site.register(Composer)
admin.site.register(Singer)
admin.site.register(Song, SongAdmin)
