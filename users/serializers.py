from rest_framework.serializers import ModelSerializer

from users.models import User


class RegisterSerializer(ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "password"]
        read_only_fields = ["id"]
        extra_kwargs = {"password": {"write_only": True}}

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
