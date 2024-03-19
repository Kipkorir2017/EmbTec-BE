from rest_framework import serializers
from .models import Data, Services


class DataSerializer(serializers.ModelSerializer):
    class Meta:
        model=Data
        
        fields=('name', 'description','user')

class ServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model=Services
        fields=('name','description','price')       