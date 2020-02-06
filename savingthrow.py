import random
# This is for saving rolls
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
        break
