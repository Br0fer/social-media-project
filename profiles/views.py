from django.shortcuts import render
from django.views.generic import DetailView
from profiles.models import Profile

# Create your views here.


class ProfileDetailView(DetailView):
    model = Profile
    context_object_name = "profile"
    template_name = "profile/profile_detailed.html"
