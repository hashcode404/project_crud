from django.contrib.auth.models import User
from rest_framework import serializers
from django.db import models
from .models import Profile

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['phone_number', 'address', 'date_of_birth']

class UserSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'profile']

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile',None)
        instance = super().update(instance, validated_data)

        profile, created = Profile.objects.get_or_create(user=instance)
        profile.phone_number = profile_data.get('phone_number', profile.phone_number)
        profile.address = profile_data.get('address', profile.address)
        profile.date_of_birth = profile_data.get('date_of_birth', profile.date_of_birth)
        profile.save()
        print(f"Updated User: {instance.profile.address}")
        print(f"Updated Profile: phone_number={profile.phone_number}, address={profile.address}, date_of_birth={profile.date_of_birth}")


        return instance
class RegistrationSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    profile = ProfileSerializer(required=True)  # Make profile required

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'profile']

    def create(self, validated_data):
        profile_data = validated_data.pop('profile')
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        # Handle profile creation
        Profile.objects.update_or_create(
            user=user,
            defaults={
                'phone_number': profile_data['phone_number'],
                'address': profile_data['address'],
                'date_of_birth': profile_data['date_of_birth']
            }
        )
        return user