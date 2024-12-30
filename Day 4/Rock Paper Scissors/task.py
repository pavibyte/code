import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
lists = [rock, paper, scissors]
choice = int(input("choose 1,2,3 for rock,paper, scissor respectively"))
if choice == 0:
    print(rock)
elif choice == 1:
    print(paper)
elif choice == 2:
    print(scissors)
else:
    print("wrong number input")

print("computer choice")
a = random.choice(lists)
print(a)
b = lists.index(a)
print(b)

if choice == b:
    print("match draw")
elif choice == 0 and b == 1:
    print("computer won")
elif choice == 0 and b == 2:
    print("you won")
elif choice == 1 and b == 0:
    print("you won")
elif choice == 1 and b == 2:
    print("computer won")
elif choice == 2 and b == 0:
    print("computer wins")
elif choice == 2 and b == 1:
    print("you won")
else:
    print("wrong input")
