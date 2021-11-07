# we are thinking to open a small cafe with  name "Ayna's Menu", I have got an idea to make some logic for cafe menu.
# The objective is start a new bussiness for that we should have menu then frnchise, then we can start a new bussiness
# object oriendted programming practiced

#  Lets expand bussiness
class Bussiness:
    def __init__(self,name, frenchises):
        self.name = name
        self.frenchises = frenchises

# Lets build Franchises of Ayna's Menu
class Franchise:
    def __init__(self, adress, menus):
        self.adress = adress
        self.menus = menus   

# string reprsentation
    def __repr__(self):
        return self.adress   

# show the customers what thay can order in a specific time we will a methode for availble items
    def availble_items(self, time):
        availble_menus = []
        for menu in self.menus: # menu is rerfeing to class Menu
            if time >= menu.start_time and time <= menu.end_time:
                availble_menus.append(menu)
            else:
                 'menu is not availble at this time'    
        
        return  availble_menus
# create a class with name Menu
class Menu:

    # constructure when we make a constructure an object is initiated constructure refers to the object.
    def __init__(self, name, menus, start_time, end_time):
        self.name = name
        self.menus = menus
        self.start_time = start_time
        self.end_time = end_time
        # self.name etc means the object created from the constructure has name attribute = name

    #  String Representaion to our class Menu
    def __repr__(self):
        return self.name + ' is avaiable from: ' + ' '+ str(self.start_time)+'-'+ str(self.end_time)

    # Methode to calculate the bill
   
    def calculate_bill(self, purchased_items):
        bill = 0
        for purchased_item in self.menus:

            # need to check item is available or not
            if purchased_item in self.menus:
                bill = bill +  self.menus[purchased_item] # how to get value a prticular item from dictionary
            else:
                return 'item is not availble'
               
        return bill





# now lets make menu for breakfast, Lunch and dinner
breakfast_items = {
    'fried_eggs' : 7.50, 'praths'   :10.50, 'tea': 4.00, 'puro': 4.00
}   
# breakfast menu object
breakfast_menu = Menu('breakfast', breakfast_items, 700 , 900)
# Lunch Menu
lunch_items = {
    'fresh_salad': 4.00, 'butter_chicken': 10.90, 'slaman_soup': 8.00, 'potatos': 3.00, 'beef': 11.00
}
lunch_menu = Menu('Lunch', lunch_items, 1100 , 1500)


# cofee and cakes
cofee_items = {
    'cofee': 2.00, 'espresso': 3.00, 'capacinuo': 4.00, 'cake': 5.00, 'cookie': 6.00
}
cofee_menu = Menu('Cofee & snaks', cofee_items, 700 , 2200)


# Dinner Menu
dinner_items = {
    'fresh_salad': 4.00, 'chicken_soup': 10.90, 'slaman_fried': 8.00, 'mix_vege': 9.00, 'salad_buffet': 11.00
}
dinner_menu = Menu('Dinner', dinner_items, 1800 , 2200)

# asin foods menu
asianfood_menu = {
    'butter_chicken': 10.90, 'Palak_paneer': 12.00
}


# lets create tow franchise objects
menus = [breakfast_menu, lunch_menu, cofee_menu, dinner_menu]
central_store = Franchise('abc Helsnki', menus)
western_store = Franchise('xyz Espoo', menus)

# Bussiness class Objects
frenchises = [central_store, western_store]
asian_foods = Bussiness('origional Asian food', frenchises)


## Testing

# testing for string representation print(breakfast_menu)
# Testing for Calculation bill function
price = breakfast_menu.calculate_bill(['fried_eggs', 'tea', 'puro'])
print('The price is:'+' ' + str(price)+ 'Thank you!')

# test string represntation
print(central_store)

# test availble_items() menu
items = central_store.availble_items(700)
print(items)






