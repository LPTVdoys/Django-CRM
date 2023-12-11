from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages



def home(request):
	# проверка на вход в систему
	if request.method == 'POST':
		username = request.POST['username']
		password = request.POST['password']
		# Авторизация
		user = authenticate(request, username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, "Succesful login")
			return redirect('home')
		else:
			messages.success(request, "somethink wrong, check your login and password...")
			return redirect('home')
	else:
		return render(request, 'home.html', {})


def logout_user(request):
	logout(request)
	messages.success(request, "You have been logout")
	return redirect('home')

def register_user(request):
	return render(request, 'register.html', {})