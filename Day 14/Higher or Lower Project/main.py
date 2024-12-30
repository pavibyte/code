from art import logo
from art import vs
import random
from game_data import data
print(logo)
def higherlower():
    global follower1, follower2, random_index, random_index2,user_input
    random_index = random.randrange(len(data)-1)
    print(f"Compare A: {data[random_index]["name"]}", end=",")
    print(f" a {data[random_index]["description"]}", end=",")
    print(f" from {data[random_index]["country"]}", end=",")
    print(vs)
    random_index2 = random.randrange(len(data)-1)
    print(f"Against B: {data[random_index2]["name"]}", end=",")
    print(f" a {data[random_index2]["description"]}", end=",")
    print(f" from {data[random_index2]["country"]}", end=",")

    follower1 = data[random_index]["follower_count"]
    follower2 = data[random_index2]["follower_count"]
    print(follower1)
    print(follower2)
    user_input = input("\nWho has more followers? Type 'A' or 'B': ").lower()

higherlower()
score = 0
if user_input == "a":
    user_found1 = data[random_index]["follower_count"]
    if user_found1 == follower1:

        print("\n "* 20)
        print(logo)
        print(f"You're right! Current score {score + 1}")
        higherlower()
    else:
        print("sorry you lost!")

if user_input == "b":
    user_found2 = data[random_index2]["follower_count"]
    if user_found2 == follower2:

        print("\n " * 20)
        print(logo)
        print(f"You're right! Current score {score + 1}")
        higherlower()
    else:
        print("sorry you lost!")

