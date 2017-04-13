from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from hello.models import *
def login(request):
	if request.method=="GET":
		return render(request,"login.html")
		
	else:
		user1=request.POST.get('uname')
		user2=request.POST.get('pwd')
		print(user1)
		print(user2)
		User.objects.create(name=user1,password=user2,)
		return HttpResponse('ok')

