from art import logo
print(logo)
print("Welcome to secret auction program")
should_continue = True
bidders_dictionary = {}
price_list = []
while should_continue:
    name = input("What's your name?").lower()
    price = int(input("what's your bid? $"))
    bidders_dictionary[name] = price
    price_list.append(price)
    bidders = input("are there any bidders? type 'yes' or 'no' ").lower()
    if bidders == "yes":
        print("\n" * 20)
    else:
        should_continue = False
key_bidder = max(bidders_dictionary, key=bidders_dictionary.get)
price_list.sort()
value_bidder = price_list[-1]
print(f"the winner is {key_bidder} with amount of {value_bidder}")



