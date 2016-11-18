from django.conf.urls import url 
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^register$', views.register),
    url(r'^dashboard$', views.dashboard),
    url(r'^login$', views.login),
    url(r'^logout_dashboard$', views.logout_dashboard),
    url(r'^add_item$', views.add_item),
    url(r'^submit_add_item$', views.submit_add_item),
]