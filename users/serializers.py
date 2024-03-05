from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['first_name', 'last_name', 'username', 'email', 'password']
        extra_kwargs = {'password': {'write_only': True}}


    def create(self, validated_data):
        user = self.Meta.model(**validated_data)
        password = validated_data.pop("password", None)

        if password is not None:
            user.set_password(password)
        user.save()
        return user