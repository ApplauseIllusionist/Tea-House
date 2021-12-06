# Assignment 10.1 Roman Luo
# This is a Tea house simulator where allows you to order an drink of your choice and print out a receipt for you as an txt file
#-------------------------------------------------------------------------------------

class Drink: # this will be the base class
    def __init__(self, name, ice_level, sweetness, cup_size, toppings):
        # parent class, which has the private data attributes
        self.__name = name
        self.__ice_level = ice_level
        self.__sweetness = sweetness
        self.__cup_size = cup_size
        self.__toppings = toppings

    # make a function to get each of data of a drink
    def get_id(self):
        return self.__name

    def get_ice_level(self):
        return self.__ice_level

    def get_sweetness(self):
        return self.__sweetness

    def get_cup_size(self):
        return self.__cup_size
    
    def get_toppings(self):
        return self.__toppings

class Tea(Drink): # (derived from the Drink class)
    def __init__(self, name, ice_level, sweetness, cup_size, toppings, tea_type):
        # from Drink
        super().__init__(name, ice_level, sweetness, cup_size, toppings)
        # add aother private data attribute
        self.__tea_type = tea_type

    def get_tea_type(self):
        return self.__tea_type

class MilkTea(Tea): # (derived from the Tea class)
    def __init__(self, name, ice_level, sweetness, cup_size, toppings, tea_type, milk_type):
        # from Tea
        super().__init__(name, ice_level, sweetness, cup_size, toppings, tea_type)
        # add aother private data attribute
        self.__milk_type = milk_type

    def get_milk_type(self):
        return self.__milk_type

class FruitTea(Tea): # (derived from the Tea class)
    def __init__(self, name, ice_level, sweetness, cup_size, toppings, tea_type, fruit_type):
        # from Tea
        super().__init__(name, ice_level, sweetness, cup_size, toppings, tea_type)
        # add aother private data attribute
        self.__fruit_type = fruit_type

    def get_fruit_type(self):
        return self.__fruit_type

