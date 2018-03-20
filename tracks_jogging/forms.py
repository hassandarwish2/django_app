from django import forms
from django.contrib.auth.forms import UserCreationForm

from tracks_jogging.models import TrackList, TodoItem, Track


class TodoListCreateForm(forms.ModelForm):
    class Meta:
        fields = ('time','distance','date' )
        model = Track

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user')
        super().__init__(*args, **kwargs)

    def save(self, commit=True):
        self.instance.user = self.user
        return super().save(commit)






class UserSignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        fields = ('username', 'first_name', 'last_name', 'email')