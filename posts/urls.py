from django.urls import path
from posts import views


urlpatterns = [
    path("", views.PostsListView.as_view(), name="posts-list"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="post-detailed"),
    path("create_post/", views.PostCreateView.as_view(), name="create-post"),
    path("<int:pk>/delete/", views.PostDeleteView.as_view(), name="delete-post"),

]


app_name = "posts"
