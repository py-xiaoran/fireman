from django.db import models
from django import forms
# Create your models here.
class Img_form(forms.Form):
    files = forms.FileField()
