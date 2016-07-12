import random 

class Human():

  def __init__(self, name):
    self.name = name 
    self.life = 10

  def attack(self, enemy):
    hit = random.randint(1,10)
    if hit >= 5:
      print("You hit the enemy")
      enemy.life -= 5
      print(enemy.life)
    else:
      print("You missed")