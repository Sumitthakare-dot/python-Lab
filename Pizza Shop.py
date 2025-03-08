
class Pizza:
    def __init__(self, name, size, price):
        self.name = name
        self.size = size
        self.price = price

    def __str__(self):
        return f"{self.size} {self.name} Pizza - ${self.price}"


class Order:
    def __init__(self):
        self.pizzas = []
        self.total_price = 0
    
    def add_pizza(self, pizza):
        self.pizzas.append(pizza)
        self.total_price += pizza.price

    def show_order(self):
        print("\nYour Order:")
        for pizza in self.pizzas:
            print(pizza)
        print(f"\nTotal Price: ${self.total_price}")


class PizzaShop:
    def __init__(self):
        self.menu = [
            Pizza("Margherita", "Small", 8),
            Pizza("Margherita", "Medium", 10),
            Pizza("Margherita", "Large", 12),
            Pizza("Pepperoni", "Small", 9),
            Pizza("Pepperoni", "Medium", 11),
            Pizza("Pepperoni", "Large", 13),
            Pizza("Veggie", "Small", 7),
            Pizza("Veggie", "Medium", 9),
            Pizza("Veggie", "Large", 11),
        ]
        self.order = Order()
    
    def show_menu(self):
        print("Welcome to Python Pizza Shop!")
        print("\nAvailable Pizzas:")
        for i, pizza in enumerate(self.menu, 1):
            print(f"{i}. {pizza}")

    def take_order(self):
        while True:
            self.show_menu()
            try:
                choice = int(input("\nEnter the number of the pizza you want to order (0 to finish): "))
                if choice == 0:
                    break
                if choice < 1 or choice > len(self.menu):
                    print("Invalid choice, please try again.")
                    continue
                
                pizza = self.menu[choice - 1]
                self.order.add_pizza(pizza)
                print(f"\nAdded: {pizza}\n")
            except ValueError:
                print("Please enter a valid number.")

    def finalize_order(self):
        print("\nFinalizing Order...")
        self.order.show_order()
        customer_name = input("\nEnter your name: ")
        delivery_address = input("Enter your delivery address: ")
        
        print(f"\nThank you for your order, {customer_name}!")
        print(f"Your pizza(s) will be delivered to: {delivery_address}")
        print(f"Total amount to pay: ${self.order.total_price}")
        print("\nEnjoy your meal!")


def main():
    shop = PizzaShop()
    shop.take_order()
    shop.finalize_order()

if __name__ == "__main__":
    main()
