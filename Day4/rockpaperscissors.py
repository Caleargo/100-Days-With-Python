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

game_input = [rock, paper, scissors]

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >= 0 and user_choice <= 2:
    print(game_input[user_choice])

machine_choice = random.randint(0, 2 )
print("Computer chose:")
print(game_input[machine_choice])

if user_choice >= 3 or user_choice < 0:
    print("You print an invalid number\n"
          "You lose")
elif user_choice == 0 and machine_choice == 2:
    print("You win")
elif machine_choice == 0 and user_choice == 2:
    print("You lose")
elif machine_choice > user_choice:
    print("You lose")
elif user_choice > machine_choice:
    print("You win")
elif user_choice == machine_choice:
    print("It's a draw")
