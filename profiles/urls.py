from django.urls import path
from profiles import views


urlpatterns = [
    path('<int:pk>/', views.ProfileDetailView.as_view(), name="profile-detailed"),
    path("update/", views.ProfileUpdateView.as_view(), name="profile-update"),
    path("my_profile/", views.MyProfileDetailView.as_view(), name="my-profile"),
    path("<int:pk>/subscribe/", views.SubscriptionCreateView.as_view(), name="subscribe"),
    path("<int:pk>/unsubscribe/", views.SubscriptionDeleteView.as_view(), name="unsubscribe"),
    path("<int:pk>/send_friendrq/", views.FriendRequestCreateView.as_view(), name="friendrq"),
    path("<int:pk>/create_friendship/", views.FriendshipCreateView.as_view(), name="friendship"),
    path("<int:pk>/delete_friendrq/", views.FriendRequestDeleteView.as_view(), name="friendreq-delete")
]

app_name = "profile"
