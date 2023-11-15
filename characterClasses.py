import sys
from enemyClasses import *

class baseClass:
    """Base class other classes inherit from."""
    def __init__(self, cname):
        self.name = cname
    """ Set up basic stats. """
    level = 1
    playerClass = ""
    currentHealth = 0
    maxHealth = 0
    attack = 0
    mattack = 0
    defense = 0
    mdefense = 0
    speed = 0
    experience = 0
    maxLevel = 30
    numHealthPotions = 1
    maxHealthPotions = 3

    """ Called when the character is defeated. """
    def characterHasDied():
        print("Game Over.")
        sys.exit(0)

    """ Called when the character wins the game """
    def characterHasWon():
        print("You have reached the end of the road congratulations traveler.")
        sys.exit(0)

    def validateMove(self):
        print("It is now your turn what will you do?")
        selection = input("Press: 1 for Attack, 2 for Magic Attack, or 3 to Heal: ")
        if selection == "1":
            return "Attack"
        elif selection == "2":
            return "Magic Attack"
        elif selection == "3":
            if self.numHealthPotions == 0:
                print("No portions left.")
                self.validateMove()
            if self.currentHealth == self.maxHealth:
                print("Already at full health.")
                self.validateMove()
            return "Heal"
        else:
            print("Please select a valid option: ")
            self.validateMove()
    
    def healthProgress(self):
        fraction = f"{self.currentHealth}/{self.maxHealth}"
        print(f"Your current health is:          {fraction}")
    
    def showStats(self):
        max_width = 4
        print(f"Level:                   {str(self.level).rjust(max_width)}")
        print(f"Current Health:          {str(self.currentHealth).rjust(max_width)}")
        print(f"Max Health:              {str(self.maxHealth).rjust(max_width)}")
        print(f"Attack:                  {str(self.attack).rjust(max_width)}")
        print(f"Magic Attack:            {str(self.mattack).rjust(max_width)}")
        print(f"Defense:                 {str(self.defense).rjust(max_width)}")
        print(f"Magic Defense:           {str(self.mdefense).rjust(max_width)}")
        print(f"Speed:                   {str(self.speed).rjust(max_width)}")
        print(f"Health Potions:          {str(self.numHealthPotions).rjust(max_width)}")
    
    def levelUp(self):
        print("TO BE IMPLEMENTED IN EACH CLASS.")

    # Experience system for the player.
    def gainExperience(self, xp):
        if self.level < self.maxLevel:
            self.experience = self.experience + xp
            xpNeeded = 50 * self.level
            
            if self.experience >= xpNeeded:
                self.experience = self.experience % xpNeeded
                self.levelUp()
                print("You have leveled up you are now level:  ", self.level)
                self.showStats()
            else:
                fraction = f"{self.experience}/{xpNeeded}"
                print(f"Experince progress:          {fraction}")
        
    def playerTurn():
        print("TO BE IMPLEMENTED IN EACH CLASS.")

    
class Solider(baseClass):
    playerClass = "solider"
    currentHealth = 100
    maxHealth = 100
    attack = 8
    mattack = 1
    defense = 15
    mdefense = 1
    speed = 5

    def playerTurn(self, enemy):
        choice = self.validateMove()
        if choice == "Attack":
            print("You lunge forward swinging your mighty sword.")
            enemy.currentHealth = enemy.currentHealth - self.attack
        elif choice == "Magic Attack":
            print("You utter a spell you remembered from your failed magic course.")
            enemy.currentHealth = enemy.currentHealth - self.mattack
        elif choice == "Heal":
            print("You use a health potion.")
            self.currentHealth = self.maxHealth
            self.numHealthPotions -= 1
            print(f"Current Health:          {str(self.currentHealth).rjust(4)}")
            print(f"Health Potions:          {str(self.numHealthPotions).rjust(4)}")
        if enemy.currentHealth <= 0:
            print("You have slain the enemy.")
            self.gainExperience(enemy.xpValue)
        else:
            enemy.healthProgress()
        return self

    def levelUp(self):
        self.level += 1
        
        if self.level % 2 == 0:
            """ On even level ups add to health. """
            self.maxHealth += 5
        
        if self.level % 5 == 0:
            """ Every five levels add to attack, defense and magic defense. """
            self.attack += 2
            self.defense += 2
            self.mdefense += 2
        
        if self.level % 15 == 0:
            """ Every 15 levels add to magic attack. """
            self.mattack += 1
        
        if self.level % 7 == 0:
            """ Every four levels add to speed """
            self.speed += 1
        """ Level up back to max health """
        self.currentHealth = self.maxHealth

