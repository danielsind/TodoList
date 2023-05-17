from django.urls import path
from .views import TaskList, TaskDetail, TaskCreate, TaskUpdate, TaskDelete, UserLoginView


urlpatterns = [
    path('', TaskList.as_view(), name='task' ),
    path('login/', UserLoginView.as_view(), name = 'login'),
    path('task-create', TaskCreate.as_view(), name='task-create'),
    path('task/<int:pk>/', TaskDetail.as_view(), name='task_detail'),
    path('task-update/<int:pk>/', TaskUpdate.as_view(), name = 'task-update'),
    path('task-delete/<int:pk>/', TaskDelete.as_view(), name = 'task-delete')
]