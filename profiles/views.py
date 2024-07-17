from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView
from profiles.models import Profile
from profiles.forms import ProfileCreationForm

# Create your views here.


class ProfileDetailView(DetailView):
    model = Profile
    context_object_name = "profile"
    template_name = "profile/profile_detailed.html"


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    context_object_name = "profile"
    form_class = ProfileCreationForm
    template_name = "profile/profile_update.html"

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_success_url(self):
        return reverse_lazy("profile-detailed", kwargs={"pk": self.request.user.pk})


class MyProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    context_object_name = "profile"
    template_name = "profile/profile_detailed.html"

    def get_object(self, queryset=None):
        return self.request.user.profile
