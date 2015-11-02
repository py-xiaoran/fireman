from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()
urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'fireman.views.home', name='home'),
    # url(r'^fireman/', include('fireman.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    url(r'^$',include('home.urls')),
    url(r'^auth/',include('auth.urls')),
    url(r'^getImg/',include('getImg.urls')),
    url(r'^users/',include('users.urls')),
)
