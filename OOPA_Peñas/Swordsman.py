from Novice import Novice

class Swordsman(Novice):
    def _init_(self, username):
        super()._init_(usernamne)
        self.setStr(5)
        self.setVit(10)
        self.setHp(self.getHp()+self.getVit())
        
    def slashattack(self, character):
        self.new_damage = self.getDamage()+self.getStr()
        character.reduceHp(self.new_damage)
        print(f"{self.getUsername()} performed Slash attack! -{self.new_damage}")
        
#Therefore, I just copied the code from the instruction, and the "slashattack"
#will perform some actions later.