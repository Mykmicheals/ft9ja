from rest_framework import serializers
from .models import TraderData, Trader
from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'is_staff')


class TraderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trader
        fields = '__all__'


class TraderDataSerializer(serializers.ModelSerializer):
    class Meta:
        model = TraderData
        fields = '__all__'
