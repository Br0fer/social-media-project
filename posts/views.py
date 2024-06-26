from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from posts.models import Post, Comment, Like

# Create your views here.


class PostsListView(ListView):
    model = Post
    context_object_name = "posts"
    template_name = "posts/posts_list.html"


class PostDetailView(DetailView):
    model = Post
    context_object_name = "post"
    template_name = "posts/post_detailed.html"
