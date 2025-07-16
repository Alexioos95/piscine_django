from django.contrib.auth.views import LogoutView
from django.urls import path
from .views import *

app_name = "ex02"

urlpatterns = [
	path("", HomeRedirectView.as_view(), name="home"),
	path("articles/", ArticlesView.as_view(), name="articles"),
	path("login/", LoginView.as_view(), name="login"),
	path("publications/", PublicationsView.as_view(), name="publications"),
	path("article/<int:pk>/", ArticleDetailView.as_view(), name="article_detail"),
	path("logout/", LogoutView.as_view(next_page="ex02:home"), name="logout"),
	path("favourites/", FavouriteArticlesView.as_view(), name="favourites"),
	path("register/", RegisterView.as_view(), name="register"),
	path("publish/", PublishArticleView.as_view(), name="publish"),
	path("favourite/add/<int:pk>/", AddFavouriteView.as_view(), name="add_favourite"),
]
