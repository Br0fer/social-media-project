from django.forms import ModelForm
from groups.models import Group, Member, Channel, Viewer


class GroupCreationForm(ModelForm):
    class Meta:
        model = Group
        fields = ["title", "description"]

    def __init__(self, *args, **kwargs):
        super(GroupCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control mb-2'}


class MemberCreationForm(ModelForm):
    class Meta:
        model = Member
        fields = []


class ViewerCreationForm(ModelForm):
    class Meta:
        model = Viewer
        fields = []


class ChannelCreationForm(ModelForm):
    class Meta:
        model = Channel
        fields = ['title', 'description']

    def __init__(self, *args, **kwargs):
        super(ChannelCreationForm, self).__init__(*args, **kwargs)
        for field in self.fields:
            self.fields[field].widget.attrs = {'class': 'form-control mb-2'}
