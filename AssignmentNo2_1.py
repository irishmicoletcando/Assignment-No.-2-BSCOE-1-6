# Create a program that will ask how many apples and oranges you want to buy.
# Display the total amount you need to pay if apple price is 20 pesos and orange is 25.
# Display the output in the following format.
# The total amount is ______.

appleQuestion = int(input("How many apples do you want to buy? "))
orangeQuestion = int(input("How many oranges do you want to buy?"))

applePrice = 20
orangePrice = 25

appleTotal = appleQuestion * applePrice
orangeTotal = orangeQuestion * orangePrice
total = appleTotal + orangeTotal
