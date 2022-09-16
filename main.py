import requests
import smtplib

api_key = "your_open_weather_apikey"
sender = "sender_email"
password = "sender_email_password"
receiver = "receiver_email"

p = {
    "lat": 22.9908,
    "lon": 120.2133,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

response = requests.get(
    url="https://api.openweathermap.org/data/2.5/onecall", params=p)
response.raise_for_status()
data = response.json()
print(data)

data_12h = data["hourly"][:12]
weather_12h = [item["weather"] for item in data_12h]
weather_code = []

rain = False

for item in weather_12h:
    for d in item:
        weather_code.append(d["id"])
        if d["id"] < 700:
            rain = True

print(weather_code)

if rain:
    print("Bring an umbrella!")

    with smtplib.SMTP("smtp.gmail.com") as connect:
        connect.starttls()
        connect.login(user=sender, password=password)
        connect.sendmail(from_addr=sender,
                         to_addrs=receiver,
                         msg=f"Subject:Bring an umbrella!\n\nHave a nice day.")