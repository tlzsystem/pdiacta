from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.compradores),
    url(r'^(?P<id>[0-9]+)/$', views.byid, name="byid"),

]