#-------------------------------------------------------------------------------------
# define the main function
def main():

    print("-------------------------------------------------------------------------------------")
    # declare description which tells you all the commands you can use
    description = """Enter a number to select: 1. drink type, 2. ice level, 3. sweetness, 4. cup size, 
                        5. toppings, 6. tea type, 7. milk type, 8. fruit type 
                        type - done - when you finished,  - help - to see this again"""
    
    drink_type = None
    ice_level = None
    sweetness = None
    cup_size = None
    toppings = None
    tea_type = None
    milk_type = None
    fruit_type = None
    # set initial price to 0 and add things up
    price = 0
    # print out the welcome message with description
    print(f"Wellcome to Amazing Tea house. Here is the instruction for odering a drink - {description}")
    print("-------------------------------------------------------------------------------------")
    while True:

        command = input(">>> Select - ")
        # selecting a drink type - to determine the class
        if command == "1":
            drink_type = input("You can choose tea, milk tea, or fruit tea: ")
            print("-------------------------------------------------------------------------------------")
            if drink_type == "tea":
                class_type = Tea
                # initial price for tea
                price += 3
                x = class_type(drink_type, ice_level, sweetness, cup_size, toppings, tea_type)
            elif drink_type == "milk tea":
                class_type = MilkTea
                # initial price for milk tea
                price += 4
                x = class_type(drink_type, ice_level, sweetness, cup_size, toppings, tea_type, milk_type)
            elif drink_type == "fruit tea":
                class_type = FruitTea
                # initial price for fruit tea
                price += 4
                x = class_type(drink_type, ice_level, sweetness, cup_size, toppings, tea_type, fruit_type)

        # selecting a ice level
        elif command == "2":
            ice_level = input("You can choose ice level from 0 - 100%: ")
            print("-------------------------------------------------------------------------------------")
            x.get_ice_level
            if class_type == Tea:
                x = class_type(drink_type, ice_level, sweetness, cup_size, toppings, tea_type)
            if class_type == MilkTea:
                x = class_type(drink_type, ice_level, sweetness, cup_size, toppings, tea_type, milk_type)
            if class_type == FruitTea:
                x = class_type(drink_type, ice_level, sweetness, cup_size, toppings, tea_type, fruit_type)

        # selecting a sweetness
        elif command == "3":
            sweetness = input("You can choose sweetness from 0 - 100%: ")
            print("-------------------------------------------------------------------------------------")
            x.get_sweetness
            if class_type == Tea:
                x = class_type(drink_type, ice_level, sweetness, cup_size, toppings, tea_type)
            if class_type == MilkTea:
                x = class_type(drink_type, ice_level, sweetness, cup_size, toppings, tea_type, milk_type)
            if class_type == FruitTea:
                x = class_type(drink_type, ice_level, sweetness, cup_size, toppings, tea_type, fruit_type)
        
        # selecting a size
        elif command == "4":
            cup_size = input("You can choose small, medium(+$1), or large(+$2): ")
            print("-------------------------------------------------------------------------------------")
            x.get_cup_size
            if class_type == Tea:
                x = class_type(drink_type, ice_level, sweetness, cup_size, toppings, tea_type)
            if class_type == MilkTea:
                x = class_type(drink_type, ice_level, sweetness, cup_size, toppings, tea_type, milk_type)
            if class_type == FruitTea:
                x = class_type(drink_type, ice_level, sweetness, cup_size, toppings, tea_type, fruit_type)
            if cup_size == "large":
                # add $ for larger cups
                price += 2
            elif cup_size == "medium":
                price += 1

        elif command == "5":
            toppings = input("You can choose boba, putin(+$1), fruit jelly(+$1), oreo(+$1), or cheese foam(+$2): ")
            print("-------------------------------------------------------------------------------------")
            x.get_toppings
            if class_type == Tea:
                x = class_type(drink_type, ice_level, sweetness, cup_size, toppings, tea_type)
            if class_type == MilkTea:
                x = class_type(drink_type, ice_level, sweetness, cup_size, toppings, tea_type, milk_type)
            if class_type == FruitTea:
                x = class_type(drink_type, ice_level, sweetness, cup_size, toppings, tea_type, fruit_type)

            if toppings == "putin" or "fruit jelly" or "oreo":
                price += 1
            elif toppings == "cheese foam":
                price += 2
            
        elif command == "6":
            tea_type = input("You can choose black, green, taro, jasmine, rose, oolong(+$1), tieguanyin(+$1), or longjing(+$4): ")
            print("-------------------------------------------------------------------------------------")
            x.get_tea_type
            if class_type == Tea:
                x = class_type(drink_type, ice_level, sweetness, cup_size, toppings, tea_type)
            if class_type == MilkTea:
                x = class_type(drink_type, ice_level, sweetness, cup_size, toppings, tea_type, milk_type)
            if class_type == FruitTea:
                x = class_type(drink_type, ice_level, sweetness, cup_size, toppings, tea_type, fruit_type)
            
            if tea_type == "oolong " or "tieguanyin":
                price += 1
            elif tea_type == "longjing":
                price += 4

        elif command == "7":
            milk_type = input("You can choose Whole milk, almond milk or Skimmed milk: ")
            print("-------------------------------------------------------------------------------------")
            if class_type == Tea:
                print("This option is unavailable for your drink")
            if class_type == MilkTea:
                x = class_type(drink_type, ice_level, sweetness, cup_size, toppings, tea_type, milk_type)
            if class_type == FruitTea:
                print("This option is unavailable for your drink")

        elif command == "8":
            fruit_type = input("You can choose apple, banana, passion fruit, mango, strawberry, \ncoconut meat, pear, watermelon, blueberry, or pineapple:")
            print("-------------------------------------------------------------------------------------")
            if class_type == Tea:
                print("This option is unavailable for your drink")
            if class_type == MilkTea:
                print("This option is unavailable for your drink")
            if class_type == FruitTea:
                x = class_type(drink_type, ice_level, sweetness, cup_size, toppings, tea_type, fruit_type)

        elif command == "help":
            print(f"{description}\n")
            print("-------------------------------------------------------------------------------------")
            # print description decleared above
        elif command == "done":
            # exiting
            break
        else:
            print("Option unavailable")
        #tells user if they have wrong input
    print("Thank you!")
                                                                                 
    filename = "receipt.txt"
    with open(filename, "w") as f:
        if class_type == Tea:
            f.write(f"-----Amazing Tea House\n")
            f.write(f"-----      receipt\n")
            f.write(f"-----Item type: {x.get_id()}\n")
            f.write(f"-----Ice level: {x.get_ice_level()}%\n")
            f.write(f"-----Sweetness: {x.get_sweetness()}%\n")
            f.write(f"-----Cup size: {x.get_cup_size()}\n")
            f.write(f"-----Toppings: {x.get_toppings()}\n")
            f.write(f"-----Tea type: {x.get_tea_type()}\n")
            f.write(f"-----Totol price: ${price}\n")
            f.write(f"-----Thank you for shopping with us\n")
        elif class_type == MilkTea:
            f.write(f"-----Amazing Tea House\n")
            f.write(f"-----receipt\n")
            f.write(f"-----Item type: {x.get_id()}\n")
            f.write(f"-----Ice level: {x.get_ice_level()}%\n")
            f.write(f"-----Sweetness: {x.get_sweetness()}%\n")
            f.write(f"-----Cup size: {x.get_cup_size()}\n")
            f.write(f"-----Toppings: {x.get_toppings()}\n")
            f.write(f"-----Tea type: {x.get_tea_type()}\n")
            f.write(f"-----Milk type: {x.get_milk_type()}\n")
            f.write(f"-----Totol price: ${price}\n")
            f.write(f"-----Thank you for shopping with us\n")
        elif class_type == FruitTea:
            f.write(f"-----Amazing Tea House\n")
            f.write(f"-----receipt\n")
            f.write(f"-----Item type: {x.get_id()}\n")
            f.write(f"-----Ice level: {x.get_ice_level()}%\n")
            f.write(f"-----Sweetness: {x.get_sweetness()}%\n")
            f.write(f"-----Cup size: {x.get_cup_size()}\n")
            f.write(f"-----Toppings: {x.get_toppings()}\n")
            f.write(f"-----Tea type: {x.get_tea_type()}\n")
            f.write(f"-----Fruit type: {x.get_fruit_type()}\n")
            f.write(f"-----Totol price: ${price}\n")
            f.write(f"-----Thank you for shopping with us\n")
            

# Call the main function
if __name__ == "__main__":
    main()

        
