import requests
from django.http import JsonResponse, HttpResponse
from django.shortcuts import render

# Index view to render the homepage
def index(request):
    return render(request, 'SearchTheStars/index.html')

# API view to fetch exoplanet data and return it as JSON (this one remains unchanged)
def fetch_exoplanet_data(request):
    # API URL from Exoplanet Archive for Kepler TCE dataset
    url = 'https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query=select+*+from+q1_q17_dr25_tce&format=json'

    try:
        # Make the API request
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses
        data = response.json()  # Parse JSON response
    except requests.exceptions.HTTPError as errh:
        return JsonResponse({"error": f"HTTP Error: {errh}"}, status=400)
    except requests.exceptions.ConnectionError as errc:
        return JsonResponse({"error": f"Connection Error: {errc}"}, status=400)
    except requests.exceptions.Timeout as errt:
        return JsonResponse({"error": f"Timeout Error: {errt}"}, status=400)
    except requests.exceptions.RequestException as err:
        return JsonResponse({"error": f"Request Error: {err}"}, status=400)

    # Return the data as JSON
    return JsonResponse(data, safe=False)

def exoplanet_data(request):
    # API URL for fetching exoplanet data
    api_url = 'https://2291-98-42-128-53.ngrok-free.app/kepler/4372765'
    
    try:
        # Make the API request
        response = requests.get(api_url)
        response.raise_for_status()  # Ensure we catch any errors
        data = response.json()  # Parse the JSON data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching exoplanet data: {e}")
        data = {}  # Empty dict if the API fails
    
    # Pass the data to the template
    return render(request, 'SearchTheStars/exoplanet_data.html', {
        'star_system': data.get('star_system'),
        'number_of_planets': data.get('number_of_planets'),
        'star_temperature': data.get('star_temperature'),
        'star_size': data.get('star_size'),
        'star_mass': data.get('star_mass'),
        'star_age': data.get('star_age'),
        'ra_dec': data.get('ra_dec'),
        'potential_planets': data.get('potential_planets', []),
        'system_note': data.get('system_note'),
        'discovery_date': data.get('discovery_date'),
        'last_update': data.get('last_update'),
        'smart_summary': data.get('smart_summary'),
    })
