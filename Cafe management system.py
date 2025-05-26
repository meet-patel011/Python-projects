#Create the menu of the cafe
menu = {
    "Pizza":120,
    "Burger":50,
    "Coffee":80,
    "French fries":60,
    "Pasta":65 
}
#Greet
print("Welcome to our Cafe")
print("Here the menu\nPizza: Rs120\nBurger: Rs50\nCoffee: Rs80\nFrench fries: Rs60\nPasta: Rs65")

order_total = 0

item1 = input("Enter the name of item you want to order: ")
if item1 in menu:
    order_total += menu[item1]
    print("Your item is added to your order")

else:
    print("Please order something that is in our menu")

another_order = input("Do you want to order another item (yes/no)? ")
if (another_order == "yes"):
    item2 = input("Enter the name of another item: ")
    if item2 in menu:
        order_total += menu[item2]
else:
    print("Please order something that is in our menu")

print("The total price for your order is: ",order_total)     