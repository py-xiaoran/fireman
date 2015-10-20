from django.conf.urls import url
from django.conf.urls import patterns
from django.conf.urls import include
from views import auth_user
from views import auth_add_user
urlpatterns = patterns("",
	url("login",auth_user),
	url("add_user",auth_add_user),
)
