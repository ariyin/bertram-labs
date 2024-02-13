import random

class Coworker:
    def __init__(self, name, favorite_drink, drink_price):
        self.name = name
        self.favorite_drink = favorite_drink
        self.drink_price = drink_price

def select_coffee_payer(coworkers):
    total_price = sum(coworker.drink_price for coworker in coworkers)
    weights = [coworker.drink_price / total_price for coworker in coworkers]
    selected_coworker = random.choices(coworkers, weights=weights, k=1)[0]
    return selected_coworker

def main():
    coworkers = [
        Coworker("Bob", "cappuccino", 3.50),
        Coworker("Jeremy", "black coffee", 2.00),
        Coworker("Shiyu", "latte", 4.00),
        Coworker("Erica", "espresso", 3.00),
        Coworker("Emily", "mocha", 4.50),
        Coworker("Sayaka", "chai latte", 3.75),
        Coworker("Jenna", "macchiato", 3.25)
    ]

    payer = select_coffee_payer(coworkers)
    print(f"It's {payer.name}'s turn to pay for coffee today.")

if __name__ == "__main__":
    main()
