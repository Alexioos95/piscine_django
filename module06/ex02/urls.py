from django.urls import path
from . import views

urlpatterns = [
	# Pages
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("login/", views.login, name="login"),
	# API
    path("logout/", views.logout, name="logout"),
]
