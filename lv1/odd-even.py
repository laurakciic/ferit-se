# https://www.practicepython.org/exercise/2014/02/05/02-odd-or-even.html

# Ask the user for a number. 
# Depending on whether the number is even or odd, print out an appropriate message to the user. 
# Hint: how does an even / odd number react differently when divided by 2?

# Extras:
#     If the number is a multiple of 4, print out a different message.

num = int(input("Enter first number: "))

if num % 4 == 0:
    print("Given number is a multiple of 4.")
elif num % 2 == 0:
    print("Given number is even.")
else:
    print("Given number is odd.")