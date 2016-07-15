from django.conf.urls import include, url
from . import views

urlpatterns = [
        url(r'^login/', views.log_in),
        url(r'^logout/', views.log_out),
    ]