from swordsman import Swordsman
from Archer import Archer
from Magician import Magician

class Boss(swordsman, Archer, Magician):
    def _init_(self, username):
        super()._init_(username)
        self.setStr(10)
        self.setVit(25)
        self.setInt(5)
        self.setHp(self.getHp()+self.getVit())
        
#THis inherit the swordsman, magician, and archer, as a boss, mixing its attributes, and having their skills.