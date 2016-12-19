from django.core.urlresolvers import reverse_lazy
from django.http import Http404
from django.views.generic import DetailView, ListView, RedirectView
from celery import chain, group
from chords.tasks import download, extract, convert_to_chords, delete_all_files
from .models import Song
from .mixin import GetSongContextMixin


class SongHomeView(ListView):
    template_name = "songs/songs_home.html"
    queryset = Song.get_success().order_by('-id')[:12]


class SongHomeRedirectView(RedirectView):
    url = reverse_lazy('song-home')


class SongListAllView(ListView):
    template_name = "songs/songs_list_all.html"
    queryset = Song.get_success().order_by('-id')


class SongBrowseView(ListView):
    template_name = "songs/songs_list_all.html"

    def get_queryset(self):
        return Song.objects.filter(name__istartswith=self.kwargs['StartWith']).order_by('-id')


class SongPlayerView(GetSongContextMixin, DetailView):
    model = Song
    template_name = "songs/songs_player_view.html"

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            self.object = Song(
                youtube=kwargs[super(SongPlayerView, self).slug_url_kwarg],
                created_by=request.user
            )
            self.object.save()
            res = chain(download.s(kwargs[super(SongPlayerView, self).slug_url_kwarg]), extract.s(),
                        convert_to_chords.s(), delete_all_files.s())()

        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)


class SongPlayerAjaxView(GetSongContextMixin, DetailView):
    model = Song
    template_name = "songs/songs_player_ajax.html"

    def get(self, request, *args, **kwargs):
        if not request.is_ajax():
            raise Http404("Oops not a correct call")

        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)
