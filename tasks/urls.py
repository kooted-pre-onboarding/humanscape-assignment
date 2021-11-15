from django.urls import path
from tasks.views import SearchView, TaskDetailView

urlpatterns = [
    path('/search', SearchView.as_view()),
    path('/<int:task_id>', TaskDetailView.as_view()),
]
