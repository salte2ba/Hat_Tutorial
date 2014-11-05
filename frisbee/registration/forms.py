from django.forms import ModelForm
from registration.models import Add_person

class Add_personForm (ModelForm):
	class Meta:
		model = Add_person
		fields = ['first_name', 'last_name', 'sex', 'email', 'phone', 'skills', 'wants_shirt', 'wants_frisbee','shirtsize', 'position']