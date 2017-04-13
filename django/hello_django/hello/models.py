from django.db import models

# Create your models here.
class User(models.Model):
	name=models.CharField(max_length=30,verbose_name="姓名",primary_key=True)
	password=models.CharField(max_length=50,verbose_name="密码")
	
	
