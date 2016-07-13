import random 
from human import Human
from alien import Alien 

#Functions that are not critical to the playing of the game go here. 

def help():
  print("\n")
  print("This is a very simple text adventure game.")
  print("You will choose to play as either the human or the alien")
  print("The goal is to either kill your opponent or get to safety")
  print("For the human safety is the bunker for the alien it is its ship")
  print("Please be aware though that the game is based on random numbers")
  print("Thus, if you choose to shoot at your opponet it may not always hit the opponet")
  main()

#This function is where the human will battle it at with the alien. 
def human_battle():
  human = Human("Mike")
  alien = Alien("Blog")

  print("There is an alien in front of you")
  action = input("What will you do run to bunker or shot it? (run / shoot)")
  if action == "run":
    print("You are running")
    human.run()
  elif action == "shoot":
    print("You shoot at the alien")
    human.attack(alien)

#Main function that will start the game. 
def main():
  print("-----------------------")
  print("WELCOME TO ALIEN BATTLE")
  print("-----------------------")
  choice = input("Do you want to play (y/n/help) ")
  if choice == "y":
    human_battle()
  elif choice == "n":
    print("Hopefully you play soon!")
    print("In the meantime we'll miss you!") 
  elif choice == "help":
    help()


main()