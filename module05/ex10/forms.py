from django import forms
from ex09.models import People

class Form(forms.Form):
	min_date = forms.DateField(label="Movies minimum release date")
	max_date = forms.DateField(label="Movies maximum release date")
	min_diameter = forms.IntegerField(label="Planet diameter greater than")
	gender = forms.ChoiceField(label="Character gender")

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		genders = People.objects.exclude(gender__isnull=True).exclude(gender="").values("gender").distinct()
		self.fields["gender"].choices = [(choice["gender"], choice["gender"]) for choice in genders]
