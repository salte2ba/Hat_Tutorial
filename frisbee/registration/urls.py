from django.conf.urls import url
from registration import views

urlpatterns = [
	url(r'^$', views.home, name = 'home'),
	url(r'^signup/$', views.signup, name = 'signup'),
	url(r'^thanks/$', views.thanks, name = 'thanks'),
]