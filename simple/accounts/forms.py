# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import (
	AuthenticationForm, PasswordChangeForm, UserCreationForm, PasswordResetForm
)
from django.contrib.auth import get_user_model
# Tạo người dùng
class simple_UserCreationFrom(UserCreationForm):
	error_messages = { 'password_mismatch': "Mật khẩu không đúng", 'user_already': "Tài khoản đã tồn tại",}
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Tài khoản'}),)
	email = forms.EmailField(widget=forms.TextInput(attrs={'placeholder': 'Email'}))
	password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Mật khẩu'}))
	password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Xác nhận mật khẩu'}))
	first_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Tên'}))
	last_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Họ'}))
	
	def clean_username(self):
		username = self.cleaned_data['username']
		if User.objects.filter(username=username).exists():
			raise forms.ValidationError(
				self.error_messages['user_already'],
				code='user_already',
			)
		return username

	def save(self, commit=True):
		user = super(simple_UserCreationFrom, self).save(commit=False)
		user.username = self.cleaned_data['username']
		user.email = self.cleaned_data['email']
		user.first_name = self.cleaned_data['first_name']
		user.last_name = self.cleaned_data['last_name']
		user.is_active = False
		user.set_password(self.cleaned_data['password1'])
		if commit:
			user.save()
			return user
	class Meta:
		model = User
		fields = ["username", "email", "first_name", "last_name", "password1", "password2"]

# Đổi thông tin cá nhân người dùng
class UserChangeForm(forms.ModelForm):
	email = forms.EmailField(label='Email',help_text="Ví dụ: email@example.com", widget=forms.TextInput())
	first_name = forms.CharField(label="Tên", help_text="Ví dụ: Vũ Luân")
	last_name = forms.CharField(label="Họ", help_text="Ví dụ: Đoàn")
	class Meta:
		model = User
		fields = ['email', 'first_name','last_name']

# Đổi mật khẩu người dùng
class simple_PasswordChangeForm(PasswordChangeForm):
	error_messages = {'password_mismatch': "2 mật khẩu không đúng", 'password_incorrect': "Mật khẩu cũ không đúng. Vui lòng nhập lại"}
	old_password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Mật khẩu cũ'}))
	new_password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Mật khẩu mới'}))
	new_password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Xác nhận mật khẩu'}))

# Đăng nhập
class LoginForm(AuthenticationForm):
	username = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Tài khoản'}))
	password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Mật khẩu'}))
# Kích hoạt tài khoản
class simple_PasswordResetForm(PasswordResetForm):
	email = forms.EmailField(widget=forms.EmailInput(attrs={'placeholder': 'Email'}))
	def get_users(self, email):
		active_users = get_user_model()._default_manager.filter(email__iexact=email)
		return (u for u in active_users if u.has_usable_password())