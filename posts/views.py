from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from posts.forms import PostCreationForm, PostUpdateForm, LikeCreationForm, CommentCreationForm, RepostCreationForm
from posts.models import Post, Comment, Like
from posts.mixins import UserIsOwnerMixin, ObjectExistMixin, UserIsNotOwnerMixin


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["liking_form"] = LikeCreationForm()
        context["comment_form"] = CommentCreationForm()
        context["comments"] = get_object_or_404(Post, pk=self.kwargs.get("pk")).comments_on_post.all()

        return context


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


class LikeCreateView(LoginRequiredMixin, UserIsNotOwnerMixin, ObjectExistMixin, CreateView):
    model = Like
    form_class = LikeCreationForm

    def get_post(self):
        post_pk = self.kwargs.get("pk")

        return get_object_or_404(Post, pk=post_pk)

    def get_success_url(self):
        return reverse_lazy("posts:post-detailed", kwargs={"pk": self.object.post.pk})

    def form_valid(self, form):
        form.instance.post = self.get_post()
        form.instance.user = self.request.user.profile

        return super().form_valid(form)


class LikeDeleteView(LoginRequiredMixin, DeleteView):
    model = Like
    template_name = "posts/like_delete_confirmation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_pk"] = self.object.liked_post.pk

        return context

    def get_post(self):
        post_pk = self.kwargs.get("pk")

        return get_object_or_404(Post, pk=post_pk)

    def get_success_url(self):
        return reverse_lazy("posts:post-detailed", kwargs={"pk": self.object.liked_post.pk})


class CommentCreateView(LoginRequiredMixin, CreateView):
    model = Comment
    form_class = CommentCreationForm

    def get_post(self):
        post_pk = self.kwargs.get("pk")

        return get_object_or_404(Post, pk=post_pk)

    def get_success_url(self):
        return reverse_lazy("posts:post-detailed", kwargs={"pk": self.object.related_post.pk})

    def form_valid(self, form):
        form.instance.created_by = self.request.user.profile
        form.instance.related_post = self.get_post()

        return super().form_valid(form)


class CommentDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Comment
    template_name = "posts/comment_delete_confirmation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_pk"] = self.object.related_post.pk

        return context

    def get_success_url(self):
        return reverse_lazy("posts:post-detailed", kwargs={"pk": self.object.related_post.pk})
