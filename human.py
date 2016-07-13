import random 

class Human():

  def __init__(self, name):
    self.name = name 
    self.life = 10
    self.distance = 15

  def attack(self, enemy):
    hit = random.randint(1,10)
    if hit >= 5:
      print("You hit the enemy")
      enemy.life -= 5
      print(enemy.life)
    else:
      print("You missed")

  def run(self):
    print("You are running to towards the bunker")
    self.distance -= 3
    print("Distance to the bunker is " + str(self.distance) + " feet")