import pickle
import time
import os

script_dir = os.path.dirname(os.path.abspath(__file__))
data_file = os.path.join(script_dir, 'data.dat')

loop = 0
saved = 0
inventory = ['']
crackpipe = 1
crackpipeuse = 0
grandhallenter = 1
hammer = 1
goldkey = 1
manalive = 1
silverkey = 1
print('=========================================================================================')
print("Welcome to Sourwood.")


def save_game():
    with open(data_file, 'wb') as f:
        pickle.dump((loop, inventory, crackpipe, crackpipeuse, grandhallenter, manalive, hammer, goldkey, silverkey), f)
        print('Game saved')

def load_game():
    try:
        with open(data_file, 'rb') as f:
            print('Save game loaded')
            loop, inventory, crackpipe, crackpipeuse, grandhallenter, manalive, hammer, goldkey, silverkey = pickle.load(f)
    except FileNotFoundError:
        print('No save file found.')

while True:
    
    #menu
    while loop == 0:
        print('=========================================================================================')
        time.sleep(1 / 2)
        print("Do you wish to play???")
        print("You can save during the game")
        print("and load whenever you want.")
        start = input()
        startl = start.lower()
        if startl == 'yes':
            time.sleep(1 / 2)
            loop = 1
        elif startl == 'save' or startl == 'save game':
            time.sleep(1 / 2)
            print('You cannot save in the menu.')
        elif startl == 'load' or startl == 'load game':
            time.sleep(1 / 2)
            load_game()
        elif startl == 'no':
            print('=========================================================================================')
            time.sleep(1 / 2)
            print('fuck you')
            print('=========================================================================================')
            time.sleep(1 / 2)
            exit()
        else:
            time.sleep(1 / 2)
            ('=========================================================================================')
            print('That is not a valid command.')

    #Street
    if loop == 1:
        print('=========================================================================================')
        print('=========================================================================================')
        print('You are standing on a dimly lit street. Infront of you is a large decorated wooden door ')
        print('connected to a large mansion. Next to the door is a metal plaque engraved with what seems ')
        print('to be text. There is also a crackpipe on the floor.')
        print('')
        time.sleep(1 / 2)
        print('You do not remember how you got here, or why you are here.')
    while loop == 1:
        action1 = input()
        action1l = action1.lower()
        if action1l == 'leave':
            time.sleep(1 / 2)
            print('=========================================================================================')
            print('You ignore the mansion in all its extravagance and walk away forever being an incurious bore.')
            print('While walking you trip on your shoelaces and crack your skull open on the pavement.')
            print('')
            time.sleep(1 / 2)
            print('You are dead.')
            print('=========================================================================================')
            time.sleep(1 / 2)
            print('Press enter to exit. Or load your save.')
            x1 = input()
            x1l = x1.lower()
            if x1l == 'load' or x1l == 'load game':
                time.sleep(1 / 2)
                load_game()
            else:
                time.sleep(1 / 2)
                exit()
        elif action1l == 'save' or action1l == 'save game':
            time.sleep(1 / 2)
            save_game()
        elif action1l == 'load' or action1l == 'load game':
            time.sleep(1 / 2)
            load_game()
        elif action1l == 'inspect plaque' or action1l == 'look at plaque':
            time.sleep(1 / 2)
            print('=========================================================================================')
            print('The plaque is made out of metal and is beautifully decorated with flowers and suns. The light')
            print('from the streetlanterns playfully dances on the uneven surface as you move closer.')
            time.sleep(1 / 2)
            print('')
            print('The plaque reads:')
            print('{''   Sourwood Mansion   ''}')
            print('{'' Home of mr. Arboreum ''}')
        elif action1l == 'enter door' or action1l == 'enter mansion' or action1l == 'open door':
            time.sleep(1 / 2)
            loop = 2
        elif action1l == 'pickup crackpipe' or action1l == 'take crackpipe':
            if crackpipe == 1:
                time.sleep(1 / 2)
                inventory.append("crackpipe")
                crackpipe = 0
                print('=========================================================================================')
                print('You took the crackpipe.')
            else:
                time.sleep(1 / 2)
                print('=========================================================================================')
                print('You already took the crackpipe.')
        elif action1l == 'use crackpipe':
            if 'crackpipe' in inventory:
                time.sleep(1 / 2)
                print('=========================================================================================')
                print('You light up the crackpipe, it makes you feel like shit but gives you alot of energy')
                inventory.remove('crackpipe')
                crackpipeuse = 1
            else:
                time.sleep(1 / 2)
                print('=========================================================================================')
                print('You do not have a crackpipe')
        else:
            time.sleep(1 / 2)
            print('=========================================================================================')
            print('That is not a valid command.')

    #Grand hall
    if loop == 2:
        if grandhallenter == 1:
            print('=========================================================================================')
            print('As you grab onto the door handles you get a faint feeling of dread flow up your spine.')
            time.sleep(1 / 2)
            print('You compose yourself and swing the doors wide open. You are greeted by a grand hall. Inside')
            print('the hall is a large staircase flairing to the right and left, on the right side is a door.')
            time.sleep(1 / 2)
            print('On the ground floor are three doors, two of which are located opposite of eachother')
            print('and the last stands stout and unshakable on the opposite side of where you entered')
            grandhallenter = 2
        else:
            print('=========================================================================================')
            print('You enter the grand hall. There are two doors on the right, one downstairs and one upstairs.')
            time.sleep(1 / 2)
            print('There is one door downstairs on the left. There is also one big door in de middle of the hall.')
            print('')
    while loop == 2:
        action2 = input()
        action2l = action2.lower()
        time.sleep(1 / 2)
        if action2l == 'enter lower right door' or action2l == 'open lower right door':
            print('=========================================================================================')
            print('The door is barred from the other side.')
        elif action2l == 'save' or action2l == 'save game':
            save_game()
        elif action2l == 'load' or action2l == 'load game':
            load_game()
        elif action2l == 'enter middle door' or action2l == 'open middle door' or action2l == 'enter big door' or action2l == 'open big door':
            if 'gold key' in inventory and 'silver key' in inventory:
                loop = 5
            elif crackpipeuse == 1:
                loop = 5
            else:
                print('=========================================================================================')
                print('The door is locked. You need two keys to open the door.')
        elif action2l == 'enter upper right door' or action2l == 'open upper right door':
            loop = 3
        elif action2l == 'enter lower left door' or action2l == 'open lower left door':
            loop = 4
        elif action2l == 'leave' or action2l == 'leave hall':
            print('The door to the street is locked.')
        elif action2l == 'use crackpipe':
            if 'crackpipe' in inventory:
                print('=========================================================================================')
                print('You light up the crackpipe, it makes you feel like shit but gives you alot of energy')
                inventory.remove('crackpipe')
                crackpipeuse = 1
            else:
                print('=========================================================================================')
                print('You do not have a crackpipe')
        else:
            print('=========================================================================================')
            print('That is not a valid command.')

    #upper right door
    if loop == 3:
        print('=========================================================================================')
        print('You walk into a very dark and bare room.')
        if manalive == 1:
            time.sleep(1)
            print('There is a man standing in the corner of the room who appears to be holding a hammer')
            print('in one hand and a golden key in the other')
    while loop == 3:
        action3 = input()
        action3l = action3.lower()
        time.sleep(1 / 2)
        if action3l == 'leave' or action3l == 'leave room':
            loop = 2
        elif action3l == 'save' or action3l == 'save game':
            save_game()
        elif action3l == 'load' or action3l == 'load game':
            load_game()
        elif action3l == 'kill man' or action3l == 'attack man':
            if manalive == 1:
                if crackpipeuse == 1:
                    print('=========================================================================================')
                    print('You fucking obliterate the man with your crackhead powers.')
                    print('He drops the key and hammer.')
                    manalive = 0
                elif crackpipeuse == 0:
                    print('=========================================================================================')
                    print('You scuffle with the man for a few seconds befor he gets a heartattack and dies.')
                    print('He drops the key and hammer.')
                    manalive = 0
            elif manalive == 0:
                print('=========================================================================================')
                print('He is already dead')
        elif action3l == 'take key' or action3l == 'take golden key' or action3l == 'pickup key' or action3l == 'pickup golden key':
            if manalive  == 1:
                print('=========================================================================================')
                print('As you try to get close to the man he jumps out at you and viciously beats you to death')
                print('with his hammer.')
                print('')
                time.sleep(1 / 2)
                print('You are dead.')
                print('=========================================================================================')
                time.sleep(1 / 2)
                print('Press enter to exit. Or load your save.')
                x3 = input()
                x3l = x3.lower()
                if x3l == 'load' or x3l == 'load game':
                    time.sleep(1 / 2)
                    load_game()
                else:
                    time.sleep(1 / 2)
                    exit()
            elif manalive == 0:
                if goldkey == 1:
                    print('=========================================================================================')
                    print('You pickup the golden key')
                    goldkey == 0
                    inventory.append("gold key")
                elif goldkey == 0:
                    print('=========================================================================================')
                    print('You already took the key')
        elif action3l == 'take hammer' or action3l == 'pickup hammer':
            if manalive == 1:
                print('=========================================================================================')
                print('You should not do this.')
            if manalive == 0:
                if hammer == 1:
                    print('=========================================================================================')
                    print('You pickup the hammer')
                    hammer == 0
                    inventory.append("hammer")
                elif hammer == 0:
                    print('=========================================================================================')
                    print('You already took the hammer')
        elif action3l == 'use crackpipe':
            if 'crackpipe' in inventory:
                print('=========================================================================================')
                print('You light up the crackpipe, it makes you feel like shit but gives you alot of energy')
                inventory.remove('crackpipe')
                crackpipeuse = 1
            else:
                print('=========================================================================================')
                print('You do not have a crackpipe')
        else:
            print('=========================================================================================')
            print('That is not a valid command.')
    #lower left door
    if loop == 4:
        print('=========================================================================================')
        print('You walk into the room.')
        if silverkey == 1:
            time.sleep(1 / 2)
            print('There is a silver key on the floor')
    while loop == 4:
        action4 = input()
        action4l = action4.lower()
        time.sleep(1 / 2)
        if action4l == 'take key' or action4l == 'take silver key' or action4l == 'pickup key' or action4l == 'pickup silver key':
            if silverkey == 1:
                    print('=========================================================================================')
                    print('You pickup the silver key')
                    silverkey == 0
                    inventory.append("silver key")
            elif silverkey == 0:
                    print('=========================================================================================')
                    print('You already took the key')
        elif action4l == 'leave' or action4l == 'leave room':
            loop = 2
        elif action4l == 'save' or action4l == 'save game':
            save_game()
        elif action4l == 'load' or action4l == 'load game':
            load_game()
        elif action4l == 'use crackpipe':
            if 'crackpipe' in inventory:
                print('=========================================================================================')
                print('You light up the crackpipe, it makes you feel like shit but gives you alot of energy')
                inventory.remove('crackpipe')
                crackpipeuse = 1
            else:
                print('=========================================================================================')
                print('You do not have a crackpipe')
        else:
            print('=========================================================================================')
            print('That is not a valid command.')
    
    #middle door
    if loop == 5:
        print('=========================================================================================')
        print('As you walk into the room you are greeted by mr. Arboreum.')
        time.sleep(1 / 2)
        print('mr. Arboreum: What the hell are you doing in my house you fool.')
    while loop == 5:
        action5 = input()
        action5l = action5.lower()
        if action5l == 'leave' or action5l == 'leave room':
            print('=========================================================================================')
            print('You try the door but it does not open. You are then shot dead by mr.Arboreum.')
            time.sleep(1 / 2)
            print('')
            print('You are dead.')
            time.sleep(1 / 2)
            print('=========================================================================================')
            print('Press enter to exit. Or load your save.')
            x5 = input()
            x5l = x5.lower()
            time.sleep(1 / 2)
            if x5l == 'load' or x5l == 'load game':
                load_game()
            else:
                exit()
        elif action5l == 'kill arboreum' or action5l == 'attack arboreum':
            if crackpipeuse == 1:
                print('=========================================================================================')
                print('You destroy the old fool with you crackhead power.')
                print('')
                time.sleep(1 / 2)
                print('You won!!!!!')
                print('=========================================================================================')
                time.sleep(1 / 2)
                print('Press enter to exit. Or load your save.')
                x5 = input()
                x5l = x5.lower()
                time.sleep(1 / 2)
                if x5l == 'load' or x5l == 'load game':
                    load_game()
                else:
                    exit()
            if crackpipeuse == 0:
                print('=========================================================================================')
                print('You rush towards mr. arboreum but are quickly shot dead.')
                print('')
                time.sleep(1 / 2)
                print('You are dead.')
                print('=========================================================================================')
                time.sleep(1 / 2)
                print('Press enter to exit. Or load your save.')
                x5 = input()
                x5l = x5.lower()
                time.sleep(1 / 2)
                if x5l == 'load' or x5l == 'load game':
                    load_game()
                else:
                    exit()
        elif action5l == 'kill arboreum with hammer' or action5l == 'attack arboreum with hammer':
            if 'hammer' in inventory:
                print('=========================================================================================')
                print('You rush mr. arboreum and beat him to death with your hammer.')
                print('')
                time.sleep(1 / 2)
                print('You won!!!!!')
                print('=========================================================================================')
                time.sleep(1 / 2)
                print('Press enter to exit. Or load your save.')
                x5 = input()
                x5l = x5.lower()
                time.sleep(1 / 2)
                if x5l == 'load' or x5l == 'load game':
                    load_game()
                else:
                    exit()
            else:
                print('=========================================================================================')
                print('You do not have a hammer.')
        elif action5l == 'save' or action5l == 'save game':
            save_game()
        elif action5l == 'load' or action5l == 'load game':
            load_game()
        elif action5l == 'use crackpipe':
            if 'crackpipe' in inventory:
                print('=========================================================================================')
                print('You light up the crackpipe, it makes you feel like shit but gives you alot of energy')
                inventory.remove('crackpipe')
                crackpipeuse = 1
            else:
                print('=========================================================================================')
                print('You do not have a crackpipe')
        else:
            print('=========================================================================================')
            print('That is not a valid command.')