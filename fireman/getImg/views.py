from django.template import loader
from django.template import Context
from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import ImageSrc
from home.views import homepage
from auth.models import UserDefine
from auth.models import UserImg
from auth.models import UserCookie
# Create your views here.
def get_img(request):
    g = request.GET
    if not g:
        return homepage(request)
    else:
        img_list = search_img(g.search)
        return load_img(img_list)

def search_img(search_info):
    if not search_info:
        return []
    img_list = Imgsrc.objects.filter(img_name='search_info')
    return img_list

def load_img(img_list):
    error=''
    if not img_list:
        error = 'no such image!'
    t = loader.get_template('list_img.html')
    return HttpResponse(t.render(Context({'img_list':img_list,'error':error})))

def get_self_img(request):
# how to get user name ? maybe cookie can do this?
# table cookie should have key from user_id and imgsrc should hav key from user_id!
	c = request.COOKIES
	if not c:
		return auth.auth_user(request,'please login first!')
	if 'fireman' not in c:
		return auth.auth_user(request,'please login firest!')
	id = UserCookie.objects.get(cookie_user_id=c['fireman']).cookie_user_id
	img_list = UserImg.objects.filter(user_id=id)
	return load_img(img_list)
