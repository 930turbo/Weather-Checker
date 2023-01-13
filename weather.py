import requests
import csv

def get_weather(location):
    # Use OpenWeatherMap API to get weather data for the given location
    api_key = "YOUR_API_KEY_HERE"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={location}&appid={api_key}"
    response = requests.get(url)
    data = response.json()
    return data

def get_clothing_recommendation(temp):
    if temp < 5:
        return "Wear a warm coat, a hat, a scarf, and gloves."
    elif temp < 15:
        return "Wear a jacket and a sweater."
    else:
        return "Wear a light jacket or a sweater."

def export_to_csv(data, location):
    # Export weather data to a CSV file on the user's desktop
    with open(f"C:\\Users\\{username}\\Desktop\\{location}_weather.csv", "w") as file:
        writer = csv.writer(file)
        writer.writerow(["Temperature", "Humidity", "Pressure"])
        writer.writerow([data["main"]["temp"], data["main"]["humidity"], data["main"]["pressure"]])

while True:
    location = input("Enter the location (town or city or state): ")
    forecast_type = input("Enter the forecast type (current, days, or weeks): ")

    if forecast_type == "current":
        data = get_weather(location)
        temp = data["main"]["temp"]
        print(f"The current temperature in {location} is {temp} degrees.")
        print(get_clothing_recommendation(temp))
    elif forecast_type == "days":
        # Code to get forecast for multiple days
        pass
    elif forecast_type == "weeks":
        # Code to get forecast for multiple weeks
        pass
    else:
        print("Invalid forecast type.")

    export = input("Do you want to export the weather data to a CSV file on your desktop? (yes or no) ")
    if export == "yes":
        export_to_csv(data, location)
        print(f"Weather data for {location} has been exported to C:\\Users\\{username}\\Desktop\\{location}_weather.csv")

    user_choice = input("Do you want to enter a new location or close the program? (new or close) ")
    if user_choice == "close":
        break
