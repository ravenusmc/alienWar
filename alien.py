import random 

class Alien():

  def __init__(self, name):
    self.name = name 
    self.life = 10

  def attack(self, enemy):
    hit = random.randint(1,10)
    if hit >= 5:
      print("The Alien hits you")
      enemy.life -= 5
    else:
      print("The Alien shot at you but missed")