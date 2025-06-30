def main():
    coffee_list = {
        "Espresso": ["Double Shot Espresso", "Quad Shot Espresso"],
        "Drip Coffee": ["Classic Brew", "Rich Brew", "Over Ice"],
        "Cold Brew": ["Cold Pressed Espresso", "Cold Brew Coffee"]
    }

    coffee_category = what_catagorie(coffee_list)
    what_type(coffee_list, coffee_category)

def what_catagorie(coffee_list):
    while True:
        coffee_category = input("What category of coffee would you like: ").title()

        if coffee_category in coffee_list:
            print(f"{coffee_category}: {', '.join(coffee_list[coffee_category])}")
            return coffee_category
        else:
            print("Please enter one of the three categories: Espresso, Drip Coffee, Cold Brew.")

def what_type(coffee_list, coffee_category):
    while True:
        coffee_type = input("What type of coffee would you like: ").title()

        if coffee_type in coffee_list[coffee_category]:
            print("Thank you for your purchase.")
            break
        else:
            print(f"Please enter one of these types of coffee: {', '.join(coffee_list[coffee_category])}")

if __name__ == "__main__":
    main()

