from django import forms
from .models import Profile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
    """Form definition for User."""

    class Meta:
        """Meta definition for UserForm."""

        model = User
        fields = ('username','first_name','last_name','email',)

class ProfileForm(forms.ModelForm):
    """Form definition for ProfileForm."""

    class Meta:
        """Meta definition for ProfileFormform."""

        model = Profile
        fields = ('country', 'address', 'image',)
