from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False,label="Full Name", help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, label="Contact Number", help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1' )

class ContactForm(forms.Form):
    name = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    # subject = forms.CharField(required=True)
    message = forms.CharField(widget=forms.Textarea, required=True)
