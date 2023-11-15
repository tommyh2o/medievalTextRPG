import math
from random import randrange
from characterClasses import *

class baseEnemyClass:
    """Base class other classes inherit from."""
    def __init__(self, scale):
        self.scale = scale

    """ Set up basic stats. """
    currentHealth = 0
    maxHealth = 0
    attack = 0
    mattack = 0
    defense = 0
    mdefense = 0
    speed = 0
    xpValue = 0

    def enemyTurn():
        print("TO BE IMPLEMENTED IN EACH CLASS.")

    # Enemies mobs get stronger every ten levels
    def scaleStats(self):
        self.maxHealth = self.maxHealth + (math.ceil(self.maxHealth * (self.scale / 2)))
        self.attack    = self.attack    + (math.ceil(self.attack    * (self.scale / 2)))
        self.mattack   = self.mattack   + (math.ceil(self.mattack   * (self.scale / 2)))
        self.defense   = self.defense   + (math.ceil(self.defense   * (self.scale / 2)))
        self.mdefense  = self.mdefense  + (math.ceil(self.mdefense  * (self.scale / 2)))
        self.speed     = self.speed     + (math.ceil(self.speed * (self.scale / 2)))
        self.xpValue   =  self.xpValue  * (self.scale + 1)
        self.currentHealth = self.maxHealth
    
    def healthProgress(self):
        print(" ")

    # For debugging purposes
    def showStats(self):
        max_width = 4
        print(f"Current Health:          {str(self.currentHealth).rjust(max_width)}")
        print(f"Max Health:              {str(self.maxHealth).rjust(max_width)}")
        print(f"Attack:                  {str(self.attack).rjust(max_width)}")
        print(f"Magic Attack:            {str(self.mattack).rjust(max_width)}")
        print(f"Defense:                 {str(self.defense).rjust(max_width)}")
        print(f"Magic Defense:           {str(self.defense).rjust(max_width)}")
        print(f"Speed:                   {str(self.speed).rjust(max_width)}")
        print(f"Xp Value:                {str(self.xpValue).rjust(max_width)}")

class Goblin(baseEnemyClass):
    currentHealth = 40
    maxHealth = 40
    attack = 5
    mattack = 2
    defense = 3
    mdefense = 2
    speed = 6
    xpValue = 10

    def healthProgress(self):
        fraction = f"{self.currentHealth}/{self.maxHealth}"
        print(f"Goblins current health is:          {fraction}")

    def enemyTurn(self, player):
        if self.currentHealth > 0:
            goblinMove = randrange(0, 10)
            if goblinMove < 9:
                print("The goblin leapt forward and swung his dagger.")
                player.currentHealth = player.currentHealth - self.attack
            else:
                print("The goblin muttered a weak spell.")
                player.currentHealth = player.currentHealth - self.mattack
            
            if player.currentHealth < 0:
                print("The goblin has slain you")
                player.characterHasDied()
            else:
                player.healthProgress()
        
        

class Witch(baseEnemyClass):
    currentHealth = 50
    maxHealth = 50
    attack = 1
    mattack = 7
    defense = 4
    mdefense = 6
    speed = 6
    xpValue = 20

    def healthProgress(self):
        fraction = f"{self.currentHealth}/{self.maxHealth}"
        print(f"The Witche's current health is:          {fraction}")

    def enemyTurn(self, player):
        if self.currentHealth > 0:
            witchMove = randrange(0, 100)
            if witchMove < 90:
                print("The witch lauches a psychic attack!")
                player.currentHealth = player.currentHealth - self.mattack
            elif witchMove < 99:
                print("The witch swings her staff at you.")
                player.currentHealth = player.currentHealth - self.attack
            else:
                print("The witch summons down lighting vaporizing you instantly.")
                player.characterHasDied()
            
            if player.currentHealth < 0:
                print("The witch has slain you")
                player.characterHasDied()
            else:
                player.healthProgress()

class Troll(baseEnemyClass):
    currentHealth = 100
    maxHealth = 100
    attack = 8
    mattack = 1
    defense = 8
    mdefense = 1
    speed = 3
    xpValue = 40
        
    def healthProgress(self):
        fraction = f"{self.currentHealth}/{self.maxHealth}"
        print(f"The Troll's current health is:          {fraction}")
    
    def enemyTurn(self, player):
        if self.currentHealth > 0:
            trollMove = randrange(0, 100)
            if trollMove < 60:
                print("Smashes his club against the floor launching you upwards.")
                player.currentHealth = player.currentHealth - self.attack
            elif trollMove < 80:
                print("The troll belches in your direction.")
                player.currentHealth = player.currentHealth - self.mattack
            elif trollMove < 90:
                print("The troll summons rocks around it increasing its defense.")
                self.defense = self.defense + 5
            else:
                print("The troll strikes a critical hit dealing double damage.")
                player.currentHealth = player.currentHealth - (self.attack * 2)
            
            if player.currentHealth < 0:
                print("The troll has slain you")
                player.characterHasDied()
            else:
                player.healthProgress()

class Dragon(baseEnemyClass):
    currentHealth = 250
    maxHealth = 250
    attack = 20
    mattack = 20
    defense = 20
    mdefense = 20
    speed = 20
    xpValue = 1500

    def healthProgress(self):
        fraction = f"{self.currentHealth}/{self.maxHealth}"
        print(f"The dragon's current health is:          {fraction}")
    
    def enemyTurn(self, player):
        if self.currentHealth > 0:
            dragonMove = randrange(0, 100)
            if dragonMove < 35:
                print("The dragon smashes his claw into slamming you into a wall.")
                player.currentHealth = player.currentHealth - self.attack
            elif dragonMove < 70:
                print("The dragon spews flames engulfing you in fire.")
                player.currentHealth = player.currentHealth - self.mattack
            elif dragonMove < 80:
                print("The dragon smashes into you from above dealing massive damage.")
                player.currentHealth = player.currentHealth - (self.attack * 2)
            elif dragonMove < 90:
                print("The dragon charges at you surrounding itself in flames.")
                player.currentHealth = player.currentHealth - self.attack
                player.currentHealth = player.currentHealth - self.mattack
            elif dragonMove < 100:
                print("The dragon coils up healing and bolstering its defense.")
                self.currentHealth += 10
                self.defense += 5
                self.mdefense += 5
            else:
                print("The dragon submits to your strength admitting defeat and flying away")
                player.characterHasWon()
            
            if player.currentHealth < 0:
                print("Your battle ends with the smell of burnt flesh lingering in the air.")
                player.characterHasDied()
            else:
                player.healthProgress()
