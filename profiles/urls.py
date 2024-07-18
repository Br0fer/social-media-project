from django.urls import path
from profiles import views


urlpatterns = [
    path('<int:pk>/', views.ProfileDetailView.as_view(), name="profile-detailed"),
    path("update/", views.ProfileUpdateView.as_view(), name="profile-update"),
    path("my_profile/", views.MyProfileDetailView.as_view(), name="my-profile"),
    path("<int:pk>/subscribe/", views.SubscriptionCreateView.as_view(), name="subscribe"),
    path("<int:pk>/send_friendrq/", views.FriendRequestCreateView.as_view(), name="friendrq")
]
