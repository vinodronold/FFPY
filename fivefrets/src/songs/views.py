from django.core.urlresolvers import reverse_lazy
from django.core.paginator import InvalidPage
from django.http import Http404
from django.shortcuts import redirect
from django.views.generic import DetailView, ListView, RedirectView, UpdateView
from celery import chain, group
from chords.tasks import download, extract, convert_to_chords, delete_all_files
from .models import Song
from .forms import SongForm
from .mixin import GetSongContextMixin, SongPaginationMixin


class SongHomeView(ListView):
    template_name = "songs/songs_home.html"
    queryset = Song.get_success().order_by('-id')[:12]


class SongHomeRedirectView(RedirectView):
    url = reverse_lazy('song-home')


class SongListAllView(SongPaginationMixin, ListView):
    template_name = "songs/songs_list_all.html"
    queryset = Song.get_success().order_by('-id')


class SongBrowseView(SongPaginationMixin, ListView):
    template_name = "songs/songs_list_all.html"

    def get_queryset(self):
        return Song.get_success().filter(name__istartswith=self.kwargs['StartWith']).order_by('-id')


class SongUpdateView(UpdateView):
    template_name = "songs/song_update.html"
    model = Song
    slug_field = 'youtube'
    form_class = SongForm

    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            return super(SongUpdateView, self).get(request, *args, **kwargs)
        else:
            return redirect('/accounts/login/?next=%s' % request.path)


class SongPlayerView(GetSongContextMixin, DetailView):
    model = Song
    template_name = "songs/songs_player_view.html"

    def create_song(self, ytid, create_user):
        self.object = Song(
            youtube=ytid,
            created_by=create_user)
        self.object.save()
        res = chain(download.s(ytid), extract.s(),
                    convert_to_chords.s(), delete_all_files.s())()
        return self.object

    def get(self, request, *args, **kwargs):
        try:
            self.object = self.get_object()
        except Http404:
            if request.user.is_authenticated():
                self.object = self.create_song(
                    kwargs[super(SongPlayerView, self).slug_url_kwarg], request.user)
            else:
                return redirect('/accounts/login/?next=%s' % request.path)

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
