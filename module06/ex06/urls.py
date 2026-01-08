from django.urls import path
from . import views

urlpatterns = [
    # Pages
    path("", views.index, name="index"),
    path("register/", views.register, name="register"),
    path("login/", views.login_v, name="login"),
    # API
    path("logout/", views.logout, name="logout"),
	path("vote/<int:id>/<str:type>/", views.vote, name="vote"),
	path("delete/<int:id>/", views.delete, name="delete"),
]
