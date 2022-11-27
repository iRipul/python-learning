from artwork import logo
import os
print(logo)
print("\n\n")

# Initialization
bids_data_list = []

should_continue = True

def find_max_bid(bids_data): 
    max_bid = bids_data[0]
    for bid in bids_data:
        if max_bid["price"] < bid["price"]:
            max_bid = bid
    print(f"The winner is {max_bid['name']} with highest bid ${max_bid['price']}")

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
        find_max_bid(bids_data_list)
    else:
        os.system('clear')


