from django.conf.urls import url
from django.conf.urls import patterns
from django.conf.urls import include
from views import auth_user
from views import auth_add_user
urlpatterns = patterns("",
	url(r"login",auth_user),
	url(r"add_user",auth_add_user),
)
