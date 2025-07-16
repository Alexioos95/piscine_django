from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import ListView, RedirectView, DetailView
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import RedirectView
from .models import Article, UserFavouriteArticle
from django.shortcuts import get_object_or_404
from django.contrib.auth import login
from django.urls import reverse_lazy
from .forms import ArticleForm

class HomeRedirectView(RedirectView):
	url = reverse_lazy("ex02:articles")
		
class ArticlesView(ListView):
	model = Article
	template_name = "ex02/articles.html"
	context_object_name = "articles"

class ArticleDetailView(DetailView):
	model = Article
	template_name = "ex02/article_detail.html"
	context_object_name = "article"

class LoginView(FormView):
	template_name = "ex02/login.html"
	form_class = AuthenticationForm
	success_url = reverse_lazy("ex02:home")

	def form_valid(self, form):
		login(self.request, form.get_user())
		return super().form_valid(form)

class PublicationsView(LoginRequiredMixin, ListView):
	model = Article
	template_name = "ex02/my_publications.html"
	context_object_name = "articles"

	def get_queryset(self):
		return Article.objects.filter(author=self.request.user)

class FavouriteArticlesView(LoginRequiredMixin, ListView):
	model = UserFavouriteArticle
	template_name = "ex02/favourites.html"
	context_object_name = "favourites"

	def get_queryset(self):
		return UserFavouriteArticle.objects.filter(user=self.request.user)


class RegisterView(CreateView):
	form_class = UserCreationForm
	template_name = "ex02/register.html"
	success_url = reverse_lazy("ex02:login")

class PublishArticleView(LoginRequiredMixin, CreateView):
	model = Article
	form_class = ArticleForm
	template_name = "ex02/publish.html"
	success_url = reverse_lazy("ex02:publications")

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class AddFavouriteView(LoginRequiredMixin, CreateView):
	model = UserFavouriteArticle
	template_name = "ex02/favourites.html"
	fields = []

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.instance.article = get_object_or_404(Article, pk=self.kwargs["pk"])
		return super().form_valid(form)

	def get_success_url(self):
		return reverse_lazy("ex02:favourites")
