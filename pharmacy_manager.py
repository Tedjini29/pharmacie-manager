import tkinter as tk
from tkinter import messagebox

# Classe pour gérer l'inventaire
class PharmacyManager:
    def __init__(self, root):
        self.root = root
        self.root.title("Pharmacy Manager")
        self.root.geometry("500x400")
        self.inventory = {}  # Dictionnaire pour stocker les produits

        # Titre
        self.label_title = tk.Label(root, text="Pharmacy Manager", font=("Arial", 20))
        self.label_title.pack(pady=10)

        # Entrée pour le nom du produit
        self.label_product = tk.Label(root, text="Product Name:")
        self.label_product.pack()
        self.entry_product = tk.Entry(root, width=30)
        self.entry_product.pack()

        # Entrée pour la quantité
        self.label_quantity = tk.Label(root, text="Quantity:")
        self.label_quantity.pack()
        self.entry_quantity = tk.Entry(root, width=30)
        self.entry_quantity.pack()

        # Bouton pour ajouter un produit
        self.add_button = tk.Button(root, text="Add Product", command=self.add_product, bg="green", fg="white")
        self.add_button.pack(pady=5)

        # Bouton pour afficher l'inventaire
        self.show_button = tk.Button(root, text="Show Inventory", command=self.show_inventory, bg="blue", fg="white")
        self.show_button.pack(pady=5)

        # Bouton pour quitter
        self.quit_button = tk.Button(root, text="Quit", command=root.quit, bg="red", fg="white")
        self.quit_button.pack(pady=5)

    # Fonction pour ajouter un produit
    def add_product(self):
        product = self.entry_product.get()
        quantity = self.entry_quantity.get()

        if product and quantity.isdigit():
            quantity = int(quantity)
            if product in self.inventory:
                self.inventory[product] += quantity
            else:
                self.inventory[product] = quantity
            messagebox.showinfo("Success", f"Added {quantity} units of {product}.")
        else:
            messagebox.showerror("Error", "Please enter a valid product name and quantity.")

        # Effacer les champs après l'ajout
        self.entry_product.delete(0, tk.END)
        self.entry_quantity.delete(0, tk.END)

    # Fonction pour afficher l'inventaire
    def show_inventory(self):
        if self.inventory:
            inventory_list = "\n".join([f"{product}: {quantity}" for product, quantity in self.inventory.items()])
            messagebox.showinfo("Inventory", inventory_list)
        else:
            messagebox.showinfo("Inventory", "The inventory is empty.")

# Exécution de l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = PharmacyManager(root)
    root.mainloop()
