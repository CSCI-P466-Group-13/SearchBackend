from rest_framework import serializers
from .models import property
from .models import car

class propertySerializer(serializers.ModelSerializer):
    class Meta:
        model = property
        fields = '__all__'

class carSerializer(serializers.ModelSerializer):
    class Meta:
        model = car
        fields = '__all__'
