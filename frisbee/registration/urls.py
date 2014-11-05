from django.conf.urls import url
from registration import views

urlpatterns = [
	url(r'^$', views.homeView.as_view(), name = 'home'),
	url(r'^signup/$', views.signup.as_view(), name = 'signup'),
	url(r'^thanks/$', views.thanks.as_view(), name = 'thanks'),
]