import requests
from twilio.rest import Client

#SMS API
Account_SID = "ENTER YOUR ACCOUNT SID"
Auth_tokens = "ENTER YOUR Auth Tokens"

#Weather API
API_KEY = "ENTER YOUR API KEY"
URL = "https://api.openweathermap.org/data/2.5/forecast"


weather_param = {
    "lat": 26.203725,
    "lon": 78.157363,
    "appid": API_KEY,
    "units": "metric",
    "cnt": 4        # next 12 hours
}

# ---------- GET WEATHER ---------- #
response = requests.get(URL, params=weather_param)
response.raise_for_status()

weather_details = response.json()

will_rain = False

# ---------- CHECK RAIN ---------- #
for hour_data in weather_details["list"]:
    condition_code = hour_data["weather"][0]["id"]
    if condition_code < 700:
        will_rain = True
        break

# ---------- SEND ALERT ---------- #
if will_rain:

    client = Client(Account_SID, Auth_tokens)

    # ----- SMS ----- #
    client.messages.create(
        body="☔ Rain alert! Take your umbrella.",
        from_="+XXXXXXXXXXX",
        to="+91XXXXXXXXXX"
    )

    # ----- WHATSAPP ----- #
    client.messages.create(
        body="☔ Rain alert! Take your umbrella.",
        from_="whatsapp:+XXXXXXXXXXX",
        to="whatsapp:+91XXXXXXXXXX"
    )

    print("SMS + WhatsApp sent ✅")

else:
    print("No rain today 🌤️")
