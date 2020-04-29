from django.contrib import admin
from django.urls import path, include
from django.conf.urls import url
from .views import home, details, post_item

urlpatterns = [
    path('', home, name='items_home'),
    url(r'^([0-9]+)/$', details, name='items_details'),
    url(r'^post_url/$', post_item, name='items_post'),
]
