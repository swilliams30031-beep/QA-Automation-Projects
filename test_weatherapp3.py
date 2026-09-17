import pytest
import requests

def test_weather_api_atlanta():
    # 1. API endpoint for city weather data
    url = "https://wttr.in/Atlanta?format=j1"

    # 2. Make GET request
    response = requests.get(url)

    # 3. Assert HTTP status code is 200 OK
    assert response.status_code == 200

    # 4. Parse JSON payload and verify city location
    data = response.json()
    area_name = data["nearest_area"][0]["areaName"][0]["value"]

    assert "Atlanta" in area_name

    # 5. Extract and verify live temperature and humidity
    current_condition = data["current_condition"][0]
    temp_f = current_condition["temp_F"]
    humidity = current_condition["humidity"]

    assert temp_f is not None
    assert humidity is not None

    print(f"\n[SUCCESS] Atlanta Weather: {temp_f} F | Humidity: {humidity}%")

                                 
