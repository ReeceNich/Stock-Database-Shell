"""
Uses stockDBhandler for retrieving the database values. 
"""

from stockDBhandler import Database_Management

class Console_Viewer:
    def __init__(self):
        self.db = Database_Management()


    def run_menu(self):
        self.print_welcome_message()
        print()
        self.menu_text = {1: "Add an Item",
                        2: "Update Name",
                        3: "Update Price",
                        4: "Update Quantity",
                        5: "Delete an Item",
                        6: "Look up an Item",
                        7: "Show all Stock Items"}
        self.print_menu_options()
        print()
        self.user_selected_option = self.get_user_option()
        self.option_selector(self.user_selected_option)


    def print_welcome_message(self):
        print("Welcome to the Stock Management Software!")          

    def print_menu_options(self):
        for key, value in self.menu_text.items():
            print("{}: {}".format(key,value))

    def get_user_option(self):
        while True:
            try:
                option = int(input("Enter an option: "))
                print()
                
                if option in self.menu_text.keys():
                    return option
                else:
                    print("Not a valid choice.")
                
            except:
                print("Error! Not a number.")

    def option_selector(self, option):
        
        if option == 1:
            self.add_item()
        elif option == 2:
            self.update_name()
        elif option == 3:
            self.update_price()
        elif option == 4:
            self.update_quantity()
        elif option == 5:
            self.delete_item()
        elif option == 6:
            self.item_lookup()
        elif option == 7:
            self.show_all_stock()
        else:
            print("Error selecting your option.")




    def add_item(self):
        name = input("Enter a name: ")
        price = float(input("Enter a price: "))
        quantity = int(input("Enter a quantity: "))

        self.db.add_new_item(name, price, quantity)

    def update_name(self):
        current = input("What is the current name: ")
        newName = input("Enter a new name: ")

        self.db.update_item_name(current, newName)
    
    def update_price(self):
        name = input("Enter a name: ")
        newPrice = float(input("Enter a new price: "))

        self.db.update_item_price(name, newPrice)
    
    def update_quantity(self):
        name = input("Enter a name: ")
        newQuantity = int(input("Enter a quantity: "))
        self.db.update_item_quantity(name, newQuantity)
    
    def delete_item(self):
        name = input("Enter the name to delete: ")
        self.db.remove_item(name)

    def item_lookup(self):
        name = input("Enter an item to lookup: ")
        result = self.db.lookup_item(name)

        if result != "":
            print()
            print("==== RESULT ====")
            print("Name:", result[0])
            print("Price:", result[1])
            print("Quantity:", result[2])
        else:
            print()
            print("==== RESULT ====")
            print("Nothing found...")

    def show_all_stock(self):
        result = self.db.get_all_items()
        

        print("|  Name  |  Price  |  Quantity  |")

        for row in range(len(result)):
            print("|  {}  |  {}  |  {}  |".format( result[row][0], result[row][1], result[row][2] ))

    
    def run(self):
        self.run_menu()

    def close_connection(self):
        self.db.cur.close()
        self.db.conn.close()





if __name__ == "__main__":
    cv = Console_Viewer()
    cv.run()
    print()
    print()
    input('Press Enter to exit')
    cv.close_connection()
