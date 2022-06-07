from django.urls import path
from . import views

urlpatterns = [
    path("add/", views.add_note, name="add"),
    path("list/", views.list_note, name="list"),
    path("update/<notes_id>/", views.update_note, name="update"),
    path("delete/<notes_id>/", views.delete_note, name="delete"),

]
