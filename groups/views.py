from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from groups.models import Group, Member, Community, Viewer
from groups.forms import GroupCreationForm


# Create your views here.

class GroupsListView(ListView):
    model = Group
    context_object_name = "groups"
    template_name = "groups/groups_list.html"


class GroupCreateView(LoginRequiredMixin, CreateView):
    model = Group
    form_class = GroupCreationForm
    template_name = "groups/group_creation_page.html"
    success_url = reverse_lazy("groups:groups-list")

    def form_valid(self, form):
        form.instance.created_by = self.request.user.profile
        group = form.save()

        Member.objects.create(user=self.request.user.profile, group=group).save()
        group.save()

        return super().form_valid(form)


class GroupUpdateView(LoginRequiredMixin, UpdateView):
    pass


class GroupDeleteView(LoginRequiredMixin, DeleteView):
    pass


class MembersListView(ListView):
    pass


class MemberCreateView(LoginRequiredMixin, CreateView):
    pass


class MemberDeleteView(LoginRequiredMixin, DeleteView):
    pass


class CommunityListView(ListView):
    pass


class CommunityCreateView(LoginRequiredMixin, CreateView):
    pass


class CommunityUpdateView(LoginRequiredMixin, UpdateView):
    pass


class CommunityDeleteView(LoginRequiredMixin, DeleteView):
    pass


class ViewerListView(ListView):
    pass


class ViewerCreateView(LoginRequiredMixin, CreateView):
    pass


class ViewerDeleteView(LoginRequiredMixin, DeleteView):
    pass
