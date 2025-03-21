from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

def home_redirect(request):
    return redirect("dashboard/")  # Redirect `/` to `/dashboard/`

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')),  
    path('dashboard/', include('dashboard.urls')),
    path('', home_redirect, name='home_redirect'),  # Add this line
]
