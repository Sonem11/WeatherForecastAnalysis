import requests
import pandas as pd

API_KEY = "Your Api Key"
CITY = "Belgrade"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

response = requests.get(URL)
data = response.json()

# Extract forecast list
forecast_list = data["list"]

# Build DataFrame
df = pd.DataFrame([{
    "Date": item["dt_txt"],
    "Temperature": item["main"]["temp"]
} for item in forecast_list])

df.to_csv("forecast.csv", index=False)
print("Forecast data saved to forecast.csv")
