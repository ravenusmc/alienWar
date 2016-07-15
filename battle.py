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

def valid(choice):
  if choice == "y" or choice == "n" or choice == "help":
    return True
  else:
    return False

def validTwo(choice):
  if choice == 1 or choice == 2:
    return True
  else: 
    return False 

#### Main Game Functions Below Here #############

def chooseSide():
  print("Here you will choose your side.")
  print("1. Human")
  print("2. Alien")
  choice = int(input("Please enter the number of your side: "))
  while not validTwo(choice):
    choice = int(input("Please enter the number of your side: "))

  if choice == 1:
    human_battle()
  elif choice == 2:
    alien_battle()

#This function is where the human will battle the alien. 
def human_battle():
  human = Human("Mike")
  alien = Alien("Blob")

  print("There is an alien in front of you")
  action = input("What will you do run to bunker or shot it? (run / shoot): ")

  while human.distance > 0 or human.life > 0 or alien.life > 0:

    if action == "run":
      human.run()
      alien.attack(human)
    elif action == "shoot":
      human.attack(alien)
      alien.attack(human)

    if human.distance == 0:
      print("You made it to the bunker!")
      print("The Game is now over!")
      break
    elif human.life == 0:
      print("The Alien kills you!")
      print("The Game is now over!")
      break
    elif alien.life == 0:
      print("You killed the Alien!")
      print("The Game is now over!")
      break

    print("Distance to bunker is: " + str(human.distance) + " feet!")
    print("Human Life is: " + str(human.life))
    print("Alien life is: " + str(alien.life)) 

    action = input("What will you do run to bunker or shot it? (run / shoot) ")

#This function is where the alien will battle the human. 
def alien_battle():
  human = Human("Mike")
  alien = Alien("Blob")

  print("There is an human in front of you")
  action = input("What will you do run to ship or shot the human? (run / shoot): ")

  while alien.distance > 0 or human.life > 0 or alien.life > 0:

    if action == "run":
      alien.run()
      human.attack(human)
    elif action == "shoot":
      alien.attack(human)
      human.attack(alien)
      

    if alien.distance == 0:
      print("You made it to the ship!")
      print("The Game is now over!")
      break
    elif human.life == 0:
      print("You killed the human!")
      print("The Game is now over!")
      break
    elif alien.life == 0:
      print("The human kills you!")
      print("The Game is now over!")
      break

    print("Distance to ship is: " + str(alien.distance) + " feet!")
    print("Human Life is: " + str(alien.life))
    print("Alien life is: " + str(human.life)) 

    action = input("What will you do run to bunker or shot the human? (run / shoot) ")


#Main function that will start the game. 
def main():
  print("-----------------------")
  print("WELCOME TO ALIEN BATTLE")
  print("-----------------------")
  choice = input("Do you want to play (Y/N/help) ")
  while not valid(choice):
    choice = input("Do you want to play (Y/N/help) ")
  if choice.lower() == "y":
    chooseSide()
  elif choice.lower() == "n":
    print("Hopefully you play soon!")
    print("In the meantime we'll miss you!") 
  elif choice == "help":
    help()


main()