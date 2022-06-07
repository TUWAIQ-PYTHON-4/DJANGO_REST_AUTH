from django.urls import path
from . import views


urlpatterns = [
    path("note/add", views.add_note, name="Add note"),
    path("notes/all", views.list_note, name="list notes"),
    path("update/<note_id>", views.update_note, name="update note"),
    path("delete/<note_id>", views.delete_note, name="delete note"),

]


