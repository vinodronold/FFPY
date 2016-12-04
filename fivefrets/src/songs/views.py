from django.core.urlresolvers import reverse_lazy
from django.views.generic import ListView, RedirectView, DetailView

from .models import Song


class SongHomeView(ListView):
    template_name = "songs/songs_home.html"
    queryset = Song.objects.all().order_by('-id')[:20]


class SongHomeRedirectView(RedirectView):
    url = reverse_lazy('song-home')


class SongListAllView(ListView):
    template_name = "songs/songs_list_all.html"
    queryset = Song.objects.all().order_by('-id')


class SongBrowseView(ListView):
    template_name = "songs/songs_list_all.html"

    def get_queryset(self):
        return Song.objects.filter(name__istartswith=lower(self.kwargs['StartWith'])).order_by('-id')


class SongPlayerView(DetailView):
    template_name = "songs/songs_player.html"
    model = Song

    def get_context_data(self, **kwargs):
        context = super(SongPlayerView, self).get_context_data(**kwargs)
        context['song_meta'] = self.get_object().get_song_meta()
        context['songchord_list'] = self.get_object().get_songchord_list()
        context['chords'] = self.get_object().get_song_chords()
        return context