class Archer(baseClass):
    playerClass = "archer"
    currentHealth = 80
    maxHealth = 80
    attack = 10
    mattack = 5
    defense = 5
    mdefense = 5
    speed = 7

    def playerTurn(self, enemy):
        choice = self.validateMove()
        if choice == "Attack":
            print("You step back and lauch an arrow.")
            enemy.currentHealth = enemy.currentHealth - self.attack
        elif choice == "Magic Attack":
            print("You cast off a basic nature spell.")
            enemy.currentHealth = enemy.currentHealth - self.mattack
        elif choice == "Heal":
            print("You use a health potion.")
            self.currentHealth = self.maxHealth
            self.numHealthPotions -= 1
            print(f"Current Health:          {str(self.currentHealth).rjust(4)}")
            print(f"Health Potions:          {str(self.numHealthPotions).rjust(4)}")
        if enemy.currentHealth <= 0:
            print("You have slain the enemy.")
            self.gainExperience(enemy.xpValue)
        else:
            enemy.healthProgress()
        return self
    
    def levelUp(self):
        self.level += 1
        
        if self.level % 2 == 0:
            """ On even level ups add to health. """
            self.maxHealth += 2
        
        if self.level % 5 == 0:
            """ Every 5 levels add to attack stats. """
            self.attack += 3
            self.mattack += 1
        
        if self.level % 7 == 0:
            """ Every five levels add to defense and magic defense. """
            self.defense += 1
            self.mdefense += 1
        
        if self.level % 4 == 0:
            """ Every four levels add to speed """
            self.speed += 2
        
        """ Level up back to max health """
        self.currentHealth = self.maxHealth

class Mage(baseClass):
    playerClass = "mage"
    currentHealth = 70
    maxHealth = 70
    attack = 1
    mattack = 10
    defense = 5
    mdefense = 10
    speed = 7

    def playerTurn(self, enemy):
        choice = self.validateMove()
        if choice == "Attack":
            print("You weakly swing out you staff grazing the enemy.")
            enemy.currentHealth = enemy.currentHealth - self.attack
        elif choice == "Magic Attack":
            print("You gather your magic unleashing an elemental attack.")
            enemy.currentHealth = enemy.currentHealth - self.mattack
        elif choice == "Heal":
            print("You use a health potion.")
            self.currentHealth = self.maxHealth
            self.numHealthPotions -= 1
            print(f"Current Health:          {str(self.currentHealth).rjust(4)}")
            print(f"Health Potions:          {str(self.numHealthPotions).rjust(4)}")
        if enemy.currentHealth <= 0:
            print("You have slain the enemy.")
            self.gainExperience(enemy.xpValue)
        else:
            enemy.healthProgress()
        return self

    def levelUp(self):
        self.level += 1
        
        if self.level % 2 == 0:
            """ On even level ups add to health. """
            self.maxHealth += 2
        
        if self.level % 5 == 0:
            """ Every 5 levels add to attack stats. """
            self.attack += 1
            self.mattack += 3
        
        if self.level % 7 == 0:
            """ Every five levels add to defense and magic defense. """
            self.defense += 1
            self.mdefense += 1
        
        if self.level % 4 == 0:
            """ Every four levels add to speed """
            self.speed += 2
        
        """ Level up back to max health """
        self.currentHealth = self.maxHealth