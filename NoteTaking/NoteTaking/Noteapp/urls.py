from django.urls import path
from . import views

app_name = "Noteapp"

urlpatterns = [
    path("notes/add", views.add_note, name="Add note"),
    path("notes/all", views.list_notes, name="list notes"),
    path("notes/update/<note_id>", views.update_note, name="update_note"),
    path("notes/delete/<note_id>", views.delete_note, name="delete_note"),
]