from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView
from profiles.models import Profile, Subscriber, Friendship
from profiles.forms import ProfileCreationForm, SubscriptionCreationForm

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

    def get_context_data(self, **kwargs):
        context = super(self).get_context_data(**kwargs)
        context["subscription_form"] = SubscriptionCreationForm()

        return context

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_success_url(self):
        return reverse_lazy("profile-detailed", kwargs={"pk": self.request.user.pk})


class MyProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    context_object_name = "my_profile"
    template_name = "profile/profile_detailed.html"

    def get_object(self, queryset=None):
        return self.request.user.profile


class SubscriptionCreateView(CreateView):
    model = Subscriber
    context_object_name = "subscription"
    form_class = SubscriptionCreationForm

    def get_account(self):
        profile_pk = self.kwargs.get("pk")

        return get_object_or_404(Profile, pk=profile_pk)

    def form_valid(self, form):
        form.instance.subscriber = self.request.user.profile
        form.instance.account = self.get_account()

        return form
