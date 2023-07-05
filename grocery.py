import tkinter as tk
from tkinter import messagebox


class GroceryItem:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def __str__(self):
        return f"{self.name} - ${self.price:.2f} ({self.quantity})"


class GroceryApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Grocery App")

        self.item_label = tk.Label(root, text="Item:")
        self.item_label.pack()

        self.item_entry = tk.Entry(root)
        self.item_entry.pack()

        self.price_label = tk.Label(root, text="Price:")
        self.price_label.pack()

        self.price_entry = tk.Entry(root)
        self.price_entry.pack()

        self.quantity_label = tk.Label(root, text="Quantity:")
        self.quantity_label.pack()

        self.quantity_entry = tk.Entry(root)
        self.quantity_entry.pack()

        self.add_button = tk.Button(root, text="Add Item", command=self.add_item)
        self.add_button.pack()

        self.item_listbox = tk.Listbox(root)
        self.item_listbox.pack()

        self.remove_button = tk.Button(root, text="Remove Item", command=self.remove_item)
        self.remove_button.pack()

    def add_item(self):
        item = self.item_entry.get()
        price = self.price_entry.get()
        quantity = self.quantity_entry.get()

        if item and price and quantity:
            try:
                price = float(price)
                quantity = int(quantity)
                grocery_item = GroceryItem(item, price, quantity)
                self.item_listbox.insert(tk.END, str(grocery_item))
                self.item_entry.delete(0, tk.END)
                self.price_entry.delete(0, tk.END)
                self.quantity_entry.delete(0, tk.END)
            except ValueError:
                messagebox.showwarning("Invalid Input", "Please enter valid price and quantity.")
        else:
            messagebox.showwarning("Empty Fields", "Please enter item name, price, and quantity.")

    def remove_item(self):
        selected_index = self.item_listbox.curselection()
        if selected_index:
            self.item_listbox.delete(selected_index)
        else:
            messagebox.showwarning("No Item Selected", "Please select an item to remove.")


if __name__ == "__main__":
    root = tk.Tk()
    app = GroceryApp(root)
    root.mainloop()
