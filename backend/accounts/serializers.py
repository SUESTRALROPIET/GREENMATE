from rest_framework import serializers
from django.contrib.auth import get_user_model
from .views.token import create_token


User = get_user_model()


class UserInfoSerializer(serializers.ModelSerializer):
    access_token = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = ('id', 'nickname', 'is_certified', 'language', 'vege_type', 'access_token', 'refresh_token',)
    
    def get_access_token(self, obj):
        return create_token({'email': obj.kakao_email}, 'access')

    
class UserSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'nickname', 'vege_type',)
        read_only_fields = ('id',)


class UserPutSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User
        fields = ('id', 'nickname', 'vege_type', 'is_certified', 'language',)
        read_only_fields = ('id',)
