# Create your views here.
from django.template import loader,Context
from django.http import HttpResponse
from django.template.base import Template
def homepage(resquest):
	t = loader.get_template("home.html")
	c = Context()
	return HttpResponse(t.render(c))
