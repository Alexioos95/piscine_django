from django import forms

class Form(forms.Form):
	input = forms.CharField(label='input', max_length=100)
