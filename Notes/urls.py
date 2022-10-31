from django.urls import path

from .views import  NotesDetailView,HomeView,AddNotesView,EditNotesView,DeleteNotesView

app_name = 'Notes'


urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('specifics/<int:pk>', NotesDetailView.as_view(), name='detail'),
    path('add/', AddNotesView.as_view(), name='add'),
    path('specifics/edit/<int:pk>', EditNotesView.as_view(), name='edit'),
    path('specifics/delete/<int:pk>', DeleteNotesView.as_view(), name='delete'),

] 