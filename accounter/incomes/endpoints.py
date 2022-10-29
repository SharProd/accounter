from rest_framework.viewsets import ModelViewSet
from rest_framework import permissions
from .serializers import IncomesNoteSerializer

from .models import IncomesNote

class IncomesNoteListCreateAPIView(ModelViewSet):
    queryset = IncomesNote.objects.all()
    serializer_class = IncomesNoteSerializer
    permission_classes = [permissions.IsAuthenticated]
