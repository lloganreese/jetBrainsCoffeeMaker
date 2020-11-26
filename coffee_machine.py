print("Write how many ml of water the coffee machine has:")
water_ml = int(input())
print("Write how many ml of milk the coffee machine has:")
milk_ml = int(input())
print("Write how many grams of coffee beans the coffee machine has:")
grams_coffee = int(input())
print("Write how many cups of coffee you will need:")
cups_of_coffee = int(input())

amount_made = int(min([(water_ml / 200), (milk_ml / 50), (grams_coffee / 15)]))

if cups_of_coffee == amount_made:
    print("Yes, I can make that amount of coffee")
elif amount_made >= cups_of_coffee:
    print(f"Yes, I can make that amount of coffee (and even {cups_of_coffee - amount_made} more than that)")
elif amount_made < cups_of_coffee:
    print(f"No, I can make only {amount_made} cups of coffee")
else:
    print("Invalid Entry")
