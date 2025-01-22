class CoffeeMachine:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
            "money": 0.0
        }
        self.menu = {
            "espresso": {"ingredients": {"water": 50, "coffee": 18}, "cost": 1.5},
            "latte": {"ingredients": {"water": 200, "milk": 150, "coffee": 24}, "cost": 2.5},
            "cappuccino": {"ingredients": {"water": 250, "milk": 100, "coffee": 24}, "cost": 3.0}
        }
        self.is_on = True

    def report(self):
        return f"Water: {self.resources['water']}ml\nMilk: {self.resources['milk']}ml\nCoffee: {self.resources['coffee']}g\nMoney: ${self.resources['money']:.2f}"

    def check_resources(self, drink):
        for item, amount in self.menu[drink]["ingredients"].items():
            if self.resources[item] < amount:
                return f"Sorry there is not enough {item}."
        return "sufficient"

    def process_coins(self):
        print("Please insert coins.")
        quarters = int(input("How many quarters?: "))
        dimes = int(input("How many dimes?: "))
        nickels = int(input("How many nickels?: "))
        pennies = int(input("How many pennies?: "))
        return quarters * 0.25 + dimes * 0.10 + nickels * 0.05 + pennies * 0.01

    def handle_transaction(self, money_received, drink):
        cost = self.menu[drink]["cost"]
        if money_received < cost:
            return "Sorry that's not enough money. Money refunded.", False
        self.resources["money"] += cost
        change = round(money_received - cost, 2)
        if change > 0:
            print(f"Here is ${change} in change.")
        return "successful", True

    def make_coffee(self, drink):
        for item, amount in self.menu[drink]["ingredients"].items():
            self.resources[item] -= amount
        return f"Here is your {drink}. Enjoy!"

    def start(self):
        while self.is_on:
            choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
            if choice == "off":
                self.is_on = False
            elif choice == "report":
                print(self.report())
            elif choice in self.menu:
                resource_check = self.check_resources(choice)
                if resource_check == "sufficient":
                    payment = self.process_coins()
                    message, success = self.handle_transaction(payment, choice)
                    if success:
                        print(self.make_coffee(choice))
                    else:
                        print(message)
                else:
                    print(resource_check)
            else:
                print("Invalid selection.")

coffee_machine = CoffeeMachine()
coffee_machine.start()
