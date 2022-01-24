from rest_framework.decorators import api_view
from rest_framework.generics import RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.reverse import reverse
from todo_app.models import Task
from todo_app.serializers import TaskListSerializer, TaskCreateSerializer, TaskDetailSerializer
from users.backends import JWTAuthentication
from todo_app.permissions import IsOwnerOrReadOnly


class TaskCreateView(CreateAPIView):
    """
    This APIView provides `create` action
    with 'header', 'text', 'liable', 'image',
    'created_time'(auto filled).
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    queryset = Task.objects.all()
    serializer_class = TaskCreateSerializer

    def perform_create(self, serializer):
        # The request user is set as owner automatically.
        serializer.save(owner=self.request.user)


class TaskListView(ListAPIView):
    """
    This APIView provides `list` action
    with 'owner', 'header', 'text', 'liable',
    'image', 'created_time'.
    """
    permission_classes = (IsAuthenticated,)
    authentication_classes = (JWTAuthentication,)
    queryset = Task.objects.all()
    serializer_class = TaskListSerializer


class TaskDetailView(RetrieveUpdateDestroyAPIView):
    """
    This APIView provides 'retrieve', `update` or 'destroy' actions
    with 'id', 'owner', 'header', 'text', 'liable', 'image', 'created_time'
    """
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly,)
    authentication_classes = (JWTAuthentication,)
    queryset = Task.objects.all()
    serializer_class = TaskDetailSerializer


@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        # Task api roots
        'tasks': reverse('task-list', request=request, format=format),
        'task-create': reverse('task-create', request=request, format=format),

        # User api roots
        'register': reverse('register', request=request, format=format),
        'login': reverse('login', request=request, format=format),
        'update': reverse('update', request=request, format=format),
    })
