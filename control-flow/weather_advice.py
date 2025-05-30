#Python script to recommend clothing recommendation based on the weather

#prompt User for Weather Input
weather = input("What's the weather like today? (sunny/rainy/cold): \n").lower()

#recommend clothing based on weather
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.\n")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.\n")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.\n")
else:
    print("Sorry, I don't have recommendations for this weather.\n")
