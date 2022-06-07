from django.urls import path
from . import views

app_name = "notes"

urlpatterns = [

    path("note/add", views.add_note, name="Add note"),
    path("note/all", views.list_notes, name="list note"),
    path("note/update/<note_id>", views.update_note, name="update_note"),
    path("note/delete/<note_id>", views.delete_note, name="delete_note"),
]
