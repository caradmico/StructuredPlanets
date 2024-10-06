from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('SearchTheStars.urls')),  # Delegate all SearchTheStars app URLs
]
