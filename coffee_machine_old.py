class CoffeeMachine:
    water = 400
    milk = 540
    coffee_beans = 120
    disposable_cups = 9
    money = 550
    user_input = ""

    def __init__(self):
        print("Write action (buy, fill, take, remaining, exit):")
        CoffeeMachine.take_input(self)
        if self.user_input == "buy":
            CoffeeMachine.user_buy(self)
        elif self.user_input == "fill":
            CoffeeMachine.user_fill(self)
        elif self.user_input == "take":
            print("Take")
        elif self.user_input == "remaining":
            print("Remaining")
        elif self.user_input == "exit":
            exit()
        else:
            print("Invalid Entry")
            CoffeeMachine.__init__(self)

    def take_input(self):
        self.user_input = input()

    def user_buy(self):
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        CoffeeMachine.take_input(self)
        if self.user_input == 'back':
            CoffeeMachine.__init__(self)
        elif self.user_input in ["1", "2", "3"]:
            CoffeeMachine.contents_check(self)
        else:
            print("Invalid Entry")

    def contents_check(self):
        if self.user_input == "1":
            if CoffeeMachine.water - 250 < 0:
                print("Sorry, not enough water!")
            elif CoffeeMachine.coffee_beans - 16 < 0:
                print("Sorry, not enough coffee beans!")
            elif CoffeeMachine.disposable_cups - 1 < 0:
                print("Sorry, not enough disposable cups!")
            else:
                print("I have enough resources, making you a espresso")
                CoffeeMachine.water -= 250
                CoffeeMachine.coffee_beans -= 16
                CoffeeMachine.disposable_cups -= 1
                CoffeeMachine.money += 4
        elif self.user_input == "2":
            if CoffeeMachine.water - 350 < 0:
                print("Sorry, not enough water!")
            elif CoffeeMachine.milk - 75 < 0:
                print("Sorry, not enough milk!")
            elif CoffeeMachine.coffee_beans - 20 < 0:
                print("Sorry, not enough coffee beans!")
            elif CoffeeMachine.disposable_cups - 1 < 0:
                print("Sorry, not enough disposable cups!")
            else:
                print("I have enough resources, making you a latte!")
                CoffeeMachine.water -= 350
                CoffeeMachine.milk -= 75
                CoffeeMachine.coffee_beans -= 20
                CoffeeMachine.disposable_cups -= 1
                CoffeeMachine.money += 7
        elif self.user_input == "3":
            if CoffeeMachine.water - 200 < 0:
                print("Sorry, not enough water!")
            elif CoffeeMachine.milk - 100 < 0:
                print("Sorry, not enough milk!")
            elif CoffeeMachine.coffee_beans - 12 < 0:
                print("Sorry, not enough coffee beans!")
            elif CoffeeMachine.disposable_cups - 1 < 0:
                print("Sorry, not enough disposable cups!")
            else:
                print("I have enough resources, making you a cappuccino!")
                CoffeeMachine.water -= 200
                CoffeeMachine.milk -= 100
                CoffeeMachine.coffee_beans -= 12
                CoffeeMachine.disposable_cups -= 1
                CoffeeMachine.money += 6
        print(CoffeeMachine.water)
        CoffeeMachine.__init__(self)

    def user_fill(self):
        print("Write how many ml of water do you want to add:")

        print("Write how many ml of milk do you want to add:")
        CoffeeMachine.milk += self.take_input()
        print("Write how many grams of coffee beans do you want to add:")
        CoffeeMachine.coffee_beans += self.take_input()
        print("Write how many disposable cups of coffee do you want to add:")
        CoffeeMachine.disposable_cups += self.take_input()
        print(CoffeeMachine.water)


test = CoffeeMachine()
