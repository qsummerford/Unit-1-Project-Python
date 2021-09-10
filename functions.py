from dataclasses import dataclass
import random

inventory = []


@dataclass
class Enemy:
    health: int
    attack1: int
    attack2: int
    is_dead: bool


@dataclass
class Player:
    health: int
    attack1: int
    attack2: int
    is_dead: bool


enemy = Enemy(0, 0, 0, False)
player = Player(30, 0, 0, False)
is_dead = False


def combat(enemy: Enemy, player: Player, currentRoom, location):
    goblin_attack = random.randint(0, 1)
    archer_attack = random.randint(0, 1)
    warrior_attack = random.randint(0, 1)
    knight_attack = random.randint(0, 1)
    warden_attack = random.randint(0, 1)
    enemychance = random.randint(1, 10)
    if 'Gobbo' in location[currentRoom]:
        if goblin_attack == 0 and (enemychance > 3 and enemychance <= 10):
            player.health -= enemy.attack1
            print('Goblin used stab!')
            goblin_attack = random.randint(0, 1)
        elif goblin_attack == 1 and (enemychance > 3 and enemychance <= 10):
            player.health -= enemy.attack2
            print("Goblin used bite!")
            goblin_attack = random.randint(0, 1)
        elif goblin_attack == 0 and enemychance <= 3:
            print('The Goblin missed!')
            goblin_attack = random.randint(0, 1)
        elif goblin_attack == 1 and enemychance <= 3:
            print('The Goblin missed!')
            goblin_attack = random.randint(0, 1)
        else:
            print('The Goblin missed!')
    elif 'David' in location[currentRoom]:
        if archer_attack == 0 and (enemychance > 3 and enemychance <= 10):
            player.health -= enemy.attack1
            print('Archer shot you with an arrow!')
            archer_attack = random.randint(0, 1)
        elif archer_attack == 1 and (enemychance > 3 and enemychance <= 10):
            player.health -= enemy.attack2
            print("Archer used short sword stab!")
            archer_attack = random.randint(0, 1)
        elif archer_attack == 0 and enemychance <= 3:
            print('The Archer missed!')
            archer_attack = random.randint(0, 1)
        elif archer_attack == 1 and enemychance <= 3:
            print('The Archer missed!')
            archer_attack = random.randint(0, 1)
        else:
            print('The Archer missed!')
    elif 'Steve' in location[currentRoom]:
        if warrior_attack == 0 and (enemychance > 3 and enemychance <= 10):
            player.health -= enemy.attack1
            print('Warrior used shield bash!')
            warrior_attack = random.randint(0, 1)
        elif warrior_attack == 1 and (enemychance > 3 and enemychance <= 10):
            player.health -= enemy.attack2
            print("Warrior used mace swing!")
            warrior_attack = random.randint(0, 1)
        elif warrior_attack == 0 and enemychance <= 3:
            print('The Warrior missed!')
            warrior_attack = random.randint(0, 1)
        elif warrior_attack == 1 and enemychance <= 3:
            print('The Warrior missed!')
            warrior_attack = random.randint(0, 1)
        else:
            print('The Warrior missed!')

    elif 'Harold' in location[currentRoom]:
        if knight_attack == 0 and (enemychance > 3 and enemychance <= 10):
            player.health -= enemy.attack1
            print('Knight used stab!')
            knight_attack = random.randint(0, 1)
        elif knight_attack == 1 and (enemychance > 3 and enemychance <= 10):
            player.health -= enemy.attack2
            print("Knight used hilt strike!")
            knight_attack = random.randint(0, 1)
        elif knight_attack == 0 and enemychance <= 3:
            print('The Knight missed!')
            knight_attack = random.randint(0, 1)
        elif knight_attack == 1 and enemychance <= 3:
            print('The Knight missed!')
            warrior_attack = random.randint(0, 1)
        else:
            print('The Knight missed!')

    elif 'Arthur' in location[currentRoom]:
        if warden_attack == 0 and (enemychance > 3 and enemychance <= 10):
            player.health -= enemy.attack1
            print('Warden used keyboard attack!')
            warden_attack = random.randint(0, 1)
        elif warden_attack == 1 and (enemychance > 3 and enemychance <= 10):
            player.health -= enemy.attack2
            print("Nate used coffee splash!")
            warden_attack = random.randint(0, 1)
        elif warden_attack == 0 and enemychance <= 3:
            print('Nate missed!')
            warden_attack = random.randint(0, 1)
        elif warden_attack == 1 and enemychance <= 3:
            print('Nate missed!')
            warrior_attack = random.randint(0, 1)
        else:
            print('Nate missed!')


