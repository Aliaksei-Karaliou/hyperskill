# Write your code here


class CoffeeReceipt:

    def __init__(self, code, name, water, milk, coffee_beans, price):
        super().__init__()
        self.code = code
        self.name = name
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee_beans
        self.price = price


class CoffeeContainer:
    def __init__(self, water, milk, coffee, cash, cups):
        super().__init__()
        self.water = water
        self.milk = milk
        self.coffee_beans = coffee
        self.cash = cash
        self.cups = cups

    def make_coffee(self, receipt: CoffeeReceipt):
        if self.water < receipt.water:
            return "water"
        elif self.milk < receipt.milk:
            return "milk"
        elif self.coffee_beans < receipt.coffee_beans:
            return "coffee_beans"
        elif self.cups == 0:
            return "disposable cups"
        else:
            self.water -= receipt.water
            self.milk -= receipt.milk
            self.coffee_beans -= receipt.coffee_beans
            self.cash += receipt.price
            self.cups -= 1
            return None

    def take_cash(self):
        cash = self.cash
        self.cash = 0
        return cash


coffee_types = [
    CoffeeReceipt(1, "espresso", water = 250, milk = 0, coffee_beans = 16,
                  price = 4),
    CoffeeReceipt(2, "latte", water = 350, milk = 75, coffee_beans = 20,
                  price = 7),
    CoffeeReceipt(3, "espresso", water = 200, milk = 100, coffee_beans = 12,
                  price = 6)
]


def get_buy_header():
    header = "What do you want to buy? "

    for cof in coffee_types:
        header = header + f"{cof.code} - {cof.name}, "

    header = header + "back - to main menu:"

    return header


def buy(container: CoffeeContainer):
    coffee_type = input(get_buy_header())

    for cof in coffee_types:
        if str(cof.code) == coffee_type:
            missing = container.make_coffee(cof)
            print(
                "I have enough resources, making you a coffee!"
                if missing is None else
                f"Sorry, not enough {missing}!")
            break


def remaining(container: CoffeeContainer):
    print(f"""The coffee machine has:
{container.water} of water
{container.milk} of milk
{container.coffee_beans} of coffee beans
{container.cups} of disposable cups
${container.cash} of money""")


def take(cash):
    print("I gave you ${}".format(cash))
    return 0


def fill(container: CoffeeContainer):
    container.water += int(
        input("Write how many ml of water do you want to add:"))
    container.milk += int(
        input("Write how many ml of milk do you want to add:"))
    container.coffee_beans += int(
        input("Write how many grams of coffee beans do you want to add:"))
    container.cups += int(
        input("Write how many disposable cups of coffee do you want to add:"))


def action(container: CoffeeContainer):
    while True:
        action_name = input("Write action (buy, fill, take, remaining, exit):")
        if action_name == "buy":
            buy(container)
        elif action_name == "fill":
            fill(container)
        elif action_name == "take":
            cash = container.take_cash()
            print(f"I gave you ${cash}")
        elif action_name == "remaining":
            remaining(container)
        elif action_name == "exit":
            break
        print("========================================\n")


coffee_container = CoffeeContainer(cash = 550, water = 400, milk = 540,
                                   coffee = 120,
                                   cups = 9)

action(coffee_container)
