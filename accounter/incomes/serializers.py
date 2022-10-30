from rest_framework import serializers
from .models import IncomesNote
from user.serializers import PhotoSerializer



class IncomesNoteSerializer(serializers.ModelSerializer):
    photo = PhotoSerializer()
    class Meta:
        model = IncomesNote
        fields = ('id','user','date_in_check','score','photo','where_from')
