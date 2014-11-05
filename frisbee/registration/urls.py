from django.conf.urls import url
from registration import views

urlpatterns = [
	url(r'^$', views.home, name = 'home'),
]