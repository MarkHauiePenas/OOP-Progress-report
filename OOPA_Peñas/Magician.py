from Novice import Novice

class Magician(Novice):
    def __init__(self, username):
        super().__init__(username)
        self.setInt(10)
        self.setVit(5)
        self.setHp(self.getHp() + self.getVit())

    def heal(self):
        heal_amount = self.getInt()
        self.addHp(heal_amount)
        print(f"{self.getUsername()} performed Heal! +{heal_amount}")

    def magicAttack(self, character):
        new_damage = self.getDamage() + self.getInt()
        character.reduceHp(new_damage)
        print(f"{self.getUsername()} performed Magic Attack! -{new_damage}")
        
#This got more skills than the archer and swords, and so performing many actions