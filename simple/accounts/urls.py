from django.conf.urls import url
from . import views
from django.contrib.auth.views import logout, password_reset,password_reset_done, password_reset_confirm, password_reset_complete
from django.conf import settings
app_name = 'accounts'
urlpatterns = [
	# home, login and logout
	url(r'^$', views.home, name="home"),
	url(r'^login/$', views.login, name="login"),
	url(r'^logout/$', logout, {'template_name': 'accounts/logout.html'}, name='logout'),

	# register and activation
	url(r'^register/$', views.register, name="register"),
	url(r'^activation/$', views.activation, name="activation"),
	url(r'^activation/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$', views.activation_confirm, name='activation_confirm'),

	#profile
	url(r'^profile/$', views.view_profile, name="view_profile"),
	url(r'^profile/edit/$', views.edit_profile, name="edit_profile"),
	url(r'^profile/password/$', views.change_password, name="change_password"),

	#password_resest
	url(r'^password_reset/$', password_reset,
		{
			'template_name': 'password_reset/password_reset_form.html',
			'subject_template_name': 'password_reset/password_reset_subject.txt',
			'email_template_name': 'password_reset/password_reset_email.html',
			'from_email': settings.EMAIL_HOST_USER,
			'post_reset_redirect': 'accounts:password_reset_done',
		},
		name='password_reset'
		),
	url(r'^password_reset_done/$', password_reset_done,
		{'template_name': 'password_reset/password_reset_done.html'},
		name='password_reset_done'
		),
	url(r'^password_reset_confirm/(?P<uidb64>[0-9A-Za-z]+)-(?P<token>.+)/$',
		password_reset_confirm,
		{
			'template_name': 'password_reset/password_reset_confirm.html',
			'post_reset_redirect': 'accounts:password_reset_complete'
		},
		name='password_reset_confirm'
		),
	url(r'^password_reset_complete/$', password_reset_complete,
		{
			'template_name': 'password_reset/password_reset_complete.html'
		}
		, name='password_reset_complete')
]