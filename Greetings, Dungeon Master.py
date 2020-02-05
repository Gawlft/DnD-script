print('Greetings, Dungeon Master, this is my D&D script made for aiding in combat and rolls in general.')
print('Use me wisely and report any bugs to Pedro')
print('So, let\'s get started. shall we?')
while True:  # This is the main menu of the program
    print('What would you like me to do?')
    print('For combat type 1, for saving throws type 2, to shut me down type 3')
    gMasterMenu = input()
    if gMasterMenu == '3':
        sys.exit() # This ends the program
    if gMasterMenu == '1':
        print('Sharp your blade and get your scrolls, combat to death shall it be!')
    if gMasterMenu == '2':
        print('Uh uh, hope you\'re not doing a con save with 1 HP already.')
    if gMasterMenu == '1' or gMasterMenu == '2':
        break
