from Novice import Novice
import random

class Archer(Novice):
    def _init_(self, username):
        super()._init_(usernamne)
        self.setAgi(5)
        self.setInt(5)
        self.setVit(5)
        self.setHp(self.getHp()+self.getVit())
        
    def rangedAttack(self, character):
        self.new_damage = self.getDamage()+random.randint(0,self.getInt())
        character.reduceHp(self.new_damage)
        print(f"{self.getUsername()} performed range attack! -{self.new_damage}")
        
#Same as swordsman, I just copied the code from swordsman and the archer class
#got more attributes than swordsman, and I changed the "slash" to "range" attack
#because he is an archer, not swordsman.