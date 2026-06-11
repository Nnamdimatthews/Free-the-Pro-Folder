print("Welcome to pygo's calculator!")
name = input("What is your name? ")
print(f"Hello, {name}! Let's do some maths.")

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))
problem1 = print(f"That's great, {name}! Let's perform the calculations with {num1} and {num2}.")
print(f"The Addition of {num1} and {num2} is: {num1 + num2}")
print(f"The Subtraction of {num1} and {num2} is: {num1 - num2}") 
print(f"The Multiplication of {num1} and {num2} is: {num1 * num2}")
if num2 != 0:
    print(f"The Division of {num1} and {num2} is: {num1 / num2}")

Continue = input("Do you want to perform more calculations? (yes/no) ")

if Continue.lower() == "yes":
    num3 = int(input("Enter the third number: "))
    num4 = int(input("Enter the fourth number: "))
problem2 = print(f"That's great, {name}! Let's perform the calculations with {num3} and {num4}.")
print(f"The Addition of {num3} and {num4} is: {num3 + num4}")
print(f"The Subtraction of {num3} and {num4} is: {num3 - num4}") 
print(f"The Multiplication of {num3} and {num4} is: {num3 * num4}")
if num4 != 0:
    print(f"The Division of {num3} and {num4} is: {num3 / num4}")
elif Continue.lower() == "no":
    print("Thank you for using the calculator!, " + name + "! Have a great day(Check out pygo for more fun projects)!")