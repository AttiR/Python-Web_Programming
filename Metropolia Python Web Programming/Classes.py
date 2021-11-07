# Class

class Car:
    pass

# Instantiation (Carete instance of a class)
car_1 = Car() # careted an object by adding parenthesis and assigned this instance to varibale
car_1_type =(type(car_1))
print(car_1_type)

# Object Oriendted Programming
# Class Variables

class Grade:
  minimum_passing = 65 # class attribute / class varibale

# Methods

class Car:
    car_color = "black" 

    def car_spec(self): # methode car_spec that take one argument as self which refers to the object created
        print('Car colour is {}' .format(self.car_color))

honda = Car()   
honda.car_spec()


# Methods and Arguments
class Circle:
  pi = 3.14
  
  def area(self, radius):
    return self.pi * radius ** 2
  
circle = Circle()
pizza_area = circle.area(12 / 2)
teaching_table_area = circle.area(36 / 2)
round_room_area = circle.area(11460 / 2)

# Constructors
class Circle:
  pi = 3.14
  
  # constructor 
  def __init__(self, diameter):
    print("New circle with diameter: {diameter}".format(diameter=diameter))
    
teaching_table = Circle(36)

# Instance Variables
class Store:
  pass
alternative_rocks = Store()
isabelles_ices = Store()

alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

class Sum:
  def __init__(self, num1, num2):
      self.num1=num1
      self.num2=num2

  def add(self):
    return self.num1 +  self.num2

result = Sum(2,3)  
print(result.add())



