from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from posts.forms import PostCreationForm
from posts.models import Post, Comment, Like

# Create your views here.


class PostsListView(ListView):
    model = Post
    paginate_by = 10
    context_object_name = "posts"
    template_name = "posts/posts_list.html"


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "posts/post_detailed.html"


class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    success_url = reverse_lazy("posts:posts-list")
    form_class = PostCreationForm
    template_name = "posts/post_creation_form.html"

    def form_valid(self, form):
        form.instance.created_by = self.request.user.profile

        return super().form_valid(form)
