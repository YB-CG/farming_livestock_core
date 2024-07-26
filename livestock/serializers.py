from rest_framework import serializers
from .models import LiveStock, Farm

class FarmSerializer(serializers.ModelSerializer):
    class Meta:
        model = Farm
        fields = '__all__'

class LivestockSerializer(serializers.DjangoModelField):
    class Meta:
        model = LiveStock
        fields = '__all__'

