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
    path('channels/', views.ChannelListView.as_view(), name='channels-list'),
    path('channels/create/', views.ChannelCreateView.as_view(), name='channel-create'),
    path('channels/<int:pk>/update/', views.ChannelUpdateView.as_view(), name='channel-update'),
    path('channels/<int:pk>/delete/', views.ChannelDeleteView.as_view(), name='channel-delete'),
    path('channels/<int:pk>/', views.ChannelDetailView.as_view(), name='channel-detailed'),

]

app_name = 'groups'