def fight_goblin(enemy: Enemy, player: Player, inventory, currentRoom, pot,
                 name):
    print('The Goblin initiates the battle!')
    status(currentRoom, inventory)
    if "Fist" in inventory:
        player.attack1 = random.randint(3, 6)
    elif 'rusty_sword' in inventory:
        player.attack1 = random.randint(5, 8)
    elif 'iron_sword' in inventory:
        player.attack1 = random.randint(7, 9)
    elif 'brass_sword' in inventory:
        player.attack1 = random.randint(9, 11)
    elif 'steel_sword' in inventory:
        player.attack1 = random.randint(10, 13)
    elif 'hero_sword' in inventory:
        player.attack1 = random.randint(12, 15)

    enemy = Enemy(random.randint(10, 16), random.randint(5, 6),
                  random.randint(6, 8), False)
    hitchance = random.randint(1, 10)

    while player.health > 0 and enemy.health > 0:
        print("[strike], [kick], [heal]")
        action = input('> ').lower()
        if action == 'strike' and (hitchance > 3 and hitchance <= 10):
            enemy.health -= player.attack1
            combat(enemy, player, currentRoom, location)
            print(f"You used Strike!")
            print(f"{name} Health: {player.health}")
            print(f"Goblin Health: {enemy.health}")
            hitchance = random.randint(1, 10)

        elif action == 'strike' and hitchance <= 3:
            combat(enemy, player, currentRoom, location)
            print("You missed!")
            print(f"{name} Health: {player.health}")
            print(f"Goblin Health: {enemy.health}")
            hitchance = random.randint(1, 10)
        elif action == 'kick' and (hitchance > 3 and hitchance <= 10):
            combat(enemy, player, currentRoom, location)
            print("You used kick!")
            enemy.health -= player.attack2
            print(f"{name} Health: {player.health}")
            print(f"Goblin Health: {enemy.health}")
            hitchance = random.randint(1, 10)
        elif action == 'kick' and (hitchance <= 3):
            combat(enemy, player, currentRoom, location)
            print('You missed!')
            print(F"{name} Health: {player.health}")
            print(f"Goblin Health: {enemy.health}")
            hitchance = random.randint(1, 10)
        elif action == "heal" and player.health <= 30:
            if pot > 0:
                if player.health <= 20:
                    player.health += 10
                    print("You used a health potion!")
                    print(f"{name} Health: {player.health}")
                    pot -= 1
                    print(f"Goblin Health: {enemy.health}")
                elif player.health > 20:
                    spark = 30 - player.health
                    player.health += spark
                    pot -= 1
                    print("You used a health potion!")
                    print(f"{name} Health: {player.health}")
                    print(f"Goblin Health: {enemy.health}")
                elif player.health == 30:
                    print(
                        "You cannot use the health potion. You are at full health."
                    )
            else:
                print("you have no health potions")
        if enemy.health <= 0:
            print('The goblin is defeated. To move on, move to the right.')
            break

        elif player.health <= 0 and player.is_dead == False:
            player.is_dead = True
            break


