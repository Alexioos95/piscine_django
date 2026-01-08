from django.views.generic import ListView, RedirectView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.base import RedirectView
from .models import Article, UserFavouriteArticle
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.urls import reverse_lazy

class HomeRedirectView(RedirectView):
	url = reverse_lazy("ex01:articles")
		
class ArticlesView(ListView):
	model = Article
	template_name = "ex01/articles.html"
	context_object_name = "articles"

class ArticleDetailView(DetailView):
	model = Article
	template_name = "ex01/article_detail.html"
	context_object_name = "article"

class LoginView(FormView):
	template_name = "ex01/login.html"
	form_class = AuthenticationForm
	success_url = reverse_lazy("ex01:home")

	def form_valid(self, form):
		login(self.request, form.get_user())
		return super().form_valid(form)

class PublicationsView(LoginRequiredMixin, ListView):
	model = Article
	template_name = "ex01/my_publications.html"
	context_object_name = "articles"

	def get_queryset(self):
		return Article.objects.filter(author=self.request.user)

class FavouriteArticlesView(LoginRequiredMixin, ListView):
	model = UserFavouriteArticle
	template_name = "ex01/favourites.html"
	context_object_name = "favourites"

	def get_queryset(self):
		return UserFavouriteArticle.objects.filter(user=self.request.user)
