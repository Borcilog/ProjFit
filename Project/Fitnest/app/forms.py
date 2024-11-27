from django import forms
from .models import Video, Contact, Enrollment
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'video_file', 'description']

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'message']

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]

class ClassEnrollmentForm(forms.ModelForm):
    class Meta:
        model = Enrollment
        fields = ['user', 'class_schedule']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['user'].widget = forms.HiddenInput()