def fight_archer(enemy: Enemy, player: Player, inventory, currentRoom, pot,
                 name):
    print('The archer initiates the battle!')
    status(currentRoom, inventory)
    if 'rusty_sword' in inventory:
        player.attack1 = random.randint(5, 8)
    elif 'iron_sword' in inventory:
        player.attack1 = random.randint(7, 9)
    elif 'brass_sword' in inventory:
        player.attack1 = random.randint(9, 11)
    elif 'steel_sword' in inventory:
        player.attack1 = random.randint(10, 13)
    elif 'hero_sword' in inventory:
        player.attack1 = random.randint(12, 15)
    enemy = Enemy(15, random.randint(7, 8), random.randint(6, 8), False)
    hitchance = random.randint(1, 10)
    while player.health > 0 and enemy.health > 0:
        print("[strike], [kick], [heal]")
        action = input('> ').lower()
        if action == 'strike' and (hitchance > 3 and hitchance <= 10):
            enemy.health -= player.attack1
            combat(enemy, player, currentRoom, location)
            print(f"You used Strike!")
            print(f"{name} Health: {player.health}")
            print(f"Archer Health: {enemy.health}")
            hitchance = random.randint(1, 10)

        elif action == 'strike' and hitchance <= 3:
            combat(enemy, player, currentRoom, location)
            print("You missed!")
            print(f"{name} Health: {player.health}")
            print(f"Archer Health: {enemy.health}")
            hitchance = random.randint(1, 10)
        elif action == 'kick' and (hitchance > 3 and hitchance <= 10):
            combat(enemy, player, currentRoom, location)
            print("You used kick!")
            enemy.health -= player.attack2
            print(f"{name} Health: {player.health}")
            print(f"Archer Health: {enemy.health}")
            hitchance = random.randint(1, 10)
        elif action == 'kick' and (hitchance <= 3):
            combat(enemy, player, currentRoom, location)
            print('You missed!')
            print(F"{name} Health: {player.health}")
            print(f"Archer Health: {enemy.health}")
            hitchance = random.randint(1, 10)
        elif action == "heal" and player.health <= 30:
            if pot > 0:
                if player.health <= 20:
                    player.health += 10
                    print("You used a health potion!")
                    print(f"{name} Health: {player.health}")
                    pot -= 1
                    print(f"Archer Health: {enemy.health}")
                elif player.health > 20:
                    spark = 30 - player.health
                    player.health += spark
                    pot -= 1
                    print("You used a health potion!")
                    print(f"{name} Health: {player.health}")
                    print(f"Archer Health: {enemy.health}")
                elif player.health == 30:
                    print(
                        "You cannot use the health potion. You are at full health."
                    )
            else:
                print("you have no health potions")

        if enemy.health <= 0:
            print('The archer is defeated. To move on, move to the right.')
            break
        elif player.health <= 0:
            player.is_dead = True
            break


def fight_warrior(enemy: Enemy, player: Player, inventory, currentRoom, pot,
                  name):
    print('The Warrior initiates the battle!')
    status(currentRoom, inventory)
    if 'rusty_sword' in inventory:
        player.attack1 = random.randint(5, 8)
    elif 'iron_sword' in inventory:
        player.attack1 = random.randint(7, 9)
    elif 'brass_sword' in inventory:
        player.attack1 = random.randint(9, 11)
    elif 'steel_sword' in inventory:
        player.attack1 = random.randint(10, 13)
    elif 'hero_sword' in inventory:
        player.attack1 = random.randint(12, 15)
    enemy = Enemy(20, random.randint(7, 8), random.randint(8, 9), False)
    hitchance = random.randint(1, 10)
    while player.health > 0 and enemy.health > 0:
        print("[strike], [kick], [heal]")
        action = input('> ').lower()
        if action == 'strike' and (hitchance > 3 and hitchance <= 10):
            enemy.health -= player.attack1
            combat(enemy, player, currentRoom, location)
            print(f"You used Strike!")
            print(f"{name} Health: {player.health}")
            print(f"Warrior Health: {enemy.health}")
            hitchance = random.randint(1, 10)

        elif action == 'strike' and hitchance <= 3:
            combat(enemy, player, currentRoom, location)
            print("You missed!")
            print(f"{name} Health: {player.health}")
            print(f"Warrior Health: {enemy.health}")
            hitchance = random.randint(1, 10)
        elif action == 'kick' and (hitchance > 3 and hitchance <= 10):
            combat(enemy, player, currentRoom, location)
            print("You used kick!")
            enemy.health -= player.attack2
            print(f"{name} Health: {player.health}")
            print(f"Warrior Health: {enemy.health}")
            hitchance = random.randint(1, 10)
        elif action == 'kick' and (hitchance <= 3):
            combat(enemy, player, currentRoom, location)
            print('You missed!')
            print(F"{name} Health: {player.health}")
            print(f"Warrior Health: {enemy.health}")
            hitchance = random.randint(1, 10)
        elif action == "heal" and player.health <= 30:
            if pot > 0:
                if player.health <= 20:
                    player.health += 10
                    print("You used a health potion!")
                    print(f"{name} Health: {player.health}")
                    pot -= 1
                    print(f"Warrior Health: {enemy.health}")
                elif player.health > 20:
                    spark = 30 - player.health
                    player.health += spark
                    pot -= 1
                    print("You used a health potion!")
                    print(f"{name} Health: {player.health}")
                    print(f"Warrior Health: {enemy.health}")
                elif player.health == 30:
                    print(
                        "You cannot use the health potion. You are at full health."
                    )
            else:
                print("you have no health potions")

        if enemy.health <= 0:
            print('The warrior is defeated. To move on, move to the right.')
            break
        elif player.health <= 0:
            player.is_dead = True
            break


