# Daniel Sterling
# October 19, 2024
# Week 3 Assignment 3: Programming Assignment

# Input user age
age = int(input("Enter your age in numbers:\n"))

# Input time of the movie
time = int(input("Enter the time of the movie in 24 hour format (ex: 14 = 2pm):\n"))

# Determine base ticket price on age
if age < 12:
    ticket_price = 5
elif age >= 55:
    ticket_price = 7
else:
    ticket_price = 10

# Apply discount if the movie is before 5pm (17:00)
if time < 17:
    ticket_price -= 2

# Display final ticket price
print(f"The final cost of your ticket is: ${ticket_price}")