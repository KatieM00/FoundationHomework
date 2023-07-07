class InsufficientFundError(Exception):
    pass


class MaximumAttemptsExceededError(Exception):
    pass


def shop_simulation():
    # Dictionary of the items and their prices
    items = {
        "Headphones": 30,
        "Kindle": 80,
        "USB": 15,
        "LaptopCase": 28,
        "Mouse": 18,
        "Keyboard": 35,
        "Printer": 82,
        "Laptop": 250,
        "SmartWatch": 100
    }
    customer_money = 100

    print("Welcome to the shop!")
    print("Here are the available items and their prices:")
    for item, price in items.items():
        print(f"{item}: £{price}")

    while True:
        try:
            # Prompt for item selection
            option = input("Enter the items you want to purchase (or 'exit' to leave): ")
            if option == "exit":
                break
            elif option not in items:
                raise ValueError("Invalid item selected")

            item_price = items[option]
            if item_price <= customer_money:
                # Purchase successful
                customer_money -= item_price
                print(f"here's your {option}!")
                del items[option]

            else:
                # Insufficient funds for the selected item
                print("you don't have enough money for this item.")
                add_money = int(
                    input("Would you like to add more money to your account? Enter the amount (or 0to exit):"))
                if add_money == 0:
                    raise InsufficientFundError("You don't have enough money to continue shopping!")
                customer_money += add_money

        except ValueError as e:
            # Invalid item selection
            print(str(e))
            print("Please try again.")

        except InsufficientFundError as e:
            # Customer doesn't have enough money to continue shopping
            print(str(e))
            print("Thank you for visiting the shop!")


        else:
            # Purchase successful
            print("Purchase successful!")

        finally:
            # Display remaining balance after each iteration
            print(f"Your remaining balance is £{customer_money}")

        if len(items) == 0:
            # All items have been purchased
            print("You have purchased all available items!")
            break

        if len(items) < 3:
            # Maximum number of purchase attempts exceeded
            raise MaximumAttemptsExceededError("You have exceeded the maximum number of purchase attempts!")


if __name__ == "__main__":
    try:
        shop_simulation()
    except MaximumAttemptsExceededError as e: \
            print(str(e))
    finally:
        print("Exiting the shop.")
