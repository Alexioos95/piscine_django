from django.contrib.auth import authenticate
from ex04.models import MyUser
from django import forms
from .models import Tip


class RegisterForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput, label="Password")
	confirm_password = forms.CharField(widget=forms.PasswordInput, label="Confirm Password")

	class Meta:
		model = MyUser
		fields = ["username", "password"]

	def clean_username(self):
		username = self.cleaned_data.get("username")
		if MyUser.objects.filter(username=username).exists():
			raise forms.ValidationError("This username is already taken.")
		return username

	def clean(self):
		cleaned_data = super().clean()
		password = cleaned_data.get("password")
		confirm = cleaned_data.get("confirm_password")
		if password != confirm:
			raise forms.ValidationError("Passwords do not match.")
		return cleaned_data

class LoginForm(forms.Form):
	username = forms.CharField(label="Username")
	password = forms.CharField(widget=forms.PasswordInput, label="Password")

	def clean(self):
		cleaned_data = super().clean()
		username = cleaned_data.get("username")
		password = cleaned_data.get("password")

		if not username or not password:
			raise forms.ValidationError("All fields are required.")
		user = authenticate(username=username, password=password)
		if user is None:
			raise forms.ValidationError("Invalid username or password.")
		cleaned_data["user"] = user
		return cleaned_data

class TipForm(forms.ModelForm):
	class Meta:
		model = Tip
		fields = ["content"]
