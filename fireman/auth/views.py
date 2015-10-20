# Create your views here.
from django.template import Template
from django.template import loader
from django.template import Context
from django.http import HttpResponse
from models import User

def auth_user(request):
	if not hasattr(request,'GET'):
		return login_fail()
	g = request.GET
	if g.has_key('user_name'):
		if not g.has_key('user_password'):
			return login_fail()
		return check_user(g['user_name'],g['user_password'])
	else:
		return login_fail()
def auth_add_user(request):
	if not hasattr(request,'GET'):
		return add_user_fail()
	g = request.GET
	if not g.has_key('user_name'):
		return add_user_fail()
	if not g.has_key('user_password'):
		return add_user_fail()
	if not g.has_key('user_password2'):
		return add_user_fail()
	if not g.has_key('user_email'):
		return add_user_fail()
	else:
		return check_add_user(g['user_name'],g['user_password'],g['user_email'])
def check_add_user(name,password,email):
	if not name or not password or not email:
		return add_user_fail()
	user_name_list = user.objects.filter(name='name')
	if not user_name_list:
		return add_user_succeed()
	else:
		us = user()
		us.user_name = name
		us.user_password = password
		us.user_email = email
		return add_user_fail()
def add_user_fail():
	t = loader.get_template('add_user.html')
	return HttpResponse(t.render(Context()))
def add_user_succeed():
	t = Template.get_template('add_user_succeed.html')
	return HttpResponse(t.render(Context()))

def login_fail():
	t = loader.get_template('login.html')
	return HttpResponse(t.render(Context()))
def login_succeed():
	t = Template.get_template('login_succeed.html')
	return HttpResponse(t.render(Context()))

def check_user(name,password):
	if not name or not password:
		return login_fail()
	name_res = User.objects.filter(user_name=str(name))
	if name_res.User_passworld == password:
		return login_succeed()
