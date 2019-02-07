"""
Creates database called 'stock.db'.
In DB, table called 'stock' containing 'nameItem', 'priceItem', 'quantityItem'.
"""


class Database_Management:
    def __init__(self):
        import sqlite3
        self.conn = sqlite3.connect("stock.db")
        self.cur = self.conn.cursor()

        self.create_table()


    def create_table(self):
        self.cur.execute("""CREATE TABLE IF NOT EXISTS 
                        stock(nameItem TEXT UNIQUE, priceItem REAL, quantityItem TEXT)""")


    def add_new_item(self, nameToAdd, priceToAdd, quantityToAdd):
        try:
            self.cur.execute("INSERT INTO stock(nameItem, priceItem, quantityItem) VALUES(?, ?, ?)",
                            (nameToAdd, priceToAdd, quantityToAdd))
            self.conn.commit()
            print("Added Successfully!")
        except:
            print("Error inserting.")
    

    def remove_item(self, nameToRemove):
        try:
            self.cur.execute("DELETE FROM stock WHERE nameItem = ?",
                            (nameToRemove,))
            self.conn.commit()
            print("Removed Successfully!")
        except:
            print("Error deleting.")
    

    def update_item_name(self, nameCurrent, nameNew):
        try:
            self.cur.execute("UPDATE stock SET nameItem = ? WHERE nameItem = ?",
                            (nameNew, nameCurrent))
            self.conn.commit()
            print("Updated Successfully!")
        except:
            print("Error updating name.")
    

    def update_item_price(self, nameItem, priceNew):
        try:
            self.cur.execute("UPDATE stock SET priceItem = ? WHERE nameItem = ?",
                            (priceNew, nameItem))
            self.conn.commit()
            print("Updated Successfully!")
        except:
            print("Error updating price.")


    def update_item_quantity(self, nameItem, quantityNew):
        try:
            self.cur.execute("UPDATE stock SET quantityItem = ? WHERE nameItem = ?",
                            (quantityNew, nameItem))
            self.conn.commit()
            print("Updated Successfully!")
        except:
            print("Error updating quantity.")
                    


    def lookup_item(self, nameOfItem):
        try:
            self.cur.execute("SELECT * FROM stock WHERE nameItem = ?", (nameOfItem,))
            row = self.cur.fetchone()

            return row
        except:
            print("Error looking up item.")


    def get_all_items(self):
        try:
            self.cur.execute("SELECT * FROM stock")
            results = self.cur.fetchall()
            return results
        except:
            print("error fetching all items.")
        


    def yeet(self):
        print(self.conn)



if __name__ == "__main__":
    db = Database_Management()

    db.cur.close()
    db.conn.close()