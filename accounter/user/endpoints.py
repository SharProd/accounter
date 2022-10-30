from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializers import UserSerializer,PhotoSerializer

from .models import CustomUser,Photo

class UserListCreateAPIView(ModelViewSet):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAdminUser]


class PhotoListCreateAPIView(ModelViewSet):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    permission_classes = [permissions.IsAdminUser]

