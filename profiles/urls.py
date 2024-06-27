from django.urls import path
from profiles import views


urlpatterns = [
    path('<int:pk>/', views.ProfileDetailView.as_view(), name="profile-detailed")
]
