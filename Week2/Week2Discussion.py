# Daniel Sterling
# October 14, 2024
# Week 2 Discussion

# Ineffective Method
fav_number = input("Enter your favorite number: ") # User can enter a non-integer value (letters)
print(f"Your favorite number is {fav_number}")  # If user enters letters, this could cause logical issues

# Effective method
while True:
    try:
        fav_number = int(input("Enter your favorite number (in numerical characters): ")) # Prompt is clear and concise
        break
    except ValueError:
        print("Please enter a number") # Informs user that a number is required to move on

print(f"Your favorite number is {fav_number}") # Safe to proceed with numerical value