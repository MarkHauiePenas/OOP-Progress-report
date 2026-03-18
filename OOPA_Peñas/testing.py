from Swordsman import Swordsman
from Archer import Archer
from Magician import Magician

Character1 = Swordsman("Royce")
Character2 = Magician("Archie")

print(f"{Character1.getUsername()} HP: {Character1.getHp()}")
print(f"{Character2.getUsername()} HP: {Character2.getHp()}")

Character1.slashattack(Character2)
Character1.basicAttack(Character2)

print(f"{Character1.getUsername()} HP: {Character1.getHp()}")
print(f"{Character2.getUsername()} HP: {Character2.getHp()}")

Character2.heal()
Character2.magicAttack(Character1)

print(f"{Character1.getUsername()} HP: {Character1.getHp()}")
print(f"{Character2.getUsername()} HP: {Character2.getHp()}")

#Following the instruction rules, I type for what the instructions says and im running out of time