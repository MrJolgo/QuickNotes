from django import forms
from .models import TextModel

class TextForm(forms.ModelForm):
	class Meta:
		model = TextModel
		fields = ["body"]
		labels = {"body" : " "}
		widgets = {'body': forms.TextInput(attrs={'class': 'note'}),
        }


	def clean_body(self):
		cleaned = self.cleaned_data
		if len(cleaned["body"]) == 0:
			raise ValidationError("Your note can't be empty!")
		return cleaned["body"]

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.label_suffix = ""