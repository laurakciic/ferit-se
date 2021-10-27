# https://www.practicepython.org/exercise/2014/01/29/01-character-input.html

# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

# Extras:
#     Add on to the previous program by asking the user for another number and printing out 
#     that many copies of the previous message. (Hint: order of operations exists in Python)

#     Print out that many copies of the previous message on separate lines. 
#     (Hint: the string "\n is the same as pressing the ENTER button)

name = input("Enter name: ")
age = int(input("Enter age: "))
repeat = int(input("Enter repetitions: "))

result = 100 - age + 2021

for x in range (repeat):
    print("\nName: " + name + "\nAge: " + str(age) + "\n" + name + " will reach 100 years in year " + str(result) + ".")