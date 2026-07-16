Name = input("What's your name?")
print(f"Hi {Name}, let's learn the months of the year!")
months_and_seasons = {
    "January": "🌨️❄️ Winter",
    "February": "🌨️❄️ Winter",
    "March": "🌧️🌱 Spring",
    "April": "🌧️🌱 Spring",
    "May": "🌧️🌱 Spring",
    "June": "⛱️☀️ Summer",
    "July": "⛱️☀️ Summer",
    "August": "⛱️☀️ Summer",
    "September": "🍁🍂 Autumn",
    "October": "🍁🍂 Autumn",
    "November": "🍁🍂 Autumn",
    "December": "🌨️❄️ Winter"
}

print("🌍 Months and Their Seasons")
print("---------------------------")

for month, season in months_and_seasons.items():
    print(f"{month} → {season}")