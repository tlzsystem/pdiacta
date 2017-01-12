from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^region/$', views.getregiones),
    url(r'^provincia/(?P<id>[0-9]+)/$', views.getprovincia),
    url(r'^comuna/(?P<id>[0-9]+)/$', views.getcomuna),
    #url(r'^(?P<id>[0-9]+)/$', views.byclientes, name="byid"),
    #url(r'^add/$', views.addcliente, name="nuevocliente"),

]