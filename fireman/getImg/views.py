from django.template import loader
from django.template import Context
from django.shortcuts import render_to_response
from django.http import HttpResponse
from models import ImageSrc
from home.views import homepage
from auth.views import auth_user
from auth.models import UserDefine
from auth.models import UserImg
from auth.models import UserCookie
import os
from algorithm.search import algor_search_img
# Create your views here.
def get_img(request):
    g = request.GET
    if not g:
        return homepage(request)
    else:
        img_list = search_img(g['search'])
        return load_img(img_list)

def search_img(search_info):
    if not search_info:
        return []
    obj_list = ImageSrc.objects.all()
    img_level_list = algor_search_img(search_info,obj_list,'img_name')
    return img_level_list

def show_static_img(request):
    pass

def load_img(img_level_list):
    error=''
    if not img_level_list:
        error = 'no such image!'
    t = loader.get_template('list_img.html')
    img_list= list()
    for level,img in img_level_list:
        img_list.append(img)
        img.img_local =  os.path.join(r'/static'+img.img_local.split('static')[-1])
    return HttpResponse(t.render(Context({'img_list':img_list,'error':error})))

def get_self_img(request):
# how to get user name ? maybe cookie can do this?
# table cookie should have key from user_id and imgsrc should hav key from user_id!
    c = request.COOKIES
    if not c:
        return auth_user(request,'please login first!')
    if 'fireman' not in c:
        return auth_user(request,'please login firest!')
    id = UserCookie.objects.get(cookie_id=c['fireman']).cookie_user
    img_list = UserImg.objects.filter(user_id=id)
    for li in img_list:
        img_list = li.user	
    return load_img(img_list)
