from rest_framework import generics, filters
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
# from django_filters.rest_framework import DjangoFilterBackend
from .models import Task
from .serializers import TaskSerializer
import logging
# Pagination
class TaskPagination(PageNumberPagination):
    page_size = 10  # Number of tasks per page

# List and Create Tasks (GET and POST)

class TaskListCreateView(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = TaskPagination
    # filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        try:
            return Task.objects.filter(user=self.request.user)
        except Exception as e:
            print(f"Error in get_queryset: {e}")
            return Task.objects.none()

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

    def get(self, request, *args, **kwargs):
        # Print the token for debugging
        auth_header = request.headers.get('Authorization')
        if auth_header:
            token = auth_header.split(' ')[1]  # Assumes format is "Bearer <token>"
            print(f"Token: {token}")
        else:
            print("No Authorization header found")

        return super().get(request, *args, **kwargs)

# Retrieve, Update, and Delete a Task (GET, PUT, DELETE)



logger = logging.getLogger(__name__)

class TaskDetailUpdateDeleteView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    lookup_field = 'pk'

    def get_queryset(self):
        logger.info(f"TaskDetailUpdateDeleteView called for user {self.request.user}")
        return Task.objects.filter(user=self.request.user)
# Filter by status
class TaskStatusFilterView(generics.ListAPIView):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    pagination_class = TaskPagination
    # filter_backends = [DjangoFilterBackend]

    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    





    

# URL patterns would look like this:
# urlpatterns = [
#     path('tasks/', views.TaskListCreateView.as_view(), name='task-list'),
#     path('tasks/<int:pk>/', views.TaskDetailUpdateDeleteView.as_view(), name='task-detail'),
#     path('tasks/status/', views.TaskStatusFilterView.as_view(), name='task-status-filter'),
# ]
