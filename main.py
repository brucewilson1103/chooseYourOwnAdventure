
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure unscathed.") 
print('''
 
*******************************************************************************
 _                                     _     _                 _ 
| |                                   (_)   | |               | |
| |_ _ __ ___  __ _ ___ _   _ _ __ ___ _ ___| | __ _ _ __   __| |
| __| '__/ _ \/ _` / __| | | | '__/ _ \ / __| |/ _` | '_ \ / _` |
| |_| | |  __/ (_| \__ \ |_| | | |  __/ \__ \ | (_| | | | | (_| |
 \__|_|  \___|\__,_|___/\__,_|_|  \___|_|___/_|\__,_|_| |_|\__,_|
*******************************************************************************
''')
choice1 = input('You are walking down a dusty dirt trail when you come to a decaying old oak tree. The trail diverges into two paths. Which route would you like to take? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. Type "swim" to swim across. \n').lower()
  if choice2 == "wait":
    choice3 = input("You arrive at the island unharmed where you approach a large shape in the distance. It is a large shack with 3 different color doors. One red copper door with a red door knob, one yellow wooden door, and one entirely green metallic door. Which color do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of flames that consume you and the rest of the structure. Game Over.")
    elif choice3 == "yellow":
      print("You found a shimmering chest full of treasure! Congratulations! You Win!")
      print('''
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
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
      print("You found a shimmering chest full of treasure! Congratulations! You Win!")
    elif choice3 == "green":
      print("You enter a room of untamed beasts that attack. Game Over.")
    else:
      print("You chose a door that doesn't exist and are swept into a parallel universe. Game Over.")
  else:
    print("You are overtaken by the undertow and get swept away. Game Over.")
else:
  print("You begin walking down the trail when you step into quicksand. You can\'t escape.' Game Over.")