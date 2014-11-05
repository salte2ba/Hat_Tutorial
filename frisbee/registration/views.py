from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic

from registration.models import Add_person

class homeView(generic.ListView):
	model = Add_person
	template_name = 'registration/home.html'
	context_object_name = 'welcome'

class signup (generic.ListView):
	model = Add_person
	template_name = 'registration/signup.html'

class thanks(generic.ListView):
	model = Add_person
	template_name = 'registration/thanks.html'		

