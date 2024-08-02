from django.urls import path
from groups import views

urlpatterns = [
    path('groups/', views.GroupsListView.as_view(), name='groups-list'),
    path('groups/create/', views.GroupCreateView.as_view(), name='groups-create'),

]

app_name = 'groups'
