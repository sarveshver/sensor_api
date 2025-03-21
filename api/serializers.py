# api/serializers.py
from rest_framework import serializers

class SensorDataSerializer(serializers.Serializer):
    sensor_id = serializers.CharField(max_length=100)
    temperature = serializers.FloatField()
    humidity = serializers.FloatField()
    pressure = serializers.FloatField()
    timestamp = serializers.DateTimeField()
