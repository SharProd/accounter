from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from .endpoints import (
    UserListCreateAPIView,PhotoListCreateAPIView
)


router = DefaultRouter()
router.register(r"user", UserListCreateAPIView)
router.register(r"photo",PhotoListCreateAPIView)

urlpatterns = [
    path('', include(router.urls)),
]