from django.urls import path
from . import views

urlpatterns = [
	# Pages
    path("", views.index, name="index"),
	# API
	path('api/username/', views.get_username, name='get_username'),
]
