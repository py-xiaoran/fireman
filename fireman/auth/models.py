from django.db import models

# Create your models here.
class UserDefine(models.Model):
	user_id = models.IntegerField(primary_key=True,auto_created=True)
	user_name = models.CharField(max_length=30,unique=True)
	user_password = models.TextField(max_length=12)
	user_email = models.EmailField()
	def __unicode__(self):
		dit ={'id':self.user_id,'name':self.user_name,'password':self.user_password,'email':self.user_email}
		return u"id:%(id),name%(name),passwd%(password),email%(email)"%dit

class UserImg(models.Model):
#	user_id = models.IntegerField()
	user = models.ForeignKey(UserDefine)
	user_img = models.TextField(max_length=100)
	user_loveleve = models.IntegerField()
	def __unicode__(self):
		dit={'id':self.user_id,'img':self.user_img,'leve':self.user_loveleve}
		return u"id:%(id),img:%(img),loveleve:%(leve)"%dit

class UserCookie(models.Model):
	cookie_id = models.CharField(max_length=150,unique=True)
	cookie_time = models.TimeField()
	cookie_domain = models.CharField(max_length=50)
	cookie_user_name = models.CharField(max_length=30)
	cookie_user  = models.ForeignKey(UserDefine)

	
