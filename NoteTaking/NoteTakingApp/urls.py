from django.urls import path
from . import views

app_name = "NoteTakingApp"

urlpatterns = [
     path("add_note/<str:user_id>/", views.add_note, name="add_note"),
     path("list_note/", views.list_note, name="list_note"),
     path("update_note/<str:note_id>/", views.update_note, name="update_note"),
     path("delete_note/<str:note_id>/", views.delete_note, name="delete_note"),
]