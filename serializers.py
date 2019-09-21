from rest_framework import serializers
from .models import Builds, Inks, Follows
from django.contrib.auth import get_user_model

UserModel = get_user_model()


class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = UserModel.objects.create(
            username = validated_data["username"]
        )
        user.first_name = validated_data["first_name"]
        user.last_name = validated_data["last_name"]
        user.set_password(validated_data["password"])
        user.save()
        return user

    class Meta:
        model = UserModel
        fields = '__all__'

class GetUsersSerializer(serializers.ModelSerializer):

    class Meta:
        model = UserModel
        fields = ('id', 'username')


class BuildsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Builds
        fields = ('username', 'build', 'date')



class InksSerializer(serializers.ModelSerializer):

    class Meta:
        model = Inks
        fields = ('username', 'ink', 'date')


class FollowsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Follows
        fields = ('followers', 'following')