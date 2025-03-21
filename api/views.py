from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from api.models import APIKey, SensorData

# Handle the submission of sensor data (POST)
@csrf_exempt  # Allow requests from external sources
def submit_sensor_data(request):
    # Debugging: Print received request method
    print(f"🔹 Received Request Method: {request.method}")

    if request.method != "POST":
        print("❌ Only POST requests are allowed")
        return JsonResponse({"error": "Only POST requests are allowed"}, status=405)

    # Get API Key from request headers
    api_key = request.META.get("HTTP_AUTHORIZATION", "").strip()
    print(f"🔹 Received API Key: {repr(api_key)}")  # Debugging API key

    # Fetch stored API keys from the database
    stored_keys = set(APIKey.objects.values_list("key", flat=True))
    print("🔹 Stored API Keys:", stored_keys)

    # Validate API Key
    if api_key not in stored_keys:
        print("❌ Invalid API Key")
        return JsonResponse({"error": "Invalid API key"}, status=403)

    # Parse JSON data from request body
    try:
        data = json.loads(request.body)
        print("🔹 Received Data:", data)  # Debugging received data
        sensor_id = data.get("sensor_id")
        temperature = data.get("temperature")
        humidity = data.get("humidity")
        pressure = data.get("pressure")
    except json.JSONDecodeError as e:
        print(f"❌ JSON Decode Error: {str(e)}")  # More detailed error
        return JsonResponse({"error": "Invalid JSON format"}, status=400)

    # Validate required fields in the sensor data
    missing_fields = [field for field in ["sensor_id", "temperature", "humidity", "pressure"] if data.get(field) is None]
    
    if missing_fields:
        print(f"❌ Missing fields: {', '.join(missing_fields)}")  # Debugging missing fields
        return JsonResponse({"error": f"Missing required fields: {', '.join(missing_fields)}"}, status=400)

    # Save the sensor data to the database
    try:
        SensorData.objects.create(
            sensor_id=sensor_id,
            temperature=temperature,
            humidity=humidity,
            pressure=pressure
        )
        print("✅ Sensor Data Saved Successfully")
        return JsonResponse({"success": "Data received"}, status=201)
    except Exception as e:
        print(f"❌ Database Error: {str(e)}")  # Debugging database errors
        return JsonResponse({"error": "Failed to save sensor data"}, status=500)

# Handle retrieving sensor data (GET)
def get_sensor_data(request):
    # Fetch all sensor data from the database
    sensor_data = list(SensorData.objects.values())

    # Return a JSON response with the sensor data
    if sensor_data:
        return JsonResponse(sensor_data, safe=False)  # Safe=False for returning a list of dictionaries
    else:
        return JsonResponse({"error": "No sensor data found"}, status=404)
