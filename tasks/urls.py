from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token
from tasks import views

urlpatterns = [
    path('', views.TaskListCreateView.as_view(), name='task-list-create'),  # List and Create
    path('<int:pk>/', views.TaskDetailUpdateDeleteView.as_view(), name='task-detail'),  # Retrieve, Update, Delete
    path('token/', obtain_auth_token, name='api_token_auth'),  # Token creation
    # path('filter/', views.TaskFilterView.as_view(), name='task-filter'),  # Filter tasks by status
]