def fight_knight(enemy: Enemy, player: Player, inventory, currentRoom, pot,
                 name):
    print('The Knight initiates the battle!')
    status(currentRoom, inventory)
    if 'rusty_sword' in inventory:
        player.attack1 = random.randint(5, 8)
    elif 'iron_sword' in inventory:
        player.attack1 = random.randint(7, 9)
    elif 'brass_sword' in inventory:
        player.attack1 = random.randint(9, 11)
    elif 'steel_sword' in inventory:
        player.attack1 = random.randint(10, 13)
    elif 'hero_sword' in inventory:
        player.attack1 = random.randint(12, 15)
    enemy = Enemy(30, random.randint(9, 10), random.randint(8, 9), False)
    hitchance = random.randint(1, 10)
    while player.health > 0 and enemy.health > 0:
        print("[strike], [kick], [heal]")
        action = input('> ').lower()
        if action == 'strike' and (hitchance > 3 and hitchance <= 10):
            enemy.health -= player.attack1
            combat(enemy, player, currentRoom, location)
            print(f"You used Strike!")
            print(f"{name} Health: {player.health}")
            print(f"Knight Health: {enemy.health}")
            hitchance = random.randint(1, 10)

        elif action == 'strike' and hitchance <= 3:
            combat(enemy, player, currentRoom, location)
            print("You missed!")
            print(f"{name} Health: {player.health}")
            print(f"Knight Health: {enemy.health}")
            hitchance = random.randint(1, 10)
        elif action == 'kick' and (hitchance > 3 and hitchance <= 10):
            combat(enemy, player, currentRoom, location)
            print("You used kick!")
            enemy.health -= player.attack2
            print(f"{name} Health: {player.health}")
            print(f"Knight Health: {enemy.health}")
            hitchance = random.randint(1, 10)
        elif action == 'kick' and (hitchance <= 3):
            combat(enemy, player, currentRoom, location)
            print('You missed!')
            print(F"{name} Health: {player.health}")
            print(f"Knight Health: {enemy.health}")
            hitchance = random.randint(1, 10)
        elif action == "heal" and player.health <= 30:
            if pot >= 1:
                if player.health <= 20:
                    player.health += 10
                    print("You used a health potion!")
                    print(f"{name} Health: {player.health}")
                    pot -= 1
                    print(f"Knight Health: {enemy.health}")
                elif player.health > 20:
                    spark = 30 - player.health
                    player.health += spark
                    pot -= 1
                    print("You used a health potion!")
                    print(f"{name} Health: {player.health}")
                    print(f"Knight Health: {enemy.health}")
                elif player.health == 30:
                    print(
                        "You cannot use the health potion. You are at full health."
                    )
            else:
                print("you have no health potions")

        if enemy.health <= 0:
            print('The knight is defeated. To move on, move to the right.')
            break
        elif player.health <= 0:
            player.is_dead = True
            break


