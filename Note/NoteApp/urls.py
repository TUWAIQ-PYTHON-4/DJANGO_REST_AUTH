from django.urls import path
from . import views

# app_name = "NoteApp"

urlpatterns = [

    path("add/", views.add_note, name="add_note"),
    path("all/", views.list_note, name="list_note"),
    path("update/<note_id>/", views.update_note, name="update_note"),
    path("delete/<note_id>/", views.delete_note, name="delete_note"),
]
