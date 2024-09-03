from django import forms
from .models import TextModel

class TextForm(forms.ModelForm):


	class Meta:
		model = TextModel
		fields = ['body','password']
		labels = {'body' : ' ', 'password' : ' '}
		widgets = {'body': forms.Textarea(attrs={'id': 'textfield', 'rows' : '20', 'placeholder': 'Your note goes here'}), 'password' : forms.TextInput(attrs ={'id' : 'pwdfield', 'type' : 'password'}),
        }

	def clean_body(self):
		cleaned = self.cleaned_data
		if len(cleaned["body"]) == 0:
			raise ValidationError("Your note can't be empty!")
		return cleaned["body"]


	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)
		self.label_suffix = ""
		self.fields['password'].required = False
