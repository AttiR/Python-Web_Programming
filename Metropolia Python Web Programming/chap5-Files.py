# File Open and Read

readfile = open("facts.txt", "r")
content = readfile.readlines()
print(content)

for i in content:
    print(i)
readfile.close()

# Writing to a File

file = input("Give file a name:")
text = input("Write something:")
x_file = open("file", "w")
x_file.write(text)
x_file.close()

my_file = open("file", "r")
content = my_file.readline()
print(content)


