from art import logo
import random
play = input("Do you want to play a game of Blackjack? Type 'y' or 'n':").lower()
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
def blackjack():
    if play == "y":
        print("\n"*25)
        print(logo)
        random_2_values = []
        random_2_values = random.choices(cards,k=2)
        total = sum(random_2_values)
        print(f"your cards :{random_2_values} , current score: {total}")
        computer_1 = random.choices(cards)
        computer_2 = random.choices(cards)
        print(f"Computer's first card: {computer_1}")
        if total == 21:
            print("you win")
        else:
            play2 = input("Type 'y' to get another card, type 'n' to pass:").lower()
            if play2 == "y":
                random_1_value = random.choices(cards)
                new_list = random_2_values + random_1_value
                total = sum(new_list)
                print(f"Your cards: {new_list} current score: {total}")
                print(f"Computer's first card: {computer_2}")
                print(f"Your final hand: {new_list} ,final score: {total}")
                computer_sum2 = sum(computer_1 + computer_2)
                if computer_sum2 < 17:
                    global computer_3
                    computer_3 = random.choices(cards)
                    global computer_sum3
                    computer_sum3 = computer_1 +computer_2 + computer_3
                    print(f"Computer's final hand: {computer_1 +computer_2 + computer_3} , final score:{sum(computer_sum3)}")
                else:
                    print(f"Computer's final hand: {computer_1 + computer_2} , final score:{computer_sum2}")
                global final_check
                def final_check():
                    if total > 21:
                        print("you went over. you lose 😭")
                    elif total < 21:
                        if computer_3:
                            element = computer_sum3[0]
                            if total > element:
                                print("you went over. you lose 😭")
                        else:
                            if total >computer_sum2:
                                print("you went over. you lose 😭")
                    else:
                        print("Opponent went over. You win 😁")
                final_check()
                round_2 = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
                if round_2 == "y":
                    blackjack()

            else:
                print(f"Your final hand: {random_2_values} ,final score: {total}")
                print(f"Computer's final hand: {computer_1 + computer_2 + computer_3} , final score:{computer_1[0]+computer_2[0]+computer_3[0]}")
            final_check()
blackjack()







