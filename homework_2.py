hotel_rooms = {
    "101": {
        "status": "available",
        "customer": ""
        },
    "102": {
        "status": "booked",
        "customer": "John Doe"
        }
}

def book_room(roomnumber, customername): 
    if hotel_rooms[roomnumber]["status"] == "available":
        hotel_rooms[roomnumber]["status"] = "booked"
        hotel_rooms[roomnumber]["customer"] = customername    

def check_out(roomnumber):
    if hotel_rooms[roomnumber]["status"] == "booked":
        hotel_rooms[roomnumber]["status"] = "available"
        hotel_rooms[roomnumber]["customer"] = ""
        
def print_status():
    for room, status in hotel_rooms.items():
        if status["status"] == "available":
            print(f"Room {room} is {status['status']}")
        else:
            print(f"Room {room} is {status['status']} and is booked by {status['customer']}")
        
book_room("101", "Jane Doe")
check_out("102")
print_status()
print("----")
check_out("101")
book_room("102", "Yasuo")
print_status()
print()

#2 

products = {
    "1": {"name": "Laptop", 
          "category": "Electronics", 
          "price": 800},
    "2": {"name": "Shirt", 
          "category": "Clothing", 
          "price": 20}
}


def search_products(name):
    for product in products.values():
        if product["name"] == name:
            print(f"{product['name']} is in the {product['category']} category and costs ${product['price']}")
            
    print(f"{name} not found in the products list")
            
search_products("Laptops")
