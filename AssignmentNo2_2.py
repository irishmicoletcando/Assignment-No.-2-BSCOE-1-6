# Create a program that will ask for name, age and address. 
# Display those details in the following format.
# Hi, my name is _____. I am ____ years old and I live in _____ .

name = input("Enter your name: ")
age = int(input("Enter your age: "))
address = input("Enter your address: ")

print(f"Hi, my name is {name}. I am {age} years old and I live in {address}.")