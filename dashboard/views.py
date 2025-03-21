import requests
from django.shortcuts import render
from django.http import JsonResponse

# API URL that provides the sensor data (replace with your actual API URL)
API_URL = 'http://127.0.0.1:8000/api/get-sensor-data/'  # Change to your API URL

# View that renders the dashboard with Plotly graphs
def dashboard(request):
    return render(request, 'index.html')

# API view that fetches data from your API
def get_sensor_data(request):
    try:
        # Fetch data from your external API
        response = requests.get(API_URL)
        data = response.json()

        # Return the data as JSON to the frontend
        return JsonResponse(data, safe=False)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)
