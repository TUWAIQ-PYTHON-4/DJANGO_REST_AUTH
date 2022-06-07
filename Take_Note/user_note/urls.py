from django.urls import path
from . import views



urlpatterns = [
    path("note/add", views.add_note, name="add_note"),
    path("note/all", views.list_note, name="list_note"),
    path("note/update/<note_id>", views.update_note, name="update_note"),
    path("note/delete/<note_id>", views.delete_note, name="delete_note"),
]