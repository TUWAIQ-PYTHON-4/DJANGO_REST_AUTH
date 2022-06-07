from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_new_note, name="Add new note"),
    path("show/", views.notes_show, name="Show Notes"),
    path("update/<note_id>", views.update_note, name="update Note"),
    path("delete/<note_id>", views.delete_note, name="delete Note ")
            ]
