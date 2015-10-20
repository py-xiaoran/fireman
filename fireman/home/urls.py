from django.conf.urls import patterns, include, url
from views import homepage
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fireman.views.home', name='home'),
    # url(r'^fireman/', include('fireman.foo.urls')),
    url(r'^$', homepage),
    #url(r'^auth/',include('auth.urls'))
)
