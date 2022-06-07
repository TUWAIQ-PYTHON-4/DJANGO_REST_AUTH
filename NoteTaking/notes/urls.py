from django.urls import path
from . import views


urlpatterns = [
    path("note/add", views.create_note, name="create_note"),
    path("note/all", views.list_notes, name="list_notes"),
    path("note/edit/<note_id>", views.edit_note, name="edit_note"),
    path("note/remove/<note_id>", views.remove_note, name="remove_note"),
]

