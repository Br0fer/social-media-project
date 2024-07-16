from django import forms
from profiles.models import Profile


class ProfileCreationForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['pfp', 'username', 'bio', 'status', 'banner']

    def __init__(self, *args, **kwargs):
        super(ProfileCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': "form-control mb-2"})

        self.fields["pfp"].widget.attrs.update({'class': "form-control mb-2", 'type': "file"})
        self.fields["banner"].widget.attrs.update({'class': "form-control mb-2", 'type': "file"})
