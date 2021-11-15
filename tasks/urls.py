from django.urls import path
from tasks.views import SearchView, TaskDetailView, TaskList

urlpatterns = [
    path('/search', SearchView.as_view()),
    path('/<int:task_id>', TaskDetailView.as_view()),
    path('/list', TaskList.as_view()),
]
