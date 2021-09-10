from dataclasses import dataclass
from functions import *
# from replit import audio
import random

is_dead = False
action = ""
pot = 0
name = input("What is your name? ")
currentRoom = "prep_room"
inventory.insert(0, "Fist")
inventory.insert(1, (pot, "potions"))
while True:
    if action == 'heal':
        pot -= 1
    if "treasure" in inventory:
        print("YOU WIN")
        break
    if name == "quit":
        print("c'mon gimme a chance")
        break
    if name == "David":
        print("David sucks")
        print("Give us a better name next time")
        break
    if name == "Nate":
        print("no, you probably think a keyboard is a weapon,")
        print("and your best freind is coffee!.. ya weirdo...")
        print("Give us a better name next time")
        break
    if player.health <= 0:
        print("""
              YOU DIED
              _________
             |         |
             | ()   () |         
              |       |
              \_|||||_/
        
              YOU DIED
  
""")
        break
    if "Gobbo" in location[currentRoom]:
        fight_goblin(enemy, player, inventory, currentRoom, pot, name)
        del location[currentRoom]['Gobbo']
    if "David" in location[currentRoom]:
        fight_archer(enemy, player, inventory, currentRoom, pot, name)
        del location[currentRoom]['David']
    if "Steve" in location[currentRoom]:
        fight_warrior(enemy, player, inventory, currentRoom, pot, name)
        del location[currentRoom]['Steve']
    if "Harold" in location[currentRoom]:
        fight_knight(enemy, player, inventory, currentRoom, pot, name)
        del location[currentRoom]['Harold']
    if "Arthur" in location[currentRoom]:
        fight_warden(enemy, player, inventory, currentRoom, pot, name)
        del location[currentRoom]['Arthur']

    if player.health <= 0:
        print("""
              YOU DIED
              _________
             |         |
             | ()   () |
             \         /
              |       |
              \_|||||_/
        
              YOU DIED
  
        """)
        break
    status(currentRoom, inventory)
    move = ''
    while move == '':
        move = input('> ')

    move = move.lower().split()
    if move[0] == 'go':
        if move[1] in location[currentRoom]:
            currentRoom = location[currentRoom][move[1]]
        else:
            print('You can\'t go that way!')

    if move[0] == 'grab':
        if "item" in location[currentRoom] and move[1] in location[
                currentRoom]['item']:
            inventory[0] = move[1]
            del location[currentRoom]['item']

        elif "potion" in location[currentRoom] and move[1] in location[
                currentRoom]['potion']:
            pot += 1
            inventory[1] = pot, 'potion(s)'
            print(move[1] + ' gained!')
            del location[currentRoom]['potion']

        elif "gold" in location[currentRoom] and move[1] in location[
                currentRoom]['gold']:
            print(move[1] + ' gained!')
            del location[currentRoom]['gold']
        else:
            print('Can\'t get ' + move[1] + '!')

    if move[0] == "quit":
        print("winners never quit")
        break
