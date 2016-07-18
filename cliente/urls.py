from django.conf.urls import include, url
from . import views


urlpatterns = [
        url(r'^', views.clientes),
        url(r'^/([0-9]+)/$', views.byclientes),
       
    ]