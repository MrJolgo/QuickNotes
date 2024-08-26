from django.urls import path, include
from . import views

urlpatterns = [
	path('', views.main_view, name = "main"),
	path('add', include('texts.urls'))
]