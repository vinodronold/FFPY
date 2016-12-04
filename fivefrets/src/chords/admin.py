from django.contrib import admin
from django.forms import TextInput
from django.db import models
from .models import Chord, GuitarChord


class GuitarChordInline(admin.TabularInline):
    model = GuitarChord
    formfield_overrides = {
        models.CharField: {
            'widget': TextInput(attrs={'size': '4'})
        }
    }


class ChordAdmin(admin.ModelAdmin):
    inlines = [
        GuitarChordInline,
    ]

admin.site.register(Chord, ChordAdmin)
