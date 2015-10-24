# Create your views here.
from django.template import Template
from django.template import loader
from django.template import Context
from django.template import RequestContext
from django.http import HttpResponse
from models import UserDefine
import uuid
from datetime import datetime
from datetime import timedelta
from auth.models import UserCookie
def auth_user(request,info=''):
	if not hasattr(request,'GET'):
		return login_fail(error_info='please enter name and password!')
	g = request.GET
	if g.has_key('user_name'):
		if not g.has_key('user_password'):
			return login_fail(error_info='plase enter password')
		return check_user(g['user_name'],g['user_password'])
	else:
		return login_fail(error_info=info)
def auth_add_user(request):
	if not hasattr(request,'POST'):
		return add_user_fail(request)
	g = request.POST
	if not g.has_key('user_name'):
		return add_user_fail(request,'please enter UserName!')
	if not g.has_key('user_password'):
		return add_user_fail(request,'please enter password!')
	if not g.has_key('user_password2'):
		return add_user_faile(request,'please repeat password!')
	if not g.has_key('user_email'):
		return add_user_fail(request,'please enter email!')
	else:
		return check_add_user(request,g['user_name'],g['user_password'],g['user_password2'],g['user_email'])
def check_add_user(request,name,password,password2,email):
	if not name or not password or not email:
		return add_user_fail(request,'please enter all infomation!')
	if password != password2:
		return add_user_fail(request,'password is not same!')
	user_name_list = UserDefine.objects.filter(user_name=name)
	if  user_name_list:
		return add_user_fail(request,'username is exist!')
	else:
		us = UserDefine()
		us.user_name = name
		us.user_password = password
		us.user_email = email
		try:
			us.save()
		except Exception as e:
			return add_user_fail(request,'create account is fail!')
		return add_user_succeed()
def add_user_fail(request,error=""):
	t = loader.get_template('add_user.html')
	return HttpResponse(t.render(RequestContext(request,{'error':error})))
def add_user_succeed():
	t = loader.get_template('add_user_succeed.html')
	return HttpResponse(t.render(Context()))

def login_fail(error_info=''):
	t = loader.get_template('login.html')
	return HttpResponse(t.render(Context({'error':error_info})))
def login_succeed(name):
	t = loader.get_template('login_succeed.html')
	response =  HttpResponse(t.render(Context()))
	key_v = 'fireman'
	id_v = str(uuid.uuid1()).decode()
	domain_v = '123.57.85.72:8000'
	expires_v = datetime.now()+timedelta(0,60*60,0)
	value_v = {'id':id_v,'domain':domain_v}
	try:								# table usercookie is almost not change ,only change cookie id
		ck = UserCookie.objects.filter(cookie_user_name =name)
		if len(ck)>1:
			for k in ck[1:]:
				k.delete()
			ck = ck[0]
		if not ck:
			ck=UserCookie()
		ck.cookie_id = id_v
		ck.cookie_time = expires_v
		ck.cookie_domain = domain_v
		ck.cookie_user_name = name
		ck.save()
	except Exception as e:
		return login_fail('save cookie error')
	#response.cookies={'id':value_v,'expires':expires_v,'domain':domain_v}
	response.set_cookie(key=key_v,value=id_v)#,max_age=60*60,domain=domain_v)
	return response
def check_user(name,password):
	if not name or not password:
		return login_fail(error_info='please enter you name and password!')
	name_res = UserDefine.objects.filter(user_name=str(name))
	if len(name_res)!=1:
		return login_fail('you account is not exist!')
	if name_res[0].user_password == password:
		return login_succeed(name)
	else:
		return login_fail(error_info='you password is not correct!')
