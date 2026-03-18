from Character import Character

class Novice(Character):
    def basicAttack(self, character):
        character.reduceHp(self.getDamage())
        print(f"{self.getUsername()} performed Basic attack -{self.getDamage()}")


username = input("Your Username: ")
user_character = Character(username)
print(user_character.getHp())

#For the novice section, I added encode the "username = input("your username")"
#to get the the user input and print their name and so as health. before 
#it print the health I encode the "print(user_character.getHp())" to print the
#health of 100 from the character.