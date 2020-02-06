import sys, random
def main():
    mainMenu()
print('Greetings, Dungeon Master, this is my D&D script made for aiding in combat and rolls in general.')
print('Use me wisely and report any bugs to Pedro')
print('So, let\'s get started. shall we?')
def mainMenu():
    print('What would you like me to do?')
    print('For combat type 1, for saving throws type 2, to shut me down type 3')
    gMasterMenu = input()
    if gMasterMenu == '3':
        print('See you later, Dungeon Master!')
        sys.exit() # This ends the program
    if gMasterMenu == '1':
        print('Sharp your blade and get your scrolls, combat to death shall it be!')
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
                main() # This takes the user back to the main options
    if gMasterMenu == '2':
        print('Uh uh, hope you\'re not doing a con save with 1 HP already.')
        while True:
            savingRoll = random.randint(1, 20)
            print('What is the saving roll DC?')
            savingRollDC = int(input())
            print('What is the saving roll bonus?')
            savingRollBonus = int(input())
            if savingRoll + savingRollBonus > savingRollDC:
                print('The character succeeded the saving roll!')
            elif savingRoll + savingRollBonus < savingRollDC:
                print('The character failed the saving roll!')
            print('Type 1 to roll again or 2 to go back to the main menu')
            if input() == '2':
                main() # This takes the user back to the main options
        mainMenu()
main()
