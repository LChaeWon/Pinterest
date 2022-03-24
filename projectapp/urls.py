from django.urls import path

from projectapp.views import ProjectCreateView, ProjectDetailView, projectListView


app_name = 'projectapp'

urlpatterns = [
    path('list/', projectListView.as_view(), name='list'),
    path('create/', ProjectCreateView.as_view(), name='create'),
    path('detail/<int:pk>', ProjectDetailView.as_view(), name='detail'),


]