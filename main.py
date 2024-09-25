# Rock, Paper, Scissors ASCII Art  --- GAME Rock, Paper, Scissors!
import random

rock= ("""
          _______
      ---'   ____)
           (_____)
           (_____)
            (____)
      ---.__(___)
   """)
paper =("""
               _______
          ---'    ____)____
                     ______)
                    _______)
                   _______)
          ---.__________)
          """)
scissors=("""
       _______
   ---'   ____)____
             ______)
          __________)
         (____)
   ---.__(___)
   """)

game_img= [rock ,paper,scissors]
while True:
    your_choice = int(input("choose rock :press'1' , paper : press'2' , scissors: press '3' \n"))
    if your_choice>3 :
        print("you typed an invalid number ")
    else:
        print("YOU  : ")
        if your_choice == 1:
             # Rock
            print(game_img[0])
        elif your_choice == 2 :
               # Paper
            print(game_img[1])

        else:
             # Scissors
            print(game_img[2])

        computer = random.randint(1, 3)
        print("COMPUTER : " )
        if computer == 1 :
             # Rock
            print(game_img[0])
        elif computer == 2 :
             # Paper
            print(game_img[1])
        elif computer==3:
              # Scissors
            print(game_img[2])

        print(f"computer chooses {computer}")
        if your_choice==computer:
            print("Play again")
        elif your_choice == 1 and computer == 3:
            print("you is the winner")
        elif your_choice == 2 and computer == 1:
            print("you is the winner")
        elif your_choice == 3 and computer == 2:
            print("you is the winner")
        else :
            print("you lose")