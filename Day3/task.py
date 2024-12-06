print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

choice1 = input("You see a trial, and there are two paths, which one do you chose, left or right?\n").lower()
if choice1 == "left":
    choice2 = input('You entered in a small hole and get out into a small cave with'
                     'a swamp inside of it, what do you do? swim or wait\n').lower()
    if choice2 == "wait":
        choice3 = input('You waited successfully and you noticed there are a small light on your right.'
                        'You walk to see what is it and you find three doors. Which one do you open? '
                        'red, yellow or blue\n').lower()
        if choice3 == "yellow":
            print("Congratulations, you are proclaimed the new Indiana Jones and receive the best reward on earth")
            print("You successfully win !!")
        elif choice3 == "red":
            print("You opened the reed door and a big flame devoured you right away, consuming and killing you")
            print("GAME OVER")
        elif choice3 == "blue":
            print("You opened the blue door and see five beast that ate you as soon as they see you")
            print("GAME OVER")
        else:
            print("You ran out of options, you waited that much that a rock fell into you, killing you")
            print("GAME OVER")
    else:
        print("You swam over the swamp when you noticed a enormous trout that eat you alive")
        print("GAME OVER")
else:
    print("You turn right and fell into a hole because the floor was fake, killing you instantly")
    print("GAME OVER")
