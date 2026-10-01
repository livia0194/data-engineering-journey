import requests

URL = "https://api.open-meteo.com/v1/forecast"

params = {
    "latitude": 52.66,      # Limerick
    "longitude": -8.63,
    "hourly": "temperature_2m,precipitation",
    "past_days": 1,
    "forecast_days": 1,
}


def main():
    response = requests.get(URL, params=params)
    print("Status code:", response.status_code)

    data = response.json()
    hourly = data["hourly"]
    times = hourly["time"]
    temps = hourly["temperature_2m"]
    rain = hourly["precipitation"]

    print("Hours of data:", len(times))
    print("First hour:", times[0], temps[0], "°C")
    print("Warmest:", max(temps), "°C")
    print("Total rain:", sum(rain), "mm")
    print("Lowest:", min(temps),"°C")
    print ("Total Temprature:",sum(temps), "°C")
    print("Average temprature", sum(temps)/len(times), "°C")
  

    for t, temp, r in zip(times, temps, rain):
        print(t, temp, r)

        if r > 0:
            print("Rained at", t, ":", r, "mm")


if __name__ == "__main__":
    main()