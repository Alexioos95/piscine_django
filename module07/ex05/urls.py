from django.contrib.auth.views import LogoutView
from django.conf.urls.i18n import set_language
from .views import NavLoginView
from django.urls import path
from .views import *

app_name = "ex05"

urlpatterns = [
	path("", HomeRedirectView.as_view(), name="home"),
	path("articles/", ArticlesView.as_view(), name="articles"),
	path("publications/", PublicationsView.as_view(), name="publications"),
	path("article/<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
	path("favourites/", FavouriteArticlesView.as_view(), name="favourites"),
	path("register/", RegisterView.as_view(), name="register"),
	path("publish/", PublishArticleView.as_view(), name="publish"),
	path("favourite/add/<int:pk>/", AddFavouriteView.as_view(), name="add_favourite"),
	path("login/", NavLoginView.as_view(), name="login"),
	path("logout/", LogoutView.as_view(next_page="ex05:home"), name="logout"),
	path("i18n/setlang/", set_language, name="set_language"),
]
