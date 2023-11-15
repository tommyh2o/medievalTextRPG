from characterClasses import *
from enemyClasses import *
from random import randrange

def engageInBattle(player):
    difficulty = 0
    if player.level >=10:
        difficulty = 1
    if player.level >= 20:
        difficulty = 2
    
    findEnemy = enemySelection()
    enemy = baseEnemyClass(difficulty)
    if findEnemy == 0:
        enemy = Goblin(difficulty)
        enemy.scaleStats()
    elif findEnemy == 1:
        enemy = Witch(difficulty)
        enemy.scaleStats()
    elif findEnemy == 2:
        enemy = Troll(difficulty)
        enemy.scaleStats()
    elif findEnemy == 3:
        enemy = Dragon(difficulty)
    
    # Now that an opponent is present do battle.
    return battleManager(player=player, enemy=enemy)

# Randomly select an opponet with weighted odds
def enemySelection():
    selection = randrange(0, 100)
    if selection <= 60:
        print("Your opponent is a goblin.")
        return 0
    elif selection <= 85:
        print("Your opponent is a witch.")
        return 1
    elif selection <= 99:
        print("Your opponent is a troll.")
        return 2
    else:
        print("You are now facing the fearsome dragon...farewell.")
        return 3

def battleManager(player, enemy):
    print(player.name)
    while player.currentHealth > 0 and enemy.currentHealth > 0:
        if player.speed >= enemy.speed:
            player.playerTurn(enemy)
            enemy.enemyTurn(player)
        else:
            enemy.enemyTurn(player)
            player.playerTurn(enemy)
    return player

x = Solider("Tommy")
x.levelUp()
y = Dragon(0)
battleManager(x, y)