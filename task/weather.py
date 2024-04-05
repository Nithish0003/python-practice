import requests

def get_weather(city, api_key):

    url = f"http://api.weatherapi.com/v1/current.json?key={api_key}&q={city}"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        
        weather_data = response.json()

        temperature = weather_data['current']['temp_c']
        wind_direction = weather_data['current']['wind_dir']
        humidity = weather_data['current']['humidity']
        
        print(f"City: {city}")
        print(f"Temperature: {temperature}°C")
        print(f"Wind Direction: {wind_direction}")
        print(f"Humidity: {humidity}%")
    else:
        print(f"Failed to retrieve weather data. Status code: {response.status_code}")
        
# city_name = "coimbatore"
city_name=input("Enter the city name: ")
api_key = "475f71268bfe4af89fd65418242803"

get_weather(city_name, api_key)