def fight_warden(enemy: Enemy, player: Player, inventory, currentRoom, pot,
                 name):
    print('Nate initiates the battle!')
    status(currentRoom, inventory)
    if 'rusty_sword' in inventory:
        player.attack1 = random.randint(5, 8)
    elif 'iron_sword' in inventory:
        player.attack1 = random.randint(7, 9)
    elif 'brass_sword' in inventory:
        player.attack1 = random.randint(9, 11)
    elif 'steel_sword' in inventory:
        player.attack1 = random.randint(10, 13)
    elif 'hero_sword' in inventory:
        player.attack1 = random.randint(12, 15)
    enemy = Enemy(40, random.randint(10, 12), random.randint(10, 12), False)
    hitchance = random.randint(1, 10)
    while player.health > 0 and enemy.health > 0:
        print("[strike], [kick], [heal]")
        action = input('> ').lower()
        if action == 'strike' and (hitchance > 3 and hitchance <= 10):
            enemy.health -= player.attack1
            combat(enemy, player, currentRoom, location)
            print(f"You used Strike!")
            print(f"{name} Health: {player.health}")
            print(f"Nate Health: {enemy.health}")
            hitchance = random.randint(1, 10)

        elif action == 'strike' and hitchance <= 3:
            combat(enemy, player, currentRoom, location)
            print("You missed!")
            print(f"{name} Health: {player.health}")
            print(f"Nate Health: {enemy.health}")
            hitchance = random.randint(1, 10)
        elif action == 'kick' and (hitchance > 3 and hitchance <= 10):
            combat(enemy, player, currentRoom, location)
            print("You used kick!")
            enemy.health -= player.attack2
            print(f"{name} Health: {player.health}")
            print(f"Nate Health: {enemy.health}")
            hitchance = random.randint(1, 10)
        elif action == 'kick' and (hitchance <= 3):
            combat(enemy, player, currentRoom, location)
            print('You missed!')
            print(F"{name} Health: {player.health}")
            print(f"Nate Health: {enemy.health}")
            hitchance = random.randint(1, 10)
        elif action == "heal" and player.health <= 30:
            if pot >= 1:
                if player.health <= 20:
                    player.health += 10
                    print("You used a health potion!")
                    print(f"Player Health: {player.health}")
                    pot -= 1
                    print(f"Nate Health: {enemy.health}")
                elif player.health > 20:
                    spark = 30 - player.health
                    player.health += spark
                    pot -= 1
                    print("You used a health potion!")
                    print(f"{name} Health: {player.health}")
                    print(f"Nate Health: {enemy.health}")
                elif player.health == 30:
                    print(
                        "You cannot use the health potion. You are at full health."
                    )
            else:
                print("you have no health potions")

        if enemy.health <= 0:
            print('Nate is defeated. To move on, move to the right.')
            break
        elif player.health <= 0:
            player.is_dead = True
            break


location = {
    "prep_room": {
        "right": "Arena",
        "item": "rusty_sword",
        "potion": "health_potion"
    },
    "Arena": {
        "left": "prep_room",
        "right": "First Chamber",
        "Gobbo": "goblin"
    },
    "First Chamber": {
        "left": "Arena",
        "right": "range",
        "item": "iron_sword",
        "potion": "health_potion"
    },
    "range": {
        "left": "First Chamber",
        "right": "Second Chamber",
        "David": "archer"
    },
    "Second Chamber": {
        "left": "Range",
        "right": "Second Arena",
        "item": "brass_sword",
        "potion": "health_potion"
    },
    "Second Arena": {
        "left": "Second Chamber",
        "right": "Third Chamber",
        "Steve": "warrior"
    },
    "Third Chamber": {
        "left": "Second Arena",
        "right": "Knights Chamber",
        "item": "steel_sword",
        "potion": "health_potion"
    },
    "Knights Chamber": {
        "left": "Third Chamber",
        "right": "Fourth Chamber",
        "Harold": "knight"
    },
    "Fourth Chamber": {
        "left": "Knights Chamber",
        "right": "Wardens Chamber",
        "item": "hero_sword",
        "potion": "health_potion"
    },
    "Wardens Chamber": {
        "left": "Fourth Chamber",
        "right": "Treasure Room",
        "Arthur": "warden"
    },
    "Treasure Room": {
        "left": "Wardens Chamber",
        "gold": "treasure"
    }
}


