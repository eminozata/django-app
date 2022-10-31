from multiprocessing import context
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.views.generic import UpdateView,DetailView,ListView,CreateView,DeleteView, DeleteView
from django.http import Http404

from django.urls import reverse_lazy




from .models import Notes


class HomeView(ListView):
    model = Notes
    template_name = 'Notes/index.html'

class NotesDetailView(DetailView):
    model = Notes
    template_name = 'Notes/detail.html'

class AddNotesView(CreateView):
    model = Notes
    template_name = 'Notes/add.html'
    fields = '__all__'

class EditNotesView(UpdateView):
    model = Notes
    template_name = 'Notes/edit.html'
    fields = '__all__'

class DeleteNotesView(DeleteView):
    model = Notes
    template_name = 'Notes/delete.html'
    success_url=  reverse_lazy('Notes:home')
