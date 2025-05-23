class InventorySystem:
    def __init__(self):
        self.inventory = {}
        self.load_inventory()
    
    def load_inventory(self):
        """Initialize with some sample items"""
        self.inventory = {
            "001": {"name": "Notebook", "quantity": 50, "price": 2.99},
            "002": {"name": "Pen", "quantity": 100, "price": 1.49},
            "003": {"name": "Pencil", "quantity": 75, "price": 0.99},
            "004": {"name": "Eraser", "quantity": 40, "price": 0.59},
            "005": {"name": "Ruler", "quantity": 30, "price": 1.99}
        }
    
    def display_menu(self):
        """Display the main menu"""
        print("\nInventory Management System")
        print("1. View all items")
        print("2. Add new item")
        print("3. Update item quantity")
        print("4. Remove item")
        print("5. Search for item")
        print("6. Exit")
    
    def view_all_items(self):
        """Display all items in inventory"""
        print("\nCurrent Inventory:")
        print("-" * 60)
        print(f"{'ID':<5} {'Name':<15} {'Quantity':<10} {'Price':<10} {'Total Value':<10}")
        print("-" * 60)
        
        for item_id, item in self.inventory.items():
            total_value = item['quantity'] * item['price']
            print(f"{item_id:<5} {item['name']:<15} {item['quantity']:<10} ${item['price']:<9.2f} ${total_value:<9.2f}")
    
    def add_item(self):
        """Add a new item to inventory"""
        print("\nAdd New Item")
        item_id = input("Enter item ID: ")
        
        if item_id in self.inventory:
            print("Error: Item ID already exists!")
            return
        
        name = input("Enter item name: ")
        
        try:
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price per unit: $"))
        except ValueError:
            print("Error: Quantity must be a whole number and price must be a number!")
            return
        
        self.inventory[item_id] = {
            "name": name,
            "quantity": quantity,
            "price": price
        }
        print(f"Item '{name}' added successfully!")
    
    def update_quantity(self):
        """Update quantity of an existing item"""
        print("\nUpdate Item Quantity")
        self.view_all_items()
        item_id = input("\nEnter item ID to update: ")
        
        if item_id not in self.inventory:
            print("Error: Item ID not found!")
            return
        
        try:
            new_quantity = int(input(f"Enter new quantity for {self.inventory[item_id]['name']}: "))
        except ValueError:
            print("Error: Quantity must be a whole number!")
            return
        
        self.inventory[item_id]['quantity'] = new_quantity
        print("Quantity updated successfully!")
    
    def remove_item(self):
        """Remove an item from inventory"""
        print("\nRemove Item")
        self.view_all_items()
        item_id = input("\nEnter item ID to remove: ")
        
        if item_id not in self.inventory:
            print("Error: Item ID not found!")
            return
        
        item_name = self.inventory[item_id]['name']
        del self.inventory[item_id]
        print(f"Item '{item_name}' removed successfully!")
    
    def search_item(self):
        """Search for an item by name or ID"""
        print("\nSearch Inventory")
        search_term = input("Enter item ID or name to search: ").lower()
        
        found_items = []
        
        for item_id, item in self.inventory.items():
            if search_term in item_id.lower() or search_term in item['name'].lower():
                found_items.append((item_id, item))
        
        if not found_items:
            print("No matching items found.")
            return
        
        print("\nSearch Results:")
        print("-" * 60)
        print(f"{'ID':<5} {'Name':<15} {'Quantity':<10} {'Price':<10}")
        print("-" * 60)
        
        for item_id, item in found_items:
            print(f"{item_id:<5} {item['name']:<15} {item['quantity']:<10} ${item['price']:<9.2f}")
    
    def run(self):
        """Main program loop"""
        while True:
            self.display_menu()
            choice = input("Enter your choice (1-6): ")
            
            if choice == "1":
                self.view_all_items()
            elif choice == "2":
                self.add_item()
            elif choice == "3":
                self.update_quantity()
            elif choice == "4":
                self.remove_item()
            elif choice == "5":
                self.search_item()
            elif choice == "6":
                print("Exiting Inventory Management System. Goodbye!")
                break
            else:
                print("Invalid choice. Please enter a number between 1-6.")
            
            input("\nPress Enter to continue...")

# Create and run the inventory system
if __name__ == "__main__":
    system = InventorySystem()
    system.run()