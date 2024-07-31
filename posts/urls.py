from django.urls import path
from posts import views


urlpatterns = [
    path("", views.PostsListView.as_view(), name="posts-list"),
    path("<int:pk>/", views.PostDetailView.as_view(), name="post-detailed"),
    path("create_post/", views.PostCreateView.as_view(), name="create-post"),
    path("<int:pk>/delete/", views.PostDeleteView.as_view(), name="delete-post"),
    path("<int:pk>/update/", views.PostUpdateView.as_view(), name="update-post"),
    path("<int:pk>/like/", views.LikeCreateView.as_view(), name="liking-post"),
    path("<int:pk>/comment/", views.CommentCreateView.as_view(), name="commenting-post"),
    path("<int:pk>/comment/delete/", views.CommentDeleteView.as_view(), name="comment-delete"),
    path("<int:pk>/like/delete/", views.LikeDeleteView.as_view(), name="like-delete"),
]


app_name = "posts"
