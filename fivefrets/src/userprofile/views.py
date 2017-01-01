from django.views.generic import ListView
from django.contrib.auth.models import User
from songs.models import Song
from songs.mixin import SongPaginationMixin


class ProfileHomeView(SongPaginationMixin, ListView):
    template_name = "userprofile/userprofile_home.html"

    def get_queryset(self):
        return Song.get_success().filter(created_by=self.request.user).order_by('-id')
