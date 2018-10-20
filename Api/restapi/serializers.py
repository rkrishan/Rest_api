from rest_framework import serializers
from .models import UserDetail


class UserDetailSerializer(serializers.ModelSerializer):
    """Serializer to map the Model instance into JSON format."""

    class Meta:
        """Meta class to map serializer's fields with the model fields."""
        model = UserDetail
        fields = ('id', 'first_name', 'last_name','companyName','city','state','zip','email','web','age')
