from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^room/(?P<pk>\d+)/$', views.room_detail, name='room_detail'),
    url(r'^scheme$', views.scheme, name='scheme'),
    url(r'^about$', views.about, name='about'),
    url(r'^add_room$', views.add_room, name='add_room'),
    url(r'^bron/(?P<pk>\d+)/$', views.bron, name='bron'),

]
