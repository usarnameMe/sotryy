from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Profile, Story


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']
        extra_kwargs = {
            'password': {'write_only': True}
        }

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password']
        )
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)


class ProfileSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=False)
    email = serializers.EmailField(source='user.email', read_only=False)
    password = serializers.CharField(source='user.password', write_only=True, required=False)

    class Meta:
        model = Profile
        fields = ['username', 'email', 'password', 'bio', 'profile_image']

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user', {})
        password = user_data.get('password')

        user = instance.user
        user.username = user_data.get('username', user.username)
        user.email = user_data.get('email', user.email)
        if password:
            user.set_password(password)
        user.save()

        instance.bio = validated_data.get('bio', instance.bio)
        instance.profile_image = validated_data.get('profile_image', instance.profile_image)
        instance.save()

        return instance


class StorySerializer(serializers.ModelSerializer):
    author = serializers.StringRelatedField()

    class Meta:
        model = Story
        fields = ['id', 'author', 'title', 'content', 'created_at', 'is_public']
