from django.conf.urls import url
from . import views

urlpatterns = [
    # /rooms
    url(r'^$', views.index, name='index'),

    # /rooms/id
    url(r'^(?P<room_id>[0-9]+)/$', views.detail, name='detail'),
]
