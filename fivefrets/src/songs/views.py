from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.views.generic import DetailView, ListView, RedirectView

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
        return Song.objects.filter(name__istartswith=self.kwargs['StartWith']).order_by('-id')


class SongPlayerView(DetailView):
    slug_field = 'youtube'
    template_name = "songs/songs_player.html"
    model = Song

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            self.object = Song(
                youtube=kwargs[super(SongPlayerView, self).slug_url_kwarg]
            )
            print(kwargs[super(SongPlayerView, self).slug_url_kwarg])
            self.object.save()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_context_data(self, **kwargs):
        context = super(SongPlayerView, self).get_context_data(**kwargs)
        context['song_meta'] = self.get_object().get_song_meta()
        context['songchord_list'] = self.get_object().get_songchord_list()
        context['chords'] = self.get_object().get_song_chords()
        return context
