from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_note, name="add"),
    path("list/", views.list_note, name="list"),
    path("put/<note_id>", views.put_note, name="put"),
    path("delete/<note_id>", views.delete_note, name="delete"),

    ]