from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from groups.models import Group, Member, Community, Viewer


# Create your views here.

class GroupsListView(ListView):
    model = Group
    context_object_name = "groups"
    template_name = "groups/groups_list.html"


class GroupCreateView(LoginRequiredMixin, CreateView):
    pass


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
