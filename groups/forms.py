from django.forms import ModelForm
from groups.models import Group


class GroupCreationForm(ModelForm):
    class Meta:
        model = Group
        fields = ["title", "description"]

    def __init__(self, *args, **kwargs):
        super(GroupCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control mb-2'}
