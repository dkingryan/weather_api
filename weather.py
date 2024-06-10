import requests

class City:
    def __init__(self, name, lat, lon, units="imperial"):
        self.name = name
        self.lat = lat
        self.lon = lon
        self.units = units
        self.get_data()

    def get_data(self):
        try:
            response = requests.get(f"https://api.openweathermap.org/data/2.5/weather?units={self.units}&lat={self.lat}&lon={self.lon}&appid=79007029562c2ab46617d801d8018750")
        except:
            print("No internet connection L")

        response_json = response.json()
        self.temp = response_json["main"]["temp"]
        self.temp_min = response_json["main"]["temp_min"]
        self.temp_max = response_json["main"]["temp_max"]
        self.feels_like = response_json["main"]["feels_like"]

    def display(self):
        units_symbol = "F"
        if self.units == "metric":
            units_symbol = "C"
        print(f"{self.name} weather right now: {self.temp}° {units_symbol}")
        print(f"Feels-like: {self.feels_like}° {units_symbol}")
        print(f"Low for the day: {self.temp_min}° {units_symbol}")
        print(f"High for the day: {self.temp_max}° {units_symbol}")

city_name = input("Enter the city name: ")
lat = float(input("Enter the latitude: "))
lon = float(input("Enter the longitude: "))
units = input("Enter the units (metric or imperial): ")
my_city = City(city_name, lat, lon, units)
my_city.display()
#my_city = City("Tokyo",35.652832, 139.839478)
