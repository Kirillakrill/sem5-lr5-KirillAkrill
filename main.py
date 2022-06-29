import json
import requests

api_key = "a6863e45-d899-4с6л-9343-85805c3dс12d" # Создаем api_key
url = "https://api.weather.yandex.ru/v2/forecast"

def get_weather_week(lat, lon):
    
    weather = dict()

    url = 'https://api.weather.yandex.ru/v2/forecast' # Получаем
    req = requests.get(
        url, 
        params = {
            "lat": str(lat),
            "lon": str(lon)
        },
        headers = { "X-Yandex-API-Key": api_key }
        )

    req_obj = json.loads(req.text)  

    days_lst = [obj for obj in req_obj["forecasts"]] # Обрабатываем

    for day in days_lst:
        weather[day["date"][5:10]] = day["parts"]["day"]["temp_avg"] # Форматируем
    
    return weather


def get_weather_hours(lat, lon):
    
    weather = dict()

    url = 'https://api.weather.yandex.ru/v2/forecast' # Получаем
    req = requests.get(
        url, 
        params = {
            "lat": str(lat),
            "lon": str(lon)
        },
        headers = { "X-Yandex-API-Key": api_key }
        )

    req_obj = json.loads(req.text)  

    days_lst = [(obj["date"], obj["hours"]) for obj in req_obj["forecasts"]]  # Обрабатываем
    
    days_lst = [obj for obj in req_obj["forecasts"]] # Итерируем
    for day in days_lst:
        for hour in day['hours']:
            weather[str(day["date"][5:10]) + " " + str(hour['hour']) + "ч"] = hour["temp"] # Форматируем


    return weather

def vizualize_data(weather): # Визуализируем
    import matplotlib.pyplot as pplt

    dates = list(weather.keys())
    values = list(weather.values())

    pplt.xlabel("Dates")
    pplt.ylabel("Temps")
    pplt.scatter(dates, values)

    pplt.show()

if __name__ == "__main__":
    vizualize_data(get_weather_week(55.45, 37.36))
    vizualize_data(get_weather_hours(55.45, 37.36))