def status(currentRoom, inventory):
    if currentRoom == "prep_room" and "item" in location[currentRoom]:
        print("""
    
          |------|
          | /'  []}
          |------|
    
    """)
    if currentRoom == "prep_room" and "item" not in location[currentRoom]:
        print("""
    
          |------|
          |     []}
          |------|
    
    """)
    if currentRoom == "Arena" and "Gobbo" in location[currentRoom]:
        print("""

          |----------|
          |          |
          |     o    |
          {[]   |\  []}
          |          |
          |----------|
    
    """)
    if currentRoom == "Arena" and "Gobbo" not in location[currentRoom]:
        print("""

          |----------|
          |          |
          |          |
          {[]       []}
          |          |
          |----------|
    
    """)

    if currentRoom == "First Chamber" and "item" in location[currentRoom]:
        print("""
    
          |------|
          | /'  []}
          |------|
    
    """)
    if currentRoom == "First Chamber" and "item" not in location[currentRoom]:
        print("""
    
          |------|
          |     []}
          |------|
    
    """)

    if currentRoom == "range" and "David" in location[currentRoom]:
        print("""

          |----------------------|
          |                  o   |
          {[]              (-|  []}
          |                 /\   |
          |----------------------|
    
    """)
    if currentRoom == "range" and "David" not in location[currentRoom]:
        print("""

          |----------------------|
          |                      |
          {[]                   []}
          |                      |
          |----------------------|
    
    """)

    if currentRoom == "Second Chamber" and "item" in location[currentRoom]:
        print("""
    
          |------|
          | /'  []}
          |------|
    
    """)
    if currentRoom == "Second Chamber" and "item" not in location[currentRoom]:
        print("""
    
          |------|
          |     []}
          |------|
    
    """)

    if currentRoom == "Second Arena" and "Steve" in location[currentRoom]:
        print("""
           _________________
          |                 |
          |                 |
          |         o   o   |
          {[]     ()[]-/    []}
          |         /\      |
          \_________________/
    
               """)

    if currentRoom == "Second Arena" and "Steve" not in location[currentRoom]:
        print("""
           _________________
          |                 |
          |                 |
          {[]              []}
          |                 |
          \_________________/
    
    """)

    if currentRoom == "Third Chamber" and "item" in location[currentRoom]:
        print("""
    
          |------|
          | /'  []}
          |------|
    
    """)
    if currentRoom == "Third Chamber" and "item" not in location[currentRoom]:
        print("""
    
          |------|
          |     []}
          |------|
    
    """)

    if currentRoom == "Knights Chamber" and "Harold" in location[currentRoom]:
        print("""
           ______________
          |              |
          |    \  0      |
          {[]   \/{}\   []}
          |       /\     |
          \______________/
    
    """)
    if currentRoom == "Knights Chamber" and "Harold" not in location[
            currentRoom]:
        print("""
           ______________
          |              |
          |              |
          {[]           []}
          |              |
          \______________/
    
    """)

    if currentRoom == "Fourth Chamber" and "item" in location[currentRoom]:
        print("""
  
        |------|
        | /'  []}
        |------|
  
  """)
    if currentRoom == "Fourth Chamber" and "item" not in location[currentRoom]:
        print("""
      
            |------|
            |     []}
            |------|
      
      """)

    if currentRoom == "Wardens Chamber" and "Arthur" in location[currentRoom]:
        print("""
          _____________
        |     / \     |
        |     | |     |
        |     | | 0   |
        |      |=(]   |
        |        /\   |
        \_____________/
    """)
    if currentRoom == "Wardens Chamber" and "Arthur" not in location[
            currentRoom]:
        print("""
          _____________
        |             |
        |             |
        |             |
        |             |
        |             |
        \_____________/
    """)
    if currentRoom == "Treasure Room":
        print("""
          _____________
        |             |
        |            o|
        |         oooo|
        |     oooooooo|
        |   oooooooooo|
        \_____________/
    """)

    print('You are in the ' + currentRoom)

    print('---------------------------')
    print('Inventory : ' + str(inventory))

    if "item" in location[currentRoom]:
        print('You see a ' + location[currentRoom]['item'])
    if "potion" in location[currentRoom]:
        print('You see a ' + location[currentRoom]['potion'])
    if "enemy" in location[currentRoom]:
        print('You see the ' + location[currentRoom]['enemy'] +
              " ahead of you!")

    print("---------------------------")
