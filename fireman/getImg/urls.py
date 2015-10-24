from django.conf.urls import patterns, include, url
from views import get_img
from views import get_self_img
urlpatterns = patterns('',
    # Examples:
    url(r'^search/$',get_img),
    url(r'^get_self_img/$',get_self_img),
)
