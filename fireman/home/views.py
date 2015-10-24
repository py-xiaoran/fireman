# Create your views here.
from django.template import loader,Context
from django.http import HttpResponse
from django.template.base import Template
from auth.models import UserCookie
def homepage(request):
	t = loader.get_template("home.html")
	cookie = request.COOKIES
	info = {}
	if 'fireman' in cookie:
		id =cookie['fireman']
		if id:
			name = UserCookie.objects.get(cookie_id=id).cookie_user_name
		info = {'user_name':name}
	c = Context(info)
	return HttpResponse(t.render(c))
