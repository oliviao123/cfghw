class NotEnoughMoneyError(Exception):
    pass


class MaximumAttemptsExceededError(Exception):
    pass


def select_item(items):
    print("Here are the items and their prices:")
    for item, price in items.items():
        print(f"{item}: £{price}")

    while True:
        try:
            option = input("Enter the item you want to purchase: ")
            if option == "exit":
                return None
            price = items[option]
            return option, price
        except KeyError:
            print("Invalid option selected")


def purchase_item(option, price, balance):
    if price > balance:
        raise NotEnoughMoneyError("You don't have enough money")
    print(f"Here's your {option}!")
    balance -= price
    print(f"Your remaining balance is £{balance}")
    return balance


def add_money(balance):
    extra_money = int(input("Enter the amount of extra money: "))
    balance += extra_money
    print(f"Your new balance is £{balance}")
    return balance


items = {
    "apple": 50,
    "pear": 100,
    "orange": 150,
}

balance = 100

print("Welcome to the shop!")
print("Enter 'exit' to leave the shop")

try_count = 0

while True:
    option, price = select_item(items)
    if option is None:
        print("Goodbye!")
        break

    try:
        balance = purchase_item(option, price, balance)

    except NotEnoughMoneyError as e:
        print(str(e))
        more_money = input("Do you have more money? (y/n) ")
        if more_money.lower() == "y":
            balance = add_money(balance)
        else:
            print("Goodbye!")
            break

    except Exception as e:
        try_count += 1
        if try_count >= 3:
            raise MaximumAttemptsExceededError("You've exceeded the maximum attempts")
        print(str(e))
        print(f"Please try again ({3 - try_count} attempts left)")

print("Thank you for visiting the shop!")