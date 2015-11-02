# Create your views here.
from django.http import HttpResponse
from django.template import Template
from django.template import loader
from django.template import Context
from django.template import RequestContext
from django import forms
from django.forms import ModelForm
from tools import ImgInfo
from auth.views import get_user_name
from auth.views import get_user_img
from auth.views import auth_user
from auth.models import UserImg
from auth.models import UserDefine
from getImg.models import ImageSrc
from getImg.models import ImageType
from models import Img_form
import os as _os
import mimetypes
TRUNC_SIZE = 4096
USER_UPLOAD = _os.path.abspath(_os.path.join(__file__,'../static/'))

import sys
import os as _os
def saveImg(f,user_name):
    # save img to local and db
    mimetype,encoding = mimetypes.guess_type(f.name)
    local = None
    if mimetype.startswith('image') and f.size<TRUNC_SIZE*1000:
        path = _os.path.join(USER_UPLOAD,user_name)    
        if not _os.path.isdir(path):
            _os.mkdir(path)
        file_src = f.read(TRUNC_SIZE)
        file_name = _os.path.join(path,f.name)
        new_f = open(file_name,'wb+') 
        try:
            with open(file_name,'wb+') as new_f:
                while file_src:
                    new_f.write(file_src)
                    file_src = f.read(TRUNC_SIZE)
         #save db
            info = ImgInfo.AnalyImg(file_name)
            if not info:
                _os.remove(file_name)
                error='please give a image file!'
                return error,local
            #img_tp = ImageType.objects.get(id=3)
            #img = ImageSrc()
            #img.img_name = f.name
            #img.img_local = file_name
            #img.img_type = img_tp
            #img.img_weight = info['weight']
            #img.img_height = info['height']
            #img.save()
            user_img = UserImg()
            user_img.user = UserDefine.objects.get(user_name=user_name)
            user_img.user_img = file_name
            user_img.user_loveleve = 0
            user_img.save()
            error = 'upload succeed!'
            local = _os.path.join('/static/',user_name,f.name)
        except Exception as e:
            error = 'save to db is failed!'
            _os.remove(file_name)
            raise e
    else:
        error = 'please give a image and not so big!'
    return error,local
 


def user_option(request):
    t = loader.get_template("user_option.html")
    p = request.POST
    error = ''
    uf = Img_form()
    user_img = get_user_img(request.COOKIES)
    for img in user_img:
        img.user_img = '/static/'+img.user_img.split('/static/')[1]
    if request.method =="POST":
    	if 'files' in request.FILES:
             f = request.FILES['files']
             user_name = get_user_name(request.COOKIES)
             if not user_name:
                 return auth_user(request,info='please login first!')
             error,local = saveImg(f,user_name)
        else:
            error = 'please give a file!'
            local = None
        return HttpResponse(t.render(RequestContext(request,{'uf':uf,'error':error,'local':local,'user_img':user_img})))
    else:
        return HttpResponse(t.render(RequestContext(request,{'uf':uf,'error':'upload image!','user_img':user_img})))

    
