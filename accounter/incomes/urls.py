from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter
from .endpoints import (
    IncomesNoteListCreateAPIView,
)


router = DefaultRouter()
router.register(r"income", IncomesNoteListCreateAPIView)

urlpatterns = [
    path('', include(router.urls)),
]