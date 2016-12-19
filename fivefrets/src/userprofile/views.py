from django.views.generic import ListView
from django.contrib.auth.models import User
from songs.models import Song


class ProfileHomeView(ListView):
    template_name = "userprofile/userprofile_home.html"
    queryset = Song.get_success().order_by('-id')[:20]
