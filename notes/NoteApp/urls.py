from django.urls import path
from . import views

urlpatterns = [
    path('display_notes', views.display_notes, name='display_notes'),
    path('add_note', views.add_note, name='add_note'),
    path('Update_note/<int:id>', views.Update_note, name='Update_note'),
    path('delete_note/<int:id>', views.delete_note, name='delete_note'),
]
