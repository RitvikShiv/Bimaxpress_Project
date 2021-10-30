from rest_framework_mongoengine import serializers
from .models import Register
class RegisterSerializer(serializers.DocumentSerializer):
    class Meta:
        model = Register
        fields = '__all__'
