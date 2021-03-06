from django.shortcuts import render,HttpResponse, redirect,HttpResponseRedirect
from django.contrib.auth import logout, authenticate, login
from django.contrib.auth.hashers import make_password
from .models import CustomUser, Staffs, Students, AdminHOD
from django.contrib import messages

def home(request):
	return render(request, 'home.html')

def loginUser(request):
	return render(request, 'login.html')

def doLogin(request):
	email_id = request.GET.get('email')
	password = request.GET.get('password')
	if not (email_id and password):
		messages.error(request, "Please provide all the details!!")
		return render(request, 'login.html')
	user = CustomUser.objects.filter(email=email_id).last()
	if not user:
		messages.error(request, 'Invalid Login Credentials!!')
		return render(request, 'login.html')
	check_user = authenticate(request, username=user.username, password=password)
	if not check_user:
		messages.error(request, 'Invalid Login Credentials!!')
		return render(request, 'login.html')
	login(request, user)
	if user.user_type == CustomUser.HOD:
		return redirect('admin_home/')
	elif user.user_type == CustomUser.STAFF:
		return redirect('staff_home/')
	elif user.user_type == CustomUser.STUDENT:
		return redirect('student_home/')

	return render(request, 'home.html')

	
def registration(request):
	return render(request, 'registration.html')
	

def doRegistration(request):
	first_name = request.GET.get('first_name')
	last_name = request.GET.get('last_name')
	email_id = request.GET.get('email')
	password = request.GET.get('password')
	confirm_password = request.GET.get('confirmPassword')
	user_type = CustomUser.EMAIL_TO_USER_TYPE_MAP[request.GET.get('user_type')]

	hashed_password = make_password(password);

	if password == confirm_password:
		password = hashed_password
		confirm_password = hashed_password
	else:
		messages.error(request, 'Both passwords should match!!')
		return render(request, 'registration.html')
	if not (email_id and password and confirm_password):
		messages.error(request, 'Please provide all the details!!')
		return render(request, 'registration.html')

	is_user_exists = CustomUser.objects.filter(email=email_id).exists()

	if is_user_exists:
		messages.error(request, 'User with this email id already exists. Please proceed to login!!')
		return render(request, 'registration.html')

	if user_type is None:
		messages.error(request, "Please use valid format for the email id: '<username>.<staff|student|hod>@<college_domain>'")
		return render(request, 'registration.html')

	username = email_id.split('@')[0].split('.')[0]

	if CustomUser.objects.filter(username=username).exists():
		messages.error(request, 'User with this username already exists. Please use different username')
		return render(request, 'registration.html')

	user = CustomUser()
	user.username = username
	user.email = email_id
	user.password = password
	user.user_type = user_type
	user.first_name = first_name
	user.last_name = last_name
	user.save()
	
	if user_type == CustomUser.STAFF:
		Staffs.objects.create(admin=user)
	elif user_type == CustomUser.STUDENT:
		Students.objects.create(admin=user)
	elif user_type == CustomUser.HOD:
		AdminHOD.objects.create(admin=user)
	return render(request, 'login.html')

	
def logout_user(request):
	logout(request)
	return HttpResponseRedirect('/')
