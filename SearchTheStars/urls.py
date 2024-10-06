from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page
    path('exoplanets/', views.exoplanet_data, name='exoplanet_data'),  # Renders filtered exoplanet data
    path('api/exoplanets/', views.fetch_exoplanet_data, name='fetch_exoplanet_data'),  # Returns JSON exoplanet data
]
