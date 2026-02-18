# Rain-Alert
DAY - 35/100 Project - python X Rain Alert

# 🌧️ Weather Alert Automation (Python + OpenWeather API + Twilio)

## 📌 Project Description

This project is a **Weather Alert Automation System** built using Python.

The program:

* Gets weather forecast data from **OpenWeather API**
* Checks if rain is expected in the next few hours
* Automatically sends alerts via:

  * 📩 SMS
  * 📱 WhatsApp (Twilio Sandbox)

This project was created during **Day 35 — 100 Days of Code (Angela Yu Bootcamp)** and upgraded with extra messaging features.

---

## 🚀 Features

✔ Real API integration
✔ Weather forecast checking (next 12 hours)
✔ Rain detection using weather condition codes
✔ SMS alert system
✔ WhatsApp alert system
✔ Automation logic using Python

---

## 🧠 Project Workflow

```
Get Weather Data
        ↓
Check forecast (next 4 blocks = 12 hrs)
        ↓
If Rain Found
        ↓
Send SMS + WhatsApp Alert
```

---

## 🛠️ Technologies Used

* Python
* Requests library
* OpenWeather API
* Twilio API
* WhatsApp Sandbox
* REST APIs
* JSON Data Handling

---

# 🔑 HOW TO GET API KEYS (STEP BY STEP)

---

## 🌦️ OpenWeather API Setup

### Step 1 — Create Account

Go to:

```
https://openweathermap.org/api
```

Sign up using email.

---

### Step 2 — Generate API Key

After login:

```
Dashboard → API Keys
```

You will see:

```
Your API Key
```

Copy it.

⚠️ Sometimes activation takes 10–15 minutes.

---

### Step 3 — Test API Key (Browser Test)

Paste in browser:

```
https://api.openweathermap.org/data/2.5/forecast?q=London&appid=YOUR_API_KEY
```

If you see:

```
"cod":"200"
```

then API works.

---

## 📱 Twilio API Setup

### Step 1 — Create Twilio Account

Go to:

```
https://www.twilio.com
```

Create a free trial account.

---

### Step 2 — Choose Setup Options

During onboarding select:

```
With Code
Notifications
SMS
```

---

### Step 3 — Get Twilio Credentials

Open:

```
Twilio Console Dashboard
```

You will see:

```
Account SID
Auth Token
```

These are your API credentials.

Example:

```
ACxxxxxxxxxxxxxxxxxxxxx
```

---

### Step 4 — Get Twilio SMS Number

Go to:

```
Phone Numbers → Manage → Active Numbers
```

Copy your Twilio number.

Example:

```
+1XXXXXXXXXX
```

---

## 📲 WhatsApp Sandbox Setup (Twilio)

Twilio trial accounts use WhatsApp Sandbox.

### Step 1 — Open Sandbox

```
Messaging → Try it out → WhatsApp Sandbox
```

---

### Step 2 — Join Sandbox

On your phone:

Open WhatsApp → send message:

```
join <your-code>
```

to:

```
+XXXXXXXXXXX
```

You will receive confirmation:

```
You have joined the sandbox
```

---

### Step 3 — WhatsApp Code Format

Use:

```
from_="whatsapp:+XXXXXXXXXXX"
to="whatsapp:+91XXXXXXXXXX"
```

---

## ⚙️ Installation

Clone repository:

```bash
git clone https://github.com/guptaji0358/Rain-Alert.git
```

Install dependencies:

```bash
pip install requests
pip install twilio
```

---

## ▶️ Run Program

```bash
python weather_alert.py
```

---

## 📂 Project Structure

```
weather-alert/
│
├── weather_alert.py
├── README.md
```

---

## 📩 Example Alert

```
☔ Rain alert! Take your umbrella.
```

---

## 👨‍💻 Author

**Robin Gupta**

Part of:

```
#100DaysOfCode
```

---

## ⭐ Learning Outcomes

* Working with APIs
* Handling JSON data
* Automation using Python
* SMS & WhatsApp APIs
* Real-world project structure

---

## 📜 License

Open-source project for learning purposes.
