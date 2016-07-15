import random 

class Alien():

  def __init__(self, name):
    self.name = name 
    self.life = 10
    self.distance = 15

  def attack(self, enemy):
    hit = random.randint(1,10)
    if hit >= 5:
      print("You hit the Human!")
      enemy.life -= 5
    else:
      print("The Alien shot at you but missed")

  def run(self):
    print("You are running to towards the ship")
    self.distance -= 5
