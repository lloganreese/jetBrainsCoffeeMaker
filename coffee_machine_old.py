water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9
money = 550


def display_contents():
    print("The coffee machine has:")
    print(f"{water} of water")
    print(f"{milk} of milk")
    print(f"{coffee_beans} of coffee beans")
    print(f"{disposable_cups} of disposable cups")
    print(f"{money} of money")


def user_buy():
    global water, milk, coffee_beans, disposable_cups, money
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu: ")
    buy_input = input()
    print("")
    if buy_input == 'back':
        main()
    elif buy_input in ["1", "2", "3"]:
        contents_check(buy_input)
    else:
        print("Invalid Entry")


def contents_check(selection):
    global water, milk, coffee_beans, disposable_cups, money
    if selection == "1":
        if water - 250 < 0:
            print("Sorry, not enough water!")
        elif coffee_beans - 16 < 0:
            print("Sorry, not enough coffee beans!")
        elif disposable_cups - 1 < 0:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a espresso")
            water -= 250
            coffee_beans -= 16
            disposable_cups -= 1
            money += 4
    elif selection == "2":
        if water - 350 < 0:
            print("Sorry, not enough water!")
        elif milk - 75 < 0:
            print("Sorry, not enough milk!")
        elif coffee_beans - 20 < 0:
            print("Sorry, not enough coffee beans!")
        elif disposable_cups - 1 < 0:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a latte!")
            water -= 350
            milk -= 75
            coffee_beans -= 20
            disposable_cups -= 1
            money += 7
    elif selection == "3":
        if water - 200 < 0:
            print("Sorry, not enough water!")
        elif milk - 100 < 0:
            print("Sorry, not enough milk!")
        elif coffee_beans - 12 < 0:
            print("Sorry, not enough coffee beans!")
        elif disposable_cups - 1 < 0:
            print("Sorry, not enough disposable cups!")
        else:
            print("I have enough resources, making you a cappuccino!")
            water -= 200
            milk -= 100
            coffee_beans -= 12
            disposable_cups -= 1
            money += 6


def user_fill():
    global water, milk, coffee_beans, disposable_cups, money
    print("Write how many ml of water do you want to add:")
    water += int(input())
    print("Write how many ml of milk do you want to add:")
    milk += int(input())
    print("Write how many grams of coffee beans do you want to add:")
    coffee_beans += int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    disposable_cups += int(input())
    print("")


def user_take():
    global money
    print(f"I gave you ${money}")
    money -= money


def main():
    while True:
        print("Write action (buy, fill, take, remaining, exit): ")
        action_input = input()

        if action_input == "buy":
            user_buy()
            print("")
        elif action_input == "fill":
            user_fill()
            print("")
        elif action_input == "take":
            user_take()
            print("")
        elif action_input == "remaining":
            display_contents()
            print("")
        elif action_input == "exit":
            exit()
        else:
            print("Invalid Entry")
            print("")


main()
