from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^display/(?P<yt_id>\w+(-\w+)?)$', views.display, name='display'),
    ]
