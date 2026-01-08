from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.views.generic import ListView, RedirectView, DetailView
from django.views.generic.edit import FormView, CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import RedirectView
from .models import Article, UserFavouriteArticle
from django.contrib.auth.views import LoginView
from django.shortcuts import get_object_or_404
from .forms import ArticleForm, NavLoginForm
from django.contrib.auth import login
from django.urls import reverse_lazy

class HomeRedirectView(RedirectView):
	url = reverse_lazy("ex03:articles")
		
class ArticlesView(ListView):
	model = Article
	template_name = "ex03/articles.html"
	context_object_name = "articles"

	def get_queryset(self):
		return Article.objects.order_by("-created")

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["nav_login_form"] = NavLoginForm()
		return context

class ArticleDetailView(DetailView):
	model = Article
	template_name = "ex03/article_detail.html"
	context_object_name = "article"

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["nav_login_form"] = NavLoginForm()
		return context

class LoginView(FormView):
	template_name = "ex03/login.html"
	form_class = AuthenticationForm
	success_url = reverse_lazy("ex03:home")

	def form_valid(self, form):
		login(self.request, form.get_user())
		return super().form_valid(form)

class PublicationsView(LoginRequiredMixin, ListView):
	model = Article
	template_name = "ex03/my_publications.html"
	context_object_name = "articles"

	def get_queryset(self):
		return Article.objects.filter(author=self.request.user)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["nav_login_form"] = NavLoginForm()
		return context

class FavouriteArticlesView(LoginRequiredMixin, ListView):
	model = UserFavouriteArticle
	template_name = "ex03/favourites.html"
	context_object_name = "favourites"

	def get_queryset(self):
		return UserFavouriteArticle.objects.filter(user=self.request.user)

	def get_context_data(self, **kwargs):
		context = super().get_context_data(**kwargs)
		context["nav_login_form"] = NavLoginForm()
		return context

class RegisterView(CreateView):
	form_class = UserCreationForm
	template_name = "ex03/register.html"
	success_url = reverse_lazy("ex03:login")

class PublishArticleView(LoginRequiredMixin, CreateView):
	model = Article
	form_class = ArticleForm
	template_name = "ex03/publish.html"
	success_url = reverse_lazy("ex03:publications")

	def form_valid(self, form):
		form.instance.author = self.request.user
		return super().form_valid(form)

class AddFavouriteView(LoginRequiredMixin, CreateView):
	model = UserFavouriteArticle
	template_name = "ex03/favourites.html"
	fields = []

	def form_valid(self, form):
		form.instance.user = self.request.user
		form.instance.article = get_object_or_404(Article, pk=self.kwargs["pk"])
		return super().form_valid(form)

	def get_success_url(self):
		return reverse_lazy("ex03:favourites")

class NavLoginView(LoginView):
	authentication_form = NavLoginForm

	def form_invalid(self, form):
		from django.shortcuts import redirect, render
		response = render(self.request, "ex03/articles.html", {
			"login_form": form,
		})
		response.status_code = 401
		return response
