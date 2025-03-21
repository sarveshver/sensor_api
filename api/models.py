from django.db import models
import secrets  # For secure API key generation
from django.utils.timezone import now

class APIKey(models.Model):
    key = models.CharField(max_length=64, unique=True)  # 64-character API key
    created_at = models.DateTimeField(default=now)

    @staticmethod
    def generate_key():
        return secrets.token_hex(32)  # Generate 64-character random key

    def __str__(self):
        return self.key

class SensorData(models.Model):
    sensor_id = models.CharField(max_length=100)
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sensor_id} - {self.timestamp}"
