import random 
from human import Human
from alien import Alien 

def test():
  human = Human("Mike")
  alien = Alien("Blog")

  human.attack(alien)

def main():
  print("----------------")
  print("WELCOME TO ALIEN BATTLE")
  print("----------------")
  choice = input("Do you want to play (y/n) ")
  if choice == "y":
    test()
  else:
    print("Hopefully you play soon!")
    print("In the meantime we'll miss you!") 


main()