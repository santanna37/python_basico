# - Create a distance converter converting Km to miles
# - Take two inputs from user: Their first name and the distance in km
# - Print: Greet user by name and show km, and mile values
# - 1 mile is 1.609 kilometers
# - hint: use correct types for calculating and print
# - Did you capitalize the name

user = input("what's your name? ")
distance = float(input("what's distance?: "))
converter = float(distance / 1.609)

print(f"Greet user by {user.capitalize()} and show km {distance}, and mile values {converter}")

