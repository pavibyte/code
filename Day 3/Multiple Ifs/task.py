print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
bill = 0

if height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age? "))
    if age <= 12:
        bill = 5
        print(" $5.")
    elif age <= 18:
        bill = 7
        print(" $7.")
    else:
        bill = 12
        print(" $12.")

    photo = input("do you need a photo yes or no:")
    if photo == "yes":
        bill += 3
    print("your bill is $",bill)
else:
    print("Sorry you have to grow taller before you can ride.")
