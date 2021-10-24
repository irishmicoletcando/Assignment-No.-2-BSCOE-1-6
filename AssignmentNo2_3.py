# Create a program which you will enter the amount of money you have, it will also ask for the price of an apple.
# Display the maximum number of apples that you can buy and the remaining money that you will have.
# Display the output in the following format.
# You can buy ___ apples and your change is ___ pesos.

money = float(input("How much money do you have? "))
apple = float(input("What is the price of an apple per piece? "))

# maximum number of apples
maxNumberApples = int(money // apple)
# remaining money
change = money % apple
print(f"You can buy {maxNumberApples} apples and your change is {change: .2f} pesos.")
# Program completed
