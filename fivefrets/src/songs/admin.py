from django.contrib import admin
from .models import Album, Composer, Singer, Song, SongChord


class SongChordInline(admin.TabularInline):
    model = SongChord


class SongAdmin(admin.ModelAdmin):
    inlines = [
        SongChordInline,
    ]

    # def save_model(self, request, obj, form, change):
    #     if not change:
    #         obj.created_by = request.user
    #         obj.save()


admin.site.register(Album)
admin.site.register(Composer)
admin.site.register(Singer)
admin.site.register(Song, SongAdmin)
