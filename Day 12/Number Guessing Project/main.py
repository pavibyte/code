import random
print("Welcome to the number GuessingGame!")
print("I'm thinking of a number between 1 to 100.")
user_input = input("choose a difficulty. Type 'easy' or 'hard':").lower()
random_number =  random.randint(1,100)
print(random_number)


def loop_fun():
    for i in range(0, attempt):
        guess = int(input("Make a guess:"))
        if guess == random_number:
            print(f"You got it! the answer is {guess}")
            return
        else:
            if guess < random_number:
                print("too low")

            else:
                print("too high")
        remaining_attempts = attempt - (i + 1)
        if remaining_attempts > 0:
            print(f"You have {remaining_attempts} attempts remaining.")
        else:
            print("You've run out of guesses. You lose!")


if user_input == "easy":
    attempt = 10
    print(f"you have {attempt} attempts remaining to guess the number.")
    loop_fun()
else:
    attempt = 5
    print(f"you have {attempt} attempts remaining to guess the number.")
    loop_fun()
