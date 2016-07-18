import random 

class Human():

  def __init__(self):
    self.health = 15
    self.distance = 15

  def attack(self, enemy):
    hit = random.randint(1,10)
    if hit >= 5:
      print("The human shoots at the alien")
      print("The alien loses life!")
      enemy.lifeForce -= 5
    else:
      print("The human shoots but misses!")

  def run(self):
    print("You are running to towards the bunker")
    self.distance -= 5
