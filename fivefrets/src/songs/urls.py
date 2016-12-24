from django.conf.urls import url
from .views import SongHomeView, SongPlayerView, SongPlayerAjaxView, SongListAllView, SongBrowseView, SongUpdateView

urlpatterns = [
    url(r'^$', SongHomeView.as_view(), name="song-home"),
    url(r'^play/(?P<slug>[-\w]+)/$',
        SongPlayerView.as_view(), name="song-detail"),
    url(r'^edit/(?P<slug>[-\w]+)/$',
        SongUpdateView.as_view(), name="song-edit"),
    url(r'^ajax/(?P<slug>[-\w]+)/$',
        SongPlayerAjaxView.as_view(), name="song-player-ajax"),
    url(r'^browse/$', SongListAllView.as_view(), name="song-list-all"),
    url(r'^browse/(?P<StartWith>[a-zA-Z0-9-]+)/',
        SongBrowseView.as_view(), name="song-browse"),
]
