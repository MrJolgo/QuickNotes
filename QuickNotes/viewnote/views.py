from django.shortcuts import render, get_object_or_404
from texts import models

def note_view(request, note_id):
	note = get_object_or_404(models.TextModel, text_id = note_id)
	print(note.body)
	print(note.text_id)
	return render(request, 'viewnote/note.html', {'note' : note})

	