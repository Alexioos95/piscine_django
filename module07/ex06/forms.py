from django import forms
from .models import Article

class ArticleForm(forms.ModelForm):
	class Meta:
		model = Article
		fields = ["title", "synopsis", "content"]

class NavLoginForm(forms.Form):
	username = forms.CharField(max_length=150)
	password = forms.CharField(widget=forms.PasswordInput)
