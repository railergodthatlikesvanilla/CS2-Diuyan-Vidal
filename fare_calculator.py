# Travel Fare Calculator
import math
FARE_RATE = 14
while True:
    name = input("Enter passenger name: ")

    if name.strip() != "":
        break
    else:
        print("Invalid name. Passenger name cannot be empty.")
while True:
    distance = float(input("Enter distance (km): "))
    
    if distance and 0 <= int(distance) <= math.inf:
        distance = int(distance)
        break
    else:
        print("Invalid distance. Distance must be greater than 0")
while True:
    passengers = int(input("Enter number of passengers: "))
    
    if passengers and 0 <= int(passengers) <= math.inf:
        passengers = int(passengers)
        break
    else:
        print("Invalid passengers. Passengers must be any positive whole number")

total_fare = distance * FARE_RATE * passengers

print("\nPassenger:", name)
print("Total Fare: PHP", round(total_fare, 2))
# Validation rules
# 1. Passenger name -- Must not be empty
# 2. Distance -- Number greater than 0
# 3. Passengers -- Positive whole number
