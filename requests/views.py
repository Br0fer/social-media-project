from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.views.generic import ListView
from requests.models import FriendRequest
# Create your views here.


class FriendRequestListView(LoginRequiredMixin, ListView):
    model = FriendRequest
    context_object_name = "friend_requests"
    template_name = "requests/friendrq_list.html"
