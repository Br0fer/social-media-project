from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ObjectDoesNotExist, PermissionDenied
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView

from posts.forms import PostCreationForm, PostUpdateForm, LikeCreationForm, CommentCreationForm, RepostCreationForm
from posts.models import Post, Comment, Like, Repost
from posts.mixins import UserIsOwnerMixin, ObjectExistMixin, UserIsNotLikeOwnerMixin, UsersActionMixin, \
    UserIsNotOwnerMixin


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

    def get_watched_post(self):
        post_pk = self.kwargs.get("pk")

        return get_object_or_404(Post, pk=post_pk)


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["liking_form"] = LikeCreationForm()
        context["comment_form"] = CommentCreationForm()
        context["repost_form"] = RepostCreationForm()
        context["comments"] = get_object_or_404(Post, pk=self.kwargs.get("pk")).comments_on_post.all()
        if self.request.user.is_authenticated:
            context["repost"] = self.request.user.profile.shares.filter(post=self.get_watched_post())
            context["like"] = self.request.user.profile.likes.filter(post=self.get_watched_post())

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


class LikeCreateView(LoginRequiredMixin, UserIsNotLikeOwnerMixin, ObjectExistMixin, CreateView):
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


class LikeDeleteView(LoginRequiredMixin, UsersActionMixin, DeleteView):
    model = Like

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_pk"] = self.object.post.pk

        return context

    def get_post(self):
        post_pk = self.kwargs.get("pk")

        return get_object_or_404(Post, pk=post_pk)

    def get_success_url(self):
        return reverse_lazy("posts:post-detailed", kwargs={"pk": self.object.post.pk})


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


class CommentUpdateView(LoginRequiredMixin, UserIsOwnerMixin, UpdateView):
    model = Comment
    template_name = "posts/comment_update_form.html"
    form_class = CommentCreationForm

    def get_success_url(self):
        return reverse_lazy("posts:post-detailed", kwargs={"pk": self.object.related_post.pk})


class CommentDeleteView(LoginRequiredMixin, UserIsOwnerMixin, DeleteView):
    model = Comment
    template_name = "posts/comment_delete_confirmation.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_pk"] = self.object.related_post.pk

        return context

    def get_success_url(self):
        return reverse_lazy("posts:post-detailed", kwargs={"pk": self.object.related_post.pk})


class RepostCreateView(LoginRequiredMixin, CreateView):
    model = Repost
    form_class = RepostCreationForm

    def get_post(self):
        post_pk = self.kwargs.get("pk")

        return get_object_or_404(Post, pk=post_pk)

    def get_success_url(self):
        return reverse_lazy("posts:post-detailed", kwargs={"pk": self.object.post.pk})

    def form_valid(self, form):
        if self.request.user.profile == self.get_post().created_by:
            raise PermissionDenied("You can't repost your own post.")
        form.instance.user = self.request.user.profile
        form.instance.post = self.get_post()

        return super().form_valid(form)


class RepostDeleteView(LoginRequiredMixin, UsersActionMixin, DeleteView):
    model = Repost

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["post_pk"] = self.object.post.pk

        return context

    def get_post(self):
        post_pk = self.kwargs.get("pk")

        return get_object_or_404(Post, pk=post_pk)

    def get_success_url(self):
        return reverse_lazy("posts:post-detailed", kwargs={"pk": self.object.post.pk})
