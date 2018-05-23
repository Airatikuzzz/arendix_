from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^room/(?P<pk>\d+)/$', views.room_detail, name='room_detail'),
    url(r'^scheme$', views.scheme, name='scheme'),
    url(r'^about$', views.about, name='about'),

]
