from characterClasses import *
from battleMode import *
from random import randrange

def main():
    print("""
        Welcome, intrepid traveler, to a world where mystery and adventure converge. 
        Unveil the secrets of uncharted realms, face daunting challenges, and forge your destiny. 
        As you step into the unknown, remember: every choice you make shapes the unfolding tale. 
        Are you ready to embark on a legendary journey? 
        The adventure begins now.
            """)
    
    # Get player input such as name and class.
    characterName = input("Traveler what is your name? ")
    characterClass = chooseAClass()

    player = baseClass(characterName)
    if characterClass == "solider":
        player = Solider(characterName)
    elif characterClass == "archer":
        player = Archer(characterName)
    elif characterClass == "mage":
        player = Mage(characterName)
    player.showStats()   
    # Main loop that progresses the game until max level is reached.
    while player.level < player.maxLevel:
        lorR = crossroad()
        if lorR == "left":
            leftChoice(player)
        elif lorR == "right":
            rightChoice(player)
    
# Function for allowing the player to select their class.
def chooseAClass():
    characterClass = input("Choose your class: Solider, Archer, or Mage. ").lower()
    if characterClass == "solider":
        print("You have chosen to be a brave solider.")
        return characterClass
    elif characterClass == "archer":
        print("You have chosen to be a daring archer.")
        return characterClass
    elif characterClass == "mage":
        print("You have chosen to be a cunning mage.")
        return characterClass
    else:
        print("You must choose one of the three classes.")
        return chooseAClass()

# Function for getting player to make a choice to go left or right.
def crossroad():
    print("You arrive at a crossroad you must choose to go left or right.")
    choice = input("Right or left? ").lower()
    if choice == "left":
        print("You have chosen to go left.")
        return choice
    elif choice == "right":
        print("You have chosen to go right.")
        return choice
    else:
        print("Please type left or right to make your decision.")
        return crossroad()
    
# Function called when player chooses to go left.
def leftChoice(player):
    path = randrange(0, 10)
    match path:
        case 0 | 1 | 2 | 3 | 4 | 5 | 6:
            print("You have encountered an enemy.")
            engageInBattle(player)
        case 7 | 8:
            wizardBehavior(player)
        case 9 | 10:
            print("You make your way into the city and find a shop.")

def wizardBehavior(player):
    print("You have encountered an old wizard.")
    

# Function called when player chooses to go right.
def rightChoice(player):
    print("Right choice.")

if __name__ == "__main__":
    main()