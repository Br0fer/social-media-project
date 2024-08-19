from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import DetailView, UpdateView, CreateView, DeleteView
from profiles.models import Profile, Subscriber, Friendship
from profiles.forms import ProfileCreationForm, SubscriptionCreationForm, FriendRequestCreationForm, \
    FriendshipCreationForm
from requests.models import FriendRequest
from django.core.exceptions import ObjectDoesNotExist


# Create your views here.


class ProfileDetailView(DetailView):
    model = Profile
    context_object_name = "profile"
    template_name = "profile/profile_detailed.html"

    def get_watched_profile(self):
        user_pk = self.kwargs.get("pk")

        return get_object_or_404(Profile, pk=user_pk)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["subscription_form"] = SubscriptionCreationForm()
        context["friendrequest_form"] = FriendRequestCreationForm()
        if self.request.user.is_authenticated:
            context["friendrequest"] = self.request.user.profile.friend_requests_send.filter(
                receiver=self.get_watched_profile())
            context["subscription"] = self.request.user.profile.subscriptions.filter(
                account=self.get_watched_profile())

        return context


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    context_object_name = "profile"
    form_class = ProfileCreationForm
    template_name = "profile/profile_update.html"
    success_url = reverse_lazy("profile:my-profile")

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
        return reverse_lazy('profile:profile-detailed', kwargs={'pk': self.object.account.pk})

    def get_account(self):
        profile_pk = self.kwargs.get('pk')

        return get_object_or_404(Profile, pk=profile_pk)

    def form_valid(self, form):
        form.instance.subscriber = self.request.user.profile
        form.instance.account = self.get_account()

        return super().form_valid(form)


class SubscriptionDeleteView(LoginRequiredMixin, DeleteView):
    model = Subscriber
    template_name = "profile/subscription_delete_confirmation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_pk"] = self.object.account.pk

        return context

    def get_success_url(self):
        return reverse_lazy('profile:profile-detailed', kwargs={'pk': self.object.account.pk})


class FriendRequestCreateView(LoginRequiredMixin, CreateView):
    model = FriendRequest
    context_object_name = "friend_request"
    form_class = FriendRequestCreationForm

    def get_success_url(self):
        return reverse_lazy('profile:profile-detailed', kwargs={'pk': self.object.receiver.pk})

    def get_receiver(self):
        receiver_pk = self.kwargs.get("pk")

        return get_object_or_404(Profile, pk=receiver_pk)

    def form_valid(self, form):
        form.instance.sender = self.request.user.profile
        form.instance.receiver = self.get_receiver()

        return super().form_valid(form)


class FriendRequestDeleteView(LoginRequiredMixin, DeleteView):
    model = FriendRequest
    template_name = "requests/friendrq_delete_confirmation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["user_pk"] = self.object.receiver.pk

        return context

    def get_success_url(self):
        return reverse_lazy('profile:profile-detailed', kwargs={'pk': self.object.receiver.pk})


class FriendshipCreateView(LoginRequiredMixin, CreateView):
    model = Friendship
    context_object_name = "friendship"
    form_class = FriendshipCreationForm

    def get_success_url(self):
        return reverse_lazy('profile:profile-detailed', kwargs={'pk': self.object.user2.pk})

    def get_friend_request(self):
        friend_request_pk = self.kwargs.get("pk")

        return get_object_or_404(FriendRequest, pk=friend_request_pk)

    def form_valid(self, form):
        friend_request = self.get_friend_request()
        form.instance.user1 = self.request.user.profile
        form.instance.user2 = self.get_friend_request().sender
        friend_request.accepted = True
        friend_request.save()

        return super().form_valid(form)
