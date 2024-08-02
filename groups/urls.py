from django.urls import path
from groups import views

urlpatterns = [
    path('groups/', views.GroupsListView.as_view(), name='groups-list'),
    path('groups/create/', views.GroupCreateView.as_view(), name='groups-create'),
    path('groups/<int:pk>/', views.GroupDetailView.as_view(), name='group-detailed'),
    path('groups/<int:pk>/delete/', views.GroupDeleteView.as_view(), name='groups-delete'),

]

app_name = 'groups'
