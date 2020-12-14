class CoffeeMachine:
    water = 400
    milk = 540
    coffee_beans = 120
    disposable_cups = 9
    money = 550
    user_input = ""

    # main constructor - sends each option to the correct method
    def __init__(self):
        print("\nWrite action (buy, fill, take, remaining, exit):")
        CoffeeMachine.take_input(self)
        if self.user_input == "buy":
            CoffeeMachine.user_buy(self)
        elif self.user_input == "fill":
            CoffeeMachine.user_fill(self)
        elif self.user_input == "take":
            CoffeeMachine.take_money(self)
        elif self.user_input == "remaining":
            CoffeeMachine.remaining(self)
        elif self.user_input == "exit":
            exit()
        else:
            print("Invalid Entry\n")
            CoffeeMachine.__init__(self)

    # takes a string input to be used throughout class
    def take_input(self):
        self.user_input = input()

    # displays the current total of each class variable
    def remaining(self):
        print("\nThe coffee machine has:")
        print(f"{CoffeeMachine.water} of water")
        print(f"{CoffeeMachine.milk} of milk")
        print(f"{CoffeeMachine.coffee_beans} of coffee beans")
        print(f"{CoffeeMachine.disposable_cups} of disposable cups")
        print(f"{CoffeeMachine.money} of money")
        CoffeeMachine.__init__(self)

    # prints how much money was currently in the machine
    def take_money(self):
        print(f"I gave you ${CoffeeMachine.money}")
        CoffeeMachine.money -= CoffeeMachine.money
        CoffeeMachine.__init__(self)

    # prompts user with buy screen - restarts program or pushes to contents check
    def user_buy(self):
        print("\nWhat do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
        CoffeeMachine.take_input(self)
        if self.user_input == 'back':
            CoffeeMachine.__init__(self)
        elif self.user_input in ["1", "2", "3"]:
            CoffeeMachine.contents_check(self)
        else:
            print("Invalid Entry")

    # checks to see if global variables hold the correct amount of 'contents'
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
        CoffeeMachine.__init__(self)

    # takes input & converts to int then adds it to class variables
    def user_fill(self):
        print("\nWrite how many ml of water do you want to add:")
        CoffeeMachine.take_input(self)
        CoffeeMachine.water += int(self.user_input)
        print("Write how many ml of milk do you want to add:")
        CoffeeMachine.take_input(self)
        CoffeeMachine.milk += int(self.user_input)
        print("Write how many grams of coffee beans do you want to add:")
        CoffeeMachine.take_input(self)
        CoffeeMachine.coffee_beans += int(self.user_input)
        print("Write how many disposable cups of coffee do you want to add:")
        CoffeeMachine.take_input(self)
        CoffeeMachine.disposable_cups += int(self.user_input)
        CoffeeMachine.__init__(self)


test = CoffeeMachine()
