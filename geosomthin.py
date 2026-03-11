import requests 
import os 
import json
 
#weather code table: https://www.nodc.noaa.gov/archive/arc0021/0002199/1.1/data/0-data/HTML/WMO-CODE/WMO4677.HTM
 
 
DATA_FILE = "snowdar.json"
URL = "https://geocoding-api.open-meteo.com/v1/search"
 
def getDataFromCity(loc):
    params = {
        "name": loc,
        "count": 10,

    }
    
    response = requests.get(URL, params=params)
    print(response.json().keys())
    return response.json()
 
#city structure:
#name: city name
#lat: latitude
#lon: longitude
def remove_duplicates(data):
    clean = []
 
    for item in data:
        if item not in clean:
            clean.append(item)
 
    return clean
 
def load_data(filename=DATA_FILE):
    if not os.path.exists(filename):
        return []   # start empty if file doesn't exist
    with open(filename, "r") as f:
        return json.load(f)
 
 
def save_data(data, filename=DATA_FILE, mode="append"):
    if mode == "overwrite":
        combined = data
    else:  # append
        combined = load_data(filename) + data
 
    with open(filename, "w") as f:
        json.dump(combined, f, indent=2)
 


cities_Name = [    "Cairo","Alexandria","Giza","Luxor","Aswan","Khartoum","Addis Ababa","Nairobi",
    "Lagos","Abuja","Accra","Johannesburg","Cape Town","Durban","Tunis","Algiers",
    "Casablanca","Rabat","Tokyo","Osaka","Kyoto","Nagoya","Seoul","Busan","Beijing",
    "Shanghai","Guangzhou","Shenzhen","Hong Kong","Taipei","Manila","Bangkok","Hanoi",
    "Ho Chi Minh City","Phnom Penh","Yangon","Kuala Lumpur","Singapore","Jakarta",
    "Surabaya","New Delhi","Mumbai","Kolkata","Chennai","Bengaluru","Hyderabad",
    "Pune","Ahmedabad","Jaipur","Lucknow","Colombo","Dhaka","Kathmandu","Islamabad",
    "Lahore","Karachi","Kabul","Tehran","Baghdad","Riyadh","Jeddah","Dubai",
    "Abu Dhabi","Doha","Kuwait City","Amman","Jerusalem","Tel Aviv","Beirut",
    "Damascus","Istanbul","Ankara","Izmir","Tbilisi","Yerevan","Baku","Astana",
    "Almaty","Tashkent","Ulaanbaatar","London","Manchester","Paris","Lyon",
    "Marseille","Berlin","Hamburg","Munich","Frankfurt","Vienna","Zurich","Geneva",
    "Milan","Rome","Florence","Venice","Madrid","Barcelona","Valencia","Lisbon",
    "Porto","Amsterdam","Rotterdam","Brussels","Dublin","Oslo","Stockholm",
    "Copenhagen","Helsinki","Warsaw","Kraków","Prague","Budapest","Athens",
    "Belgrade","Zagreb","Sarajevo","Moscow","Saint Petersburg","Kyiv","Lviv",
    "New York City","Los Angeles","Chicago","Houston","Phoenix","Philadelphia",
    "San Antonio","San Diego","Dallas","San Francisco","Seattle","Denver",
    "Las Vegas","Miami","Orlando","Tampa","Atlanta","New Orleans","Mexico City",
    "Guadalajara","Monterrey","Cancún","Guatemala City","San Salvador",
    "Panama City","Bogotá","Medellín","Cali","Lima","Cusco","La Paz","Santiago",
    "Buenos Aires","Córdoba","Rosario","Montevideo","Asunción","São Paulo",
    "Rio de Janeiro","Brasília","Salvador","Recife","Fortaleza","Sydney",
    "Melbourne","Brisbane","Perth","Canberra","Auckland","Wellington",
    "Christchurch","Honolulu",
]
cities = []
for city_name in cities_Name:
    data = getDataFromCity(city_name)
    for item in data["results"]:
        newCity = {
            "name": item["name"],
            "lat": item["latitude"],
            "lon": item["longitude"]
            
            }
        cities.append(newCity)
        existing = load_data(DATA_FILE)
        combined = existing + cities
        unique_cities = remove_duplicates(combined)
        save_data(unique_cities, filename=DATA_FILE, mode="overwrite")
    print("raw Data", data["results"])



save_data(cities)

print("Saved", len(cities), "cities to", DATA_FILE)