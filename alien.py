import random 

class Alien():

  def __init__(self):
    self.lifeForce = 15
    self.distance = 15

  def alienAttack(self, human):
    hit = random.randint(1,10)
    if hit >= 5:
      print("The alien shots and hits the human")
      print("The human loses life!")
      human.health -= 5
    else:
      print("The alien shots but misses!")

  def run(self):
    print("You are running to towards the ship")
    self.distance -= 5

