from django.conf.urls import url, include
from . import views

urlpatterns = [
    url(r'^a/$', views.PayApiView.as_view()),
    url(r'^f/$', views.index),
]

