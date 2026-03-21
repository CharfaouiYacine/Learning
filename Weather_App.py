import requests

api_key = "My API key"
def get_weather(city):
    try:
        response = requests.get(f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}')
        data = response.json()
        print(f"------{city} Weather-------\nThe weather is: {data['current']['condition']['text']}\nTemperature in celsius: {data['current']['temp_c']}\nTemperature in fahrenheit: {data['current']['temp_f']}\nHumidity is:{data['current']['humidity']}")
    except Exception:
        response= requests.get(f'https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}')
        print(f"didn't find anything , Error: {response}")
def main():
    city = input("Please enter your City: ").title()
    get_weather(city)

if __name__ == '__main__':
    main()

"""You enter a city and get the weather and temperature back from the weather API"""