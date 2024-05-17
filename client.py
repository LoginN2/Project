import requests

def get_weather_info(city):
    try:
        url = f"http://localhost:5000/weather?city={city}"
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()

        if 'error' in data:
            print(f"Error: {data['error']}")
        else:
            print(f"Город: {data['name']}")
            print(f"Погода: {data['weather'][0]['main']}")
            print(f"Температура: {data['main']['temp']}°C")
            print(f"Ощущается как: {data['main']['feels_like']}°C")

    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    city = input("Введите город: ")
    get_weather_info(city)