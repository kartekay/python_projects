class CoffeeMachine:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
            "money": 0.0
        }
        self.menu = {
            "espresso": {"water": 50, "milk": 0, "coffee": 18, "cost": 1.5},
            "latte": {"water": 200, "milk": 150, "coffee": 24, "cost": 2.5},
            "cappuccino": {"water": 250, "milk": 100, "coffee": 24, "cost": 3.0}
        }
        self.is_on = True

    def print_report(self):
        for resource, amount in self.resources.items():
            unit = "ml" if resource in ["water", "milk"] else "g" if resource == "coffee" else "$"
            print(f"{resource.capitalize()}: {amount}{unit}")

    def check_resources(self, drink):
        for item, required in self.menu[drink].items():
            if item != "cost" and self.resources[item] < required:
                print(f"Sorry there is not enough {item}.")
                return False
        return True

    def process_coins(self):
        quarters = int(input("How many quarters? ")) * 0.25
        dimes = int(input("How many dimes? ")) * 0.10
        nickels = int(input("How many nickels? ")) * 0.05
        pennies = int(input("How many pennies? ")) * 0.01
        return round(quarters + dimes + nickels + pennies, 2)

    def handle_transaction(self, drink, inserted_money):
        cost = self.menu[drink]["cost"]
        if inserted_money < cost:
            print("Sorry that's not enough money. Money refunded.")
            return False
        elif inserted_money > cost:
            change = round(inserted_money - cost, 2)
            print(f"Here is ${change} in change.")
        self.resources["money"] += cost
        return True

    def make_coffee(self, drink):
        for item, required in self.menu[drink].items():
            if item != "cost":
                self.resources[item] -= required
        print(f"Here is your {drink}. Enjoy!")

    def refill_resources(self):
        self.resources["water"] += int(input("How much water to add (ml)? "))
        self.resources["milk"] += int(input("How much milk to add (ml)? "))
        self.resources["coffee"] += int(input("How much coffee to add (g)? "))
        print("Resources refilled.")

    def add_custom_drink(self):
        name = input("Enter the name of the custom drink: ").lower()
        water = int(input("Enter the amount of water required (ml): "))
        milk = int(input("Enter the amount of milk required (ml): "))
        coffee = int(input("Enter the amount of coffee required (g): "))
        cost = float(input("Enter the cost of the drink: "))
        self.menu[name] = {"water": water, "milk": milk, "coffee": coffee, "cost": cost}
        print(f"Custom drink '{name}' added to the menu.")

    def start(self):
        while self.is_on:
            choice = input("What would you like? (espresso/latte/cappuccino/custom/refill/report/off): ").lower()
            if choice == "off":
                self.is_on = False
            elif choice == "report":
                self.print_report()
            elif choice == "refill":
                self.refill_resources()
            elif choice == "custom":
                self.add_custom_drink()
            elif choice in self.menu:
                if self.check_resources(choice):
                    payment = self.process_coins()
                    if self.handle_transaction(choice, payment):
                        self.make_coffee(choice)
            else:
                print("Invalid choice. Please select again.")

coffee_machine = CoffeeMachine()
coffee_machine.start()
