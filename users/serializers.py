from rest_framework import serializers
from users.models import Passport
from django.contrib.auth import get_user_model

UserProfile = get_user_model()

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'
