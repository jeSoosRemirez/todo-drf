from django.urls import path, include
from django.contrib import admin


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('todo_app.urls')),
    path('', include('users.urls')),
]

urlpatterns += [
    path('api-auth/', include('rest_framework.urls')),
]
