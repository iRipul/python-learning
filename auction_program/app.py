from artwork import logo
import os
print(logo)
print("\n\n")

# Initialization
bids_data_list = []

should_continue = True

while should_continue:
    name = input("Enter your name\n").lower()
    bid_price = float(input("Enter your bid $"))

    new_bid = {}
    new_bid["name"] = name
    new_bid["price"] = bid_price

    bids_data_list.append(new_bid)

    ans = input("is there anyone who wants to bid? yes or no\n")

    if ans == "no":
        should_continue = False
        max_bid = bids_data_list[0]
        for bid in bids_data_list:
            if max_bid["price"] < bid["price"]:
                max_bid = bid
            
        print(f"The winner is {max_bid['name']} with highest bid ${max_bid['price']}")
    else:
        os.system('clear')


