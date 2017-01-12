from django.conf.urls import include, url
from . import views


urlpatterns = [
        url(r'^$', views.clientes),
        url(r'^(?P<id>[0-9]+)/$', views.byclientes, name="byid"),
        url(r'^add/$', views.addcliente, name="nuevocliente"),
        url(r'^delete/(?P<id>[0-9]+)/$', views.deletebyid, name="deletebyid")
    ]