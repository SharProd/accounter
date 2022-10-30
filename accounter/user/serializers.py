from rest_framework import serializers
from .models import Photo,CustomUser


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('id','email','first_name','last_name','is_superuser','last_login','date_joined')


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


