from django.template import loader
from django.template import Context
from django.https import HttpResponse
from models import Imgsrc
from home import homepage
# Create your views here.
def get_img(request):
    if getattr(request,'GET'):
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
    return HttpResponse(t.render(Context({'img_list':img_list,'error':error}))
