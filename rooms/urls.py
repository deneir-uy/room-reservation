from django.conf.urls import url
from rest_framework.urlpatterns import format_suffix_patterns
from rooms import views


app_name = 'rooms'


urlpatterns = [
    # /rooms/
    url(r'^$', views.RoomList.as_view({'get': 'room'}), name='index'),

    # /rooms/<room_id>/
    url(r'^(?P<pk>[0-9]+)/$', views.RoomDetail.as_view({'get': 'room'}), name='detail'),

    # /rooms/<room_id>/reserve/
    url(r'^(?P<pk>[0-9]+)/reserve/$', views.ReservationCreate.as_view({'post': 'create'}), name='reserve'),
]


urlpatterns = format_suffix_patterns(urlpatterns)
