restaurant_menu = {
    "Starters": {"Soup": 5.99, "Bruschetta": 6.50},
    "Main Course": {"Steak": 15.99, "Salmon": 13.99},
    "Desserts": {"Cake": 4.99, "Ice Cream": 3.99}
}

restaurant_menu.update({"Drinks": {"Water": 1.00, "Wine": 5.00}})
restaurant_menu["Main Course"]["Steak"] = 17.99

for i in restaurant_menu.items():
    print(i)