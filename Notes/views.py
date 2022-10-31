from multiprocessing import context
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.http import Http404

from .models import Notes


def index(request):
    latest_notes_list = Notes.objects.order_by('-date')[:10]
    context = {'latest_notes_list': latest_notes_list}
    return render(request, 'Notes/index.html', context)

def detail(request, id):
    note = get_object_or_404(Notes, pk=id)
    return render(request, 'Notes/detail.html', {'note': note})

def edit(request):
    note = get_object_or_404(Notes, pk=id)
    try:
        content = note.choice_set.get(pk=request.POST['content'])
    except (KeyError, Notes.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'Notes/detail.html', {
            'note': note,
            'error_message': "You didn't edit a note.",
        })
    else:
        content.save()
        return HttpResponseRedirect(reverse('Notes:detail', args=(note.id,)))