# defining variables and Printing strings

v = "Isn't that nice?"
print("Our variable has a value which is string-type content.", v)

# counting variables

num1 = 1000
num2 = 24
num3 = num1 + num2 + 15
num3_exp = num3 ** 2
print("The final results of the calculation was:", num3_exp)

# Type Conversion and F String

a = 10.6411
b = "Stringing!"
c = int(10.6411)
d = b * 2
# fstring to combine different data types in a string
print(f'Integer conversion cannot do roundings: {c}  Multiplying strings also causes trouble: {d}')

# Layout characters Predefined String

print("""This here is divided to several lines:\n I am still in the same print-command.\n
      \t\t\t Name:\t\tPeter\n
      \t\t\t job:\t\tbabysitter""")

# take Input from  users

num1 = int(input("Give the first number:"))
num2 = int(input("Give the second number:"))
t_sum = num1 + num2
print(f"The result is: {t_sum}")

# String Slices

v = "desserts"
length = len("desserts")
a = v[0:4]
b = v[4:length + 1]
s = a + b
ls = len(s)
reverseString = s[ls::-1]  # slicing
# The slice statement means start at string length, end at position 0, move with the step -1 (or one step backward).
print(reverseString)


