from django.views.generic import ListView, RedirectView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from .models import Article

class HomeRedirectView(RedirectView):
	url = reverse_lazy("ex00:articles")

class ArticleListView(ListView):
	model = Article
	template_name = "ex00/articles.html"
	context_object_name = "articles"

class CustomLoginView(LoginView):
	template_name = "ex00/login.html"
	authentication_form = AuthenticationForm

	def get_success_url(self):
		return reverse_lazy("ex00:home")
