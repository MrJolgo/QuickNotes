from django import forms
from django.contrib.auth import get_user_model

class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField(widget = forms.PasswordInput)
    #def clean(self):
        #cleaned = form.cleaned_data
           # user = authenticate(request, email = cleaned['email'], password = cleaned['password'])
            #if user is not None:  
                #login(request, user)

class RegisterForm(forms.ModelForm):
    password = forms.CharField(label = 'Password', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Repeat passowrd', widget = forms.PasswordInput)
    
    class Meta:
        model = get_user_model()
        fields = ['email']
    def clean_password2(self):
        cleaned = self.cleaned_data
        if cleaned['password'] != cleaned['password2']:
            raise forms.ValidationError('Passwords are not the same')
        return cleaned['password2']
