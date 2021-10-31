from rest_framework_mongoengine import serializers
from .models import Demo
class DemoSerializers(serializers.DocumentSerializer):
    class Meta:
        model = Demo
        fields ='__all__'