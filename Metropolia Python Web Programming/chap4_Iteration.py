# Exercise 1

i = 0
while i < 5:
    print(f'This is lap {i}')
    i += 1

# Exercise 2

keep_printing = True
while keep_printing:
    v = input("Write Something:")
    if v == "quit":
        print("Bye bye!")
        keep_printing = False
    else:
        print(v)

# Exercise 3

number = int(input("Give a number:"))
sum1 = 0
for i in range(0, number):
    sum1 += i
print(f"The sum was: {sum1}")

# Exercise 4
keep = True
print("Calculator")
num1 = int(input("Give the first number:"))
num2 = int(input("Give the second number:"))
while keep:

    print("""(1) + \n(2) - \n(3) *\n(4) /\n(5) Change numbers\n(6) Quit""")
    print(f'Current numbers:{num1}  {num2}')
    s_num = int(input("Please select something (1-6):"))
    if s_num == 6:
        print("Thank you")
        keep = False
    elif s_num == 5:
        num1 = int(input("Give the first number:"))
        num2 = int(input("Give the second number:"))
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


