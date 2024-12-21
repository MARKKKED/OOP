class Player:
  def __init__(self, name, health, attack_power):
    self.name = name
    self.health = health
    self.attack_power = attack_power

  def attack(self, target):
    print(f"{self.name} attacks {target.name} for {self.attack_power} damage.")
    target.health -= self.attack_power
    print(f"{target.name} now has {target.health} health left.")
  
  def heal(self, amount):
    self.health += amount
    print(f"{self.name} heals for {amount} health, now has {self.health} health left.")

player1 = Player("Alice", 100, 20)
player2 = Player("Bob", 80, 30)

while player1.health > 0 and player2.health > 0:
  player1.attack(player2)
  if player2.health <= 0:
    print(f"{player1.name} wins!")
    break
  player2.attack(player1)
  if player1.health <= 0:
    print(f"{player2.name} wins!")
    break

player1.heal(10)