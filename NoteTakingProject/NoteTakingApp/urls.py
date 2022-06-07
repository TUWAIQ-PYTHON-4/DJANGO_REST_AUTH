from django.urls import path
from . import views



urlpatterns = [
    path("add_note/", views.add_note, name="add_note"),
    path("list_Note/", views.list_Note, name="list_Note"),
    path("update_note/<note_id>", views.update_note, name="update_note"),
    path("delete_note/<note_id>", views.delete_note, name="delete_note"),


]