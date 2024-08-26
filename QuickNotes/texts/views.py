from django.shortcuts import render
from .forms import TextForm

def text_view(request):
	if request.method == "POST":
		note = TextForm(request.POST)
		if note.is_valid():
			note.save()
			return render(request, "texts/successful.html")
	return render(request, "texts/textadd.html", {"text_form" : TextForm()})