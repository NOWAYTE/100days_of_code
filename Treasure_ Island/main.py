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
 _________|___________| ;`-.o`"=._; ." ` '`."` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/''')
print("welcome to the treaure island\nyour mission is to find the treasure")
choice1 = input("""     .
              :  
             ' _ '
         -= ( (_) ) =-
             .   .
            /  :  \
        .-.    '
        |.|
      /)|`|(\
     (.(|'|)`) <-----         ------>
  ~~~~`\`'./'~~~~~~~|~~~~~~~|~~~~~~~~~~~~~~~~
  jgs   |.|         |  ~~   |
        |`|         |       |           ~~
       ,|'|.      (_)          ~~
        "'"        \"\
             ~~     ^~^
you are at crossroad where do you want to go??\n'right' or 'left'\n
""").lower()
if choice1 == "left":
    choice2 = input(""""
                    seems like you survived this time ..the treasure palace is across the river
                    'wait for a boat ' or 'swim'\n----->
                    """)
    if choice2 == "wait for a boat":
        choice3 = input("""
        you are so lucky you made it through...There are three door at the entrance of the treasure palace
         ______________
| ___________ /|
| |  _ _ _ _  | |
| | | | | | | | |
| | |-+-+-+-| | |
| | |-+-+=+%| | |
| | |_|_|_|_| | |
| |    ___    | |
| |   [___] ()| |

| |         ||| |
| |         ()| |
| |           | |
| |           | |
| |           | |
|_|____RED_______|_| 
          ______________
| ___________ /|
| |  _ _ _ _  | |
| | | | | | | | |
| | |-+-+-+-| | |
| | |-+-+=+%| | |
| | |_|_|_|_| | |
| |    ___    | |
| |   [___] ()| |

| |         ||| |
| |         ()| |
| |           | |
| |           | |
| |           | |
|_|____BLACK_______|_| 
  ______________
| ___________ /|
| |  _ _ _ _  | |
| | | | | | | | |
| | |-+-+-+-| | |
| | |-+-+=+%| | |
| | |_|_|_|_| | |
| |    ___    | |
| |   [___] ()| |

| |         ||| |
| |         ()| |
| |           | |
| |           | |
| |           | |
|_|___WHITE________|_|
choose one \n---->
        """).lower()
        if choice3 == "white":
            choice4 = input(
                """you are damn lucky ....There are two boxes one of which has the treasure choose one
                                            +------+     +------+.
                                            |\     |\    |`.    | `.
                                            | +----+-+   |  `+--+---+
                                            | |    | |   |   |  |   |
                                            +-+----+ |   +---+--+   |
                                            \|     \|    `. |       |
                                             +------+      `+------+           
                                               A                B
            """).lower()
            if choice4 == "A":
                print("came all this way to loose...oops! Game over")
            else:
                print("""
                 ,--.     ,--.
 (  O )   (  O )
  `--'  \  `--'
         \   _
   >-.   /   /| 
      `-.__.'
                played you.....Anyway here is the real deal ...
                YOU ARE THE REAL TREASURE .....WORK ON YOURSELF
                """)
        elif choice3 == "black":
            print("busted dumbass ....Game over")
        elif choice3 == "red":
            print("never choose red doofus....Game over ")
        else:
            print("are you blind or what?...")
    else:
        print("seems like you dont know how to swim SUCKER...GAME OVER")
else:
    print("Dude did you just die in the first round")
