from django.urls import path
from .views import *

app_name = "ex00"

urlpatterns = [
	path("", HomeRedirectView.as_view(), name="home"),
	path("articles", ArticleListView.as_view(), name="articles"),
	path("login", CustomLoginView.as_view(), name="login"),
]
