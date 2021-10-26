# Conditional Structures if-elif-else

# Exercise 1

num = int(input("Give a number:"))
if num % 2 == 0:
    print("The given number was even")

# Exercise 2

name = "John"
password = "ABC123"
pass1 = ""
g_name = input("Give name:")
if name == g_name:
    pass1 = input("Give password:")
    if pass1 != password:
        print("The password is incorrect.")
    else:
        print("Both inputs are correct!")
else:
    print("The given name is wrong.")

# Exercise 3

num = int(input("Select a number (1-3):"))
if num == 1:
    print("You selected one.")
elif num == 2:
    print("You selected two.")
else:
    print("You selected three.")

# Exercise 4

num1 = int(input("Give a number:"))
num2 = int(input("Give another number:"))
if (num1 % 2 == 0) and (num2 % 2 == 0):
    print("Both numbers are even.")
elif (num1 % 2 == 0) and (num2 % 2 != 0):
    print("One of the numbers is even")
elif (num1 % 2 != 0) and (num2 % 2 == 0):
    print("One of the numbers is even")
else:
    print("Both numbers are odd.")

# Exercise 5

print("Calculator")
num1 = int(input("Give the first number:"))
num2 = int(input("Give the second number:"))
print("""(1) + \n(2) - \n(3) *\n(4) /""")
s_num = int(input("Please select something (1-4):"))
if s_num == 1:
    result = num1 + num2
    print(f'The result is {result}')
elif s_num == 2:
    result = num1 - num2
    print(f'The result is {result}')
elif s_num == 3:
    result = num1 * num2
    print(f'The result is {result}')
elif s_num == 4:
    result = num1 / num2
    print(f'The result is {result}')
else:
    print("Selection was not correct.")
