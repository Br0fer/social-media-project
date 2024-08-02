from django.urls import path
from groups import views

urlpatterns = [
    path('groups/', views.GroupsListView.as_view(), name='groups-list'),

]
