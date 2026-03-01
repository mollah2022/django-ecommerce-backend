from rest_framework.routers import DefaultRouter
from .views import UserViewSet
from django.urls import re_path, include

router = DefaultRouter()
router.register(r'user', UserViewSet, basename='user')  # ✅ এখানে register হলো router object থেকে

urlpatterns = [
    re_path(r'^', include(router.urls)),  # router.urls include করো
]
