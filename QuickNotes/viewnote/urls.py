from django.urls import path, include
from . import views

urlpatterns = [
	path('<uuid:note_id>', views.note_view, name = "note"),
]