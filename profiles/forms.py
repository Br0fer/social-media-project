from django import forms
from profiles.models import Profile


class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['pfp', 'username', 'bio', 'status', 'banner']

    def __init__(self, *args, **kwargs):
        super(ProfileCreationForm, self).__init__(self, *args, **kwargs)

