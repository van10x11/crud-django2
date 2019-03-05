from django.shortcuts import render,redirect
from django.contrib import auth,messages




def user_login(request):
	if request.user.is_authenticated and request.user.groups.filter(name='administrator').exists:
		return redirect('dashboard:index')

	if request.method == "POST":
		username = request.POST.get('username')
		password = request.POST.get('password')

		user = auth.authenticate(username=username,password=password)

		if user is not None:
			auth.login(request,user)
			return redirect('dashboard:index')
		else:
			messages.error(request,'username or password incorrect')

	return render(request,'login.html')


def user_logout(request,username_login):
	
	if request.user.is_authenticated and request.user.groups.filter(name='administrator'):
		username = request.user.username
		if username == username_login :
			auth.logout(request)
			return redirect('login')
		else:
			return redirect('dashboard:index')
	else:
		return redirect('dashboard:index')
	