import random
print('So you are ready to jump at each other\'s throath? Fine, let\'s get to rolling dices!')
while True: # This is the main loop of the attacking action
    print('What is the target Armor Class?')
    aC= int(input())
    print('What is the to hit bonus from the attacker?')
    attackRoll = random.randint(1, 20)
    toHitValue = int(input())
    if attackRoll + toHitValue > aC: # This compares the roll and bonus value to the AC of the target
        print('Target hit!')
    elif attackRoll + toHitValue < aC:
        print('The attack missed the mark!')
    print('Type 1 to attack again, type 2 to go back to the main menu') # This gives the user the option to attack again or go
    if input() == '2':
        break
