from django.urls import include, path

from rest_framework import routers
from profilepage.views import UserListApiView,TodoListApiView,LinkListApiView

router = routers.DefaultRouter()
router.register(r'users', UserListApiView)
router.register(r'todos', TodoListApiView)
router.register(r'links', LinkListApiView)

urlpatterns = [
   path('', include(router.urls)),
]