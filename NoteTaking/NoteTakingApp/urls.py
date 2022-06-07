from django.urls import path
from . import views

app_name = "students"

urlpatterns = [
    path("list_notes/", views.list_notes, name="list notes"),
    path("add_note/", views.add_note, name="Add note"),
    path("update_note/<note_id>", views.update_note, name="update note"),
    path("delete_note/<note_id>", views.delete_note, name="delete note"),

]
