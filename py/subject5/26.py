weather = input("is it sunny or raining?: ")
temperature= input("Is it cold or warm?: ")

if weather == "raining" and temperature == "cold":
    print("take an umbrella and a warm jacket.")
elif weather == "raining" and temperature == "warm":
    print("take an umbrella and a t-shirt.")
elif weather == "sunny" and temperature == "cold":
    print("take sunglasses and a warm jacket.")
elif weather == "sunny" and temperature == "warm":
    print("take sunglasses and a t-shirt.")
else:
    print("stay home!")

