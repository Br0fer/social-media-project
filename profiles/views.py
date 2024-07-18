from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView
from profiles.models import Profile, Subscriber, Friendship
from profiles.forms import ProfileCreationForm, SubscriptionCreationForm, FriendRequestCreationForm
from requests.models import FriendRequest

# Create your views here.


class ProfileDetailView(DetailView):
    model = Profile
    context_object_name = "profile"
    template_name = "profile/profile_detailed.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subscription_form"] = SubscriptionCreationForm()

        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    context_object_name = "profile"
    form_class = ProfileCreationForm
    template_name = "profile/profile_update.html"
    success_url = reverse_lazy("my-profile")

    def get_object(self, queryset=None):
        return self.request.user.profile


class MyProfileDetailView(LoginRequiredMixin, DetailView):
    model = Profile
    context_object_name = "my_profile"
    template_name = "profile/profile_detailed.html"

    def get_object(self, queryset=None):
        return self.request.user.profile


class SubscriptionCreateView(LoginRequiredMixin, CreateView):
    model = Subscriber
    context_object_name = "subscription"
    form_class = SubscriptionCreationForm

    def get_success_url(self):
        return reverse_lazy('profile-detailed', kwargs={'pk': self.object.account.pk})

    def get_account(self):
        profile_pk = self.kwargs.get('pk')

        return get_object_or_404(Profile, pk=profile_pk)

    def form_valid(self, form):
        form.instance.subscriber = self.request.user.profile
        form.instance.account = self.get_account()

        return super().form_valid(form)


class FriendRequestCreateView(LoginRequiredMixin, CreateView):
    model = FriendRequest
    context_object_name = "friend_request"
    form_class = FriendRequestCreationForm

    def get_success_url(self):
        return reverse_lazy('profile-detailed', kwargs={'pk': self.object.receiver.pk})

    def get_receiver(self):
        receiver_pk = self.kwargs.get("pk")

        return get_object_or_404(Profile, pk=receiver_pk)

    def form_valid(self, form):
        form.instance.sender = self.request.user.profile
        form.instance.receiver = self.get_receiver()

        return super().form_valid(form)
