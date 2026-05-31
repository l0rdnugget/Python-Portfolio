# ---- TEMPERATURE VALIDATION ----

while True:
    try:
        temperature = float(input("What\'s the current temperature? "))
        if temperature < -60 or temperature > 140:
            print("If it\'s that hot or cold, you have more things to worry about than what to wear. Try again!")
        else:
            break  # valid! exit the loop
    except ValueError:
        print("Oops! Please enter a number like 72 or 30.5")


# ---- WEATHER TYPE VALIDATION ----

valid_types = ["sunny", "rainy", "snowy", "cloudy", "windy", "stormy"]
while True:
    try:
        weather_type = input("What\'s the weather like? (sunny, rainy, snowy, cloudy, windy, stormy) ").lower()
        if weather_type not in valid_types:
            print("Please choose from: sunny, rainy, snowy, cloudy, windy, or stormy")
        else:
            break  # valid! exit the loop
    except ValueError:
        print("That doesn\'t sound quite right. Is it rainy, sunny, or cloudy?")


# ---- WIND SPEED VALIDATION ----

while True:
    try:
        wind_speed = float(input("What\'s the wind speed? Estimates are cool too! "))
        if wind_speed < 0:
            print("Wind speed can\'t be negative! Try again.")
        else:
            break  # valid! exit the loop
    except ValueError:
        print("Oops! Please enter a number like 10 or 20.5")


# ----OUTFIT SUGGESTIONS ----

if temperature < 32:
    outfit = "Arcteryx, gloves, or book a flight to Mexico"
elif weather_type == "snowy":
    outfit = "Grab your snow boots and call off work"
elif weather_type == "rainy" and temperature > 45:
    outfit = "Raincoat, dress like you\'re in the PNW, grab an iced coffee"
elif weather_type == "windy":
    outfit = "The 80s called, they want you to grab your fave windbreaker"
elif temperature < 65:
    outfit = "Light jacket and New Balances"
else:
    outfit = "Sandals and shorts"


# ----EMOJI SELECTION ----

if temperature < 32:
    emoji = "❄️"
elif weather_type == "snowy":
    emoji = "🌨️"
elif weather_type == "rainy" and temperature > 45:
    emoji = "🌧️"
elif weather_type == "windy":
    emoji = "🌬️"
elif temperature < 65:
    emoji = "🍂"
else:
    emoji = "☀️"


# ---- DISPLAY RESULTS + SIGN OFF ----

print(f"{emoji} - - - - - - - - - - - - - - {emoji}")
print("     MARI'S OUTFIT ADVISOR")
print(f"{emoji} - - - - - - - - - - - - - - {emoji}")
print(f"🌡️  Temp        : {temperature}°F")
print(f"🌤️  Weather     : {weather_type}")
print(f"💨  Wind        : {wind_speed} mph")
print(f"👗  Today\'s Fit : {outfit}")
print(f"{emoji} - - - - - - - - - - - - - - {emoji}")
print("Have a good day. See you tomorrow!")

