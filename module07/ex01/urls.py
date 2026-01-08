from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import (
	HomeRedirectView,
	ArticlesView,
	ArticleDetailView,
	LoginView,
	PublicationsView,
	FavouriteArticlesView,
)

app_name = "ex01"

urlpatterns = [
	path("", HomeRedirectView.as_view(), name="home"),
	path("articles/", ArticlesView.as_view(), name="articles"),
	path("login/", LoginView.as_view(), name="login"),
	path("publications/", PublicationsView.as_view(), name="publications"),
	path("article/<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
	path("logout/", LogoutView.as_view(next_page="ex01:home"), name="logout"),
	path("favourites/", FavouriteArticlesView.as_view(), name="favourites"),
]
