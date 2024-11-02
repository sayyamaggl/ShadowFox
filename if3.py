countries = {
    "Australia": ["Sydney", "Melbourne", "Brisbane", "Perth"],
    "UAE": ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"],
    "India": ["Mumbai", "Bangalore", "Chennai", "Delhi"]
}


def find_country(city):
    for country, cities in countries.items():
        if city in cities:
            return country
    return None


city1 = input("Enter the first city name: ")
city2 = input("Enter the second city name: ")


country1 = find_country(city1)
country2 = find_country(city2)


if country1 and country2:
    if country1 == country2:
        print(f"{city1} and {city2} belong to the same country: {country1}")
    else:
        print(f"{city1} and {city2} do not belong to the same country")