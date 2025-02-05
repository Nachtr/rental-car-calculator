#!/usr/bin/python3
# Author: Danny Whitaker
# Date: 2/4/25
# Version 1.1

"""
The task is to create a Python script that calculates the total cost of a car rental based on the number of days
the car is rented and the daily rental price.

The script should prompt the user to enter the necessary information and display the calculated total cost using an
f-string.Additionally, the company offers a special weekend promotion where the rental price is discounted by 10% for
rentals that include a Saturday or Sunday
"""

# vehicle prices
vehicle_price = {
    "SEDAN": 48,
    "SUV": 64,
    "TRUCK": 80,
    "SPORTSCAR": 130
}

# Days of the week to numerical value
days_of_week = {
    "MONDAY": 1,
    "TUESDAY": 2,
    "WEDNESDAY": 3,
    "THURSDAY": 4,
    "FRIDAY": 5,
    "SATURDAY": 6,
    "SUNDAY": 7
}

# Function loop to check if the rental period includes a weekend or not!
def includes_weekend(start_day, rental_days):
    start_index = days_of_week[start_day]
    for i in range(rental_days): # start loop
        current_day_index = (start_index + i - 1) % 7 + 1
        if current_day_index in [6, 7]:
            return True
    return False

# Type of vehicle
type_of_vehicle = input("What type of vehicle do you want to rent? (SUV, SEDAN, TRUCK, SPORTSCAR) ").upper()
while type_of_vehicle not in vehicle_price:
    print("Please select from our vehicles...")
    type_of_vehicle = input("What type of vehicle do you want to rent? (SUV, SEDAN, TRUCK, SPORTSCAR) ")

# Start day
start_day = input("What day would you like to start renting our vehicle? ").upper()
while start_day not in days_of_week:
    print("That day does not exist, please try again")
    start_day = input("What day would you like to start renting our vehicle? ")

# Rental days
rental_days = input("How long would you like to rent our vehicle for? ")
while not rental_days.isdigit() or int(rental_days) <= 0:
    print("That is an invalid input, please try again!")
    rental_days = input("How long would you like to rent our vehicle for? ")
rental_days = int(rental_days)

# Total cost
daily_rate = vehicle_price[type_of_vehicle]
total_cost = rental_days * daily_rate

# Does it include the weekend?
if includes_weekend(start_day,rental_days):
    total_cost *= 0.9

print(f"Your total rental cost for an {type_of_vehicle} for {rental_days} days is {total_cost}")