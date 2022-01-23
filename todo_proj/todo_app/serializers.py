from rest_framework import serializers
from todo_app.models import Task


class TaskCreateSerializer(serializers.ModelSerializer):
    """
    Shows when we're creating a task
    """
    created_time = serializers.ReadOnlyField()

    class Meta:
        model = Task
        fields = ['header', 'text', 'liable', 'image', 'created_time']


class TaskListSerializer(serializers.ModelSerializer):
    """
    Shows when we see a list of tasks
    """

    class Meta:
        model = Task
        fields = ['owner', 'header', 'text', 'liable', 'image', 'created_time']


class TaskDetailSerializer(serializers.ModelSerializer):
    """
    Shows when we look at exact task
    """
    class Meta:
        model = Task
        fields = ['id', 'owner', 'header', 'text', 'liable', 'image', 'created_time']
