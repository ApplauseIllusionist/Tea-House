# Tea-House
https://github.com/ApplauseIllusionist/Tea-House
Class Documentation
Drink class is a class that includes all the basic traits of a drink. This is a Tea house simulator where allows you to order a drink of your choice and print out a receipt for you as a text file with all the info of the drink and price.
The name is for the type of the drink
Ice_level, sweetness is in %
Cup sizes is small, medium, and large
Toppings have a lot of items in it
get_id(self) returns the id 
get_ice_level(self) returns the ice level
get_sweetness(self) returns the sweetness
get_cup_size(self) returns the cup size
get_toppings(self) returns the toppings
Tea class is a class derived from the Drink class. While it has all the traits that were mentioned in the Drink class, it also has a tea_type so that customers can choose the type of tea they want.
get_tea_type(self) returns the tea name
Milktea class is a class derived from the Tea class as it also needs tea. In addition, It has a milk type data attribute.
get_milk_type(self) returns the type of milk used for the drink.
Fruittea class is a class derived from the Tea class as it also needs tea. In addition, it has a fruit-type data attribute.
get _fruit_type(self) returns the type of fruit added to the drink.

Demo Program Documentation
A description of the demo program: This Tea house simulator works as a shell that keep asking you to make your drink until you are done. 
You can select drink type, ice level, sweetness, cup_size, toppings, tea_type, milk_type, fruit_type. 
After you are done selecting, the program will generate a txt file called receipt as you receipt that has all the information of your drink and price.

Instructions: Just run it. Make sure to choose a drink type because it determine which class you are using to make the drink as some drink do not need milk. The instructions along with the menu are in the demo program.
