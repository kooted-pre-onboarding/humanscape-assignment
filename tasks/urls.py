from django.urls import path
from tasks.views import TaskListView, TaskDetailView, SearchView

urlpatterns = [
    path('/search', SearchView.as_view()),
    path('/<int:task_id>', TaskDetailView.as_view()),
    path('', TaskListView.as_view())
]
