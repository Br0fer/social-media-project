from django.urls import path
from groups import views

urlpatterns = [
    path('groups/', views.GroupsListView.as_view(), name='groups-list'),
    path('groups/create/', views.GroupCreateView.as_view(), name='group-create'),
    path('groups/<int:pk>/', views.GroupDetailView.as_view(), name='group-detailed'),
    path('groups/<int:pk>/delete/', views.GroupDeleteView.as_view(), name='group-delete'),
    path('groups/<int:pk>/update/', views.GroupUpdateView.as_view(), name='group-update'),
    path('groups/<int:pk>/join/', views.MemberCreateView.as_view(), name='group-join'),
    path('groups/<int:pk>/leave/', views.MemberDeleteView.as_view(), name='group-leave'),
    path('communities/', views.CommunityListView.as_view(), name='communities-list'),
    path('communities/create/', views.CommunityCreateView.as_view(), name='community-create'),

]

app_name = 'groups'
