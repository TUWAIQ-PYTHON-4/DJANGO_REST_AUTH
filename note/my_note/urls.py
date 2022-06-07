from django.urls import path
from . import views



urlpatterns = [
    path("add", views.add_note, name="add"),
    path("list", views.list_notes, name="list"),
    path("update/<note_id>", views.update_note, name="update"),
    path("delete/<note_id>", views.delete_note, name="delete"),
]