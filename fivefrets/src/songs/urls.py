from django.conf.urls import url
from .views import SongHomeView, SongPlayerView, SongListAllView, SongBrowseView

urlpatterns = [
    url(r'^$', SongHomeView.as_view(), name="song-home"),
    url(r'^(?P<pk>\d+)/$', SongPlayerView.as_view(), name="song-detail"),
    url(r'^browse/$', SongListAllView.as_view(), name="song-browse"),
    url(r'^browse/(?P<StartWith>[a-zA-Z0-9-]+)/$',
        SongBrowseView.as_view(), name="song-browse"),
]
