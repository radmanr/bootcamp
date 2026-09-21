#unit converter for km to miles and Celcius to Fahrenheit 
km = float(input("Enter the distance in Km: "))
miles = round(km * 0.621371, 2)
print(f"{km} equals to {miles} miles.")
c = float(input("Enter the temperature in C: "))
f = (c * 9/5) + 32
print(f"{c} degrees C equals to {f} degrees F.")
