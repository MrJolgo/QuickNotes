from django.shortcuts import render
from .forms import TextForm

def text_view(request):
	if request.method == "POST":
		note = TextForm(request.POST)
		if note.is_valid():
			new_note = note.save(commit = False)
			if note.cleaned_data["password"] != "":
				new_note.set_password(note.cleaned_data["password"])
			new_note.save()
			uuid = new_note.text_id
			return render(request, "texts/successful.html", {"uuid" : uuid})

	return render(request, "texts/textadd.html", {"text_form" : TextForm()})