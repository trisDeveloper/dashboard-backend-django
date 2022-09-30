from django.urls import include, path

from rest_framework import routers
from profilepage.views import UserListApiView

router = routers.DefaultRouter()
router.register(r'users', UserListApiView)

urlpatterns = [
   path('', include(router.urls)),
]