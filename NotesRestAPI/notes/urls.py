from django.urls import path
from . import views

app_name = 'notes'
urlpatterns = [
    path('register_user/', views.register_user, name='register_user'),
    path('login_user/', views.login_user, name='login_user'),
    path('add_note/', views.add_note, name='add_note'),
    path('all_notes/', views.all_notes, name='all_notes'),
    path('update_note/<note_id>/', views.update_note, name='update_note'),
    path('delete_note/<note_id>/', views.delete_note, name='delete_note'),

]
