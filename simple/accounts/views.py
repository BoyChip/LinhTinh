# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from django.contrib.auth import update_session_auth_hash, login as auth_login
from .forms import (
	LoginForm, simple_PasswordResetForm, UserChangeForm,
    simple_PasswordChangeForm, simple_UserCreationFrom,
	)
from django.urls import reverse
from django.contrib.auth.tokens import default_token_generator
from django.conf import settings
from django.contrib.auth import get_user_model
from django.utils.encoding import force_text
from django.utils.http import urlsafe_base64_decode
# Create your views here.

def default(request):
	return redirect(reverse('accounts:home'))

def view_profile(request):
    return render(request, 'accounts/profile.html', {'user': request.user})

def edit_profile(request):
	if request.method == 'POST':
		form = UserChangeForm(request.POST, instance=request.user)
		if form.is_valid():
			form.save()
			return redirect(reverse('accounts:view_profile'))
	else:
		form = UserChangeForm(instance=request.user)
	return render(request, 'accounts/editprofile.html', {'form': form})
	
# change password
def change_password(request):
	if request.method == 'POST':
		form = simple_PasswordChangeForm(data=request.POST, user=request.user)

		if form.is_valid():
			form.save()
			update_session_auth_hash(request, form.user)
			return redirect(reverse('accounts:view_profile'))
	else:
		form = simple_PasswordChangeForm(user=request.user)
	return render(request, 'accounts/changepassword.html', {'form': form})

def login(request):
	if request.method == 'POST':
		form = LoginForm(request, data=request.POST)
		if form.is_valid():
			auth_login(request, form.get_user())
			return redirect(reverse('accounts:home'))
	else:
		form = LoginForm(request)
	return render(request, 'accounts/login.html', {'form': form})

def register(request):
    if request.method == 'POST':
        form = simple_UserCreationFrom(request.POST)
        if form.is_valid():
            form.save()
            activation(request)
            return redirect(reverse('accounts:login'))
    else:
        form = simple_UserCreationFrom()
    return render(request, 'accounts/signup.html', {'form': form})

def activation(request,
               template_name='activation/activation_form.html',
               subject_template_name='activation/activation_subject.txt',
               email_template_name='activation/activation_email.html',
               activation_form = simple_PasswordResetForm,
               token_generator = default_token_generator,
               from_email=settings.EMAIL_HOST_USER):
    if request.method == 'POST':
        form = activation_form(request.POST)
        if form.is_valid():
            kwargs = {
                'use_https':request.is_secure(),
                'token_generator': token_generator,
                'subject_template_name': subject_template_name,
                'email_template_name': email_template_name,
                'from_email': from_email,
                'request': request,
                'html_email_template_name': None
            }
            form.save(**kwargs)
            return render(request, 'activation/activation_done.html')
    else:
        form = activation_form()
    return render(request, template_name, {'form': form})

def activation_confirm(request, uidb64=None, token=None, token_generator=default_token_generator):
    UserModel = get_user_model()
    assert uidb64 is not None and token is not None
    try:
        uid = force_text(urlsafe_base64_decode(uidb64))
        user = UserModel._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, UserModel.DoesNotExists):
        user=None

    if user is not None and token_generator.check_token(user, token):
        if not user.is_active:
            user.is_active = True
            user.save()
            return render(request, 'activation/activation_complete.html', {'message': 'Kích hoạt thành công'})
        else:
            return render(request, 'activation/activation_complete.html', {'message': 'Tài khoản đã kích hoạt rồi'})
    else:
        return render(request, 'activation/activation_complete.html', {'message': 'Kích hoạt thất bại'})