from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from groups.models import Group, Member, Community, Viewer
from groups.forms import GroupCreationForm, MemberCreationForm


# Create your views here.

class GroupsListView(ListView):
    model = Group
    context_object_name = "groups"
    template_name = "groups/groups_list.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["join_form"] = MemberCreationForm()

        return context


class GroupDetailView(DetailView):
    model = Group
    context_object_name = "group"
    template_name = "groups/group_detailed.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["members"] = Member.objects.filter(group=self.object)

        return context


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
    model = Group
    template_name = "groups/group_creation_page.html"

    def get_success_url(self):
        return reverse_lazy("groups:groups-detail", kwargs={"pk": self.object.pk})


class GroupDeleteView(LoginRequiredMixin, DeleteView):
    model = Group
    template_name = "groups/group_delete_confirmation.html"
    success_url = reverse_lazy("groups:groups-list")


class MemberCreateView(LoginRequiredMixin, CreateView):
    model = Member
    form_class = MemberCreationForm

    def get_group(self):
        group_pk = self.kwargs.get("pk")

        return get_object_or_404(Group, pk=group_pk)

    def form_valid(self, form):
        form.instance.user = self.request.user.profile
        form.instance.group = self.get_group()

        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy("groups:group-detailed", kwargs={"pk": self.kwargs.get("pk")})


class MemberDeleteView(LoginRequiredMixin, DeleteView):
    model = Member
    template_name = "groups/group_leaving_confirmation.html"
    success_url = reverse_lazy("groups:groups-list")
    context_object_name = "member"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["group_pk"] = self.kwargs.get("pk")

        return context

    def get_object(self, queryset=None):
        obj = Member.objects.get(user=self.request.user.profile, group=self.kwargs.get("pk"))

        return obj


class CommunityListView(ListView):
    model = Community
    context_object_name = "communities"
    template_name = "groups/communities_list.html"


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
