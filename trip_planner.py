#travel planner program
#this program helps organize your trip itinerary

print("Welcome to Trip Planner!")
print("Let's plan your next adventure!\n")

#first destination!
city1 = input("Where's your First stop? Enter the city: ")
country1 = input("What country is it in? ")
duration1 = int(input("How many days are you staying? "))
budget1 = int(input("What's your budget in usd? "))

#second destination!
city2 = input("Where's your Second stop? Enter the city: ")
country2 = input("What country is it in? ")
duration2 = int(input("How many days are you staying? "))
budget2 = int(input("What's your budget in usd? "))

#third destination!
city3 = input("Where's your Final stop? Enter the city: ")
country3 = input("What country is it in? ")
duration3 = int(input("How many days are you staying? "))
budget3 = int(input("What's your budget in usd? "))

#store in dictionary of lists
itinerary = {
    "city": [city1, city2, city3],
    "country": [country1, country2, country3],
    "duration": [duration1, duration2, duration3],
    "budget": [budget1, budget2, budget3]
}

#display results
print("Here's your Complete Travel Itinerary!\n")

for i in range(3):
    print(f"\nCity: {itinerary['city'][i]}")
    print(f"Country: {itinerary['country'][i]}")
    print(f"Duration of Stay: {itinerary['duration'][i]} days")
    print(f"Budget: ${itinerary['budget'][i]}")


input("Press Enter to finish your adventure...")
