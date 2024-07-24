from django import forms

from posts.models import Post


class PostCreationForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "description", "media"]

    def __init__(self, *args, **kwargs):
        super(PostCreationForm, self).__init__(*args, **kwargs)

        for field in self.fields:
            self.fields[field].widget.attrs.update({'class': "form-control mb-2"})

        self.fields["media"].widget.attrs.update({'class': "form-control mb-2", "type": "file"})
