class IceCreamParlor:
    def __init__(self):
        self.seasonal_flavors = {
            "Winter": ["Peppermint Bark", "Eggnog"],
            "Spring": ["Strawberry Blossom", "Lemon Lavender"],
            "Summer": ["Mango Sorbet", "Blueberry Cheesecake"],
            "Fall": ["Pumpkin Spice", "Caramel Apple"]
        }
        self.inventory = {
            "Milk": 50,
            "Sugar": 30,
            "Cream": 40,
            "Strawberries": 20,
            "Mangoes": 25,
            "Pumpkins": 15,
            "Blueberries": 10,
        }
        self.customer_suggestions = []

    def display_seasonal_flavors(self, season):
        if season in self.seasonal_flavors:
            print(f"\n{season} Seasonal Flavors:")
            for flavor in self.seasonal_flavors[season]:
                print(f"- {flavor}")
        else:
            print("\nInvalid season. Please enter Winter, Spring, Summer, or Fall.")

    def view_inventory(self):
        print("\nCurrent Ingredient Inventory:")
        for ingredient, quantity in self.inventory.items():
            print(f"{ingredient}: {quantity} units")

    def update_inventory(self, ingredient, quantity):
        if ingredient in self.inventory:
            self.inventory[ingredient] += quantity
            print(f"\nUpdated {ingredient} inventory to {self.inventory[ingredient]} units.")
        else:
            print("\nIngredient not found in inventory.")

    def add_customer_suggestion(self, flavor, allergies):
        self.customer_suggestions.append({"Flavor": flavor, "Allergies": allergies})
        print(f"\nThank you for suggesting '{flavor}'! We'll consider it.")

    def view_customer_suggestions(self):
        if self.customer_suggestions:
            print("\nCustomer Suggestions:")
            for suggestion in self.customer_suggestions:
                flavor = suggestion["Flavor"]
                allergies = suggestion["Allergies"]
                print(f"- {flavor} (Allergies: {', '.join(allergies) if allergies else 'None'})")
        else:
            print("\nNo customer suggestions yet.")

def main():
    parlor = IceCreamParlor()
    
    while True:
        print("\nIce Cream Parlor Management System")
        print("1. View Seasonal Flavors")
        print("2. View Ingredient Inventory")
        print("3. Update Ingredient Inventory")
        print("4. Add Customer Flavor Suggestion")
        print("5. View Customer Suggestions")
        print("6. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            season = input("Enter the season (Winter, Spring, Summer, Fall): ")
            parlor.display_seasonal_flavors(season)
        elif choice == "2":
            parlor.view_inventory()
        elif choice == "3":
            ingredient = input("Enter the ingredient to update: ")
            try:
                quantity = int(input("Enter the quantity to add/remove: "))
                parlor.update_inventory(ingredient, quantity)
            except ValueError:
                print("\nInvalid quantity. Please enter a number.")
        elif choice == "4":
            flavor = input("Enter the flavor suggestion: ")
            allergies = input("Enter any allergy concerns (comma-separated, leave blank if none): ").split(",")
            allergies = [allergy.strip() for allergy in allergies if allergy.strip()]
            parlor.add_customer_suggestion(flavor, allergies)
        elif choice == "5":
            parlor.view_customer_suggestions()
        elif choice == "6":
            print("Thank you for using the Ice Cream Parlor Management System!")
            break
        else:
            print("\nInvalid choice. Please try again.")

if __name__ == "__main__":
    main()
