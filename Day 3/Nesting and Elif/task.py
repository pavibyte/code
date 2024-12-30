print("Welcome to the rollercoaster!")
height = int(input("What is your height in cm? "))
age = int(input("enter your age:"))

if height >= 120:
    print("You can ride the rollercoaster")
    if age < 12:
        print("$2")
    elif age>=12 or age<=18:
        print("$7")
    else:
        print("$12")
else:
    print("Sorry you have to grow taller before you can ride.")
