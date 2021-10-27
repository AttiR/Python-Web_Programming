# Data Structures  LISTS
orders = ["daisy", "buttercup", "snapdragon", "gardenia", "lily"]
items_sold = ["cake", "cookie", "bread"]
items_sold_new = items_sold + ["biscuit", "tart"] #cancantenation
print(items_sold_new)

# Accessing Lists Elements
employees = ["Michael", "Dwight", "Jim", "Pam", "Ryan", "Andy", "Robert"]
employee_four = (employees[3])
print(employees[4])

# Accessing List Elements: Negative Index

shopping_list = ["eggs", "butter", "milk", "cucumbers", "juice", "cereal"]
last_element = (shopping_list[-1])
index5_element = (shopping_list[5])
print(last_element)
print(index5_element)

# Modifying List Elements
garden_waitlist = ["jiho", "Adam", "Sonny", "Alisha"]
garden_waitlist[1] = "Calla"
print(garden_waitlist)
garden_waitlist[-1] = "Alex"
print(garden_waitlist)

# Shrinking a List: Remove

order_list = ["Celery", "Orange Juice", "Orange", "Flatbread"]
print(order_list)
order_list.remove("Flatbread")
print(order_list)
new_store_order_list = ["Orange", "Apple", "Mango", "Broccoli", "Mango"]
print(new_store_order_list)
new_store_order_list.remove("Mango")
print(new_store_order_list)

# Two-Dimensional (2D) Lists

heights = [["Jenny", 61], ["Alexus", 70], ["Sam", 67], ["Grace", 64]]
heights.append(["Vik", 68])
ages = [["Aaron", 15], ["Dhruti", 16]]

# Accessing 2D Lists

class_name_test = [["Jenny", 90], ["Alexus", 85.5], ["Sam", 83], ["Ellie", 101.5]]
print(class_name_test)
sams_score = class_name_test[2][1]
print(sams_score)
ellies_score = class_name_test[-1][-1]
print(ellies_score)


