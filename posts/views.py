from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from posts.forms import PostCreationForm, PostUpdateForm
from posts.models import Post, Comment, Like
from posts.mixins import UserIsOwnerMixin

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


class PostDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Post
    template_name = "posts/post_delete_confirmation.html"
    success_url = reverse_lazy("posts:posts-list")


class PostUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Post
    form_class = PostUpdateForm
    context_object_name = "post"
    template_name = "posts/post_update_form.html"

    def get_success_url(self):
        return reverse_lazy("posts:post-detailed", kwargs={"pk": self.object.pk})
