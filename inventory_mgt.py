#Inventory management
#1.Add item
#2.View  current inventory
#3.Delete item
#4.Exit inventory

#Start with an empty inventory
inventory = {}

print("Welcome to Inventory Management")
while True:
    print("\nChoose on the following options to continue(1-4)")
    print("1.Add new item")
    print("2.View current inventory")
    print("3.Delete an item")
    print("4.Exit")
    
    option = int(input("Enter Option."))
    if option == 1:
        item_name = input("Enter the item name: ").lower()
        item_Id =input("Enter the item Id: ")
        quantity = input("Enter the Quantity: ")
        price = input("Enter the unit price: ")
        
        if not quantity.isdigit() or int(quantity) <= 0:
            print("Invalid quantity, enter a positive number")
            continue
            
        if not price.isdigit()  or int(price) <= 0:
            print("Invalid price, Enter a digit price greater than zero") 
            continue
            
        quantity = int(quantity)   
        price = int(price) 
             
             #check if item already exists in inventory
        if item_name in inventory:
            inventory[item_name] ["quantity"]   += quantity
            print(f"Updated item {item_name} : Quantity increased by {quantity} kg")
        else:
            inventory[item_name]  ={
                "id": item_Id,
                "quantity": quantity,
                "price": price
            }  
            print(f"Added {item_name} with Id {item_Id} at shs{price} each , quantity: {quantity}kg")
    elif option == 2: 
        if not inventory :
            print("Inventory empty")  
        else:
            print("\n Current Inventory")
            for item, details in inventory.items():
                print(f" Name: {item} | ID: {details['id']} | Quantity:{details['quantity']} | Price: shs.{details['price']}")            
    elif option == 3:
        item_name = input("Enter item name to remove: ").lower()  
        
        if item_name  not in inventory:
            print("Item not found in inventory")  
            continue
        del inventory[item_name]     
        print(f"Removed '{item_name}' from inventory.")   
    elif option == 4:
        print("Exiting inventory system. Good bye!")   
        break
    else:
        print("Invalid option! Enter a number btn 1 and 4")   
            
            
        
                
            
                
        
        
        

         
         
         
         
         