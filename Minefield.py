import random

# Variable declarations
global player
global game
global mine
global cycle
global spot
global boom, valid_input
global now_player
global player_num

player = []
spot = []

# Function Declarations
def playerInput() :
    global game
    global player
    global player_num

    player_num = input("How many player? (1~5) :")
    player_num = int(player_num)
    for i in range(0,player_num) :
        player.append(input("Enter player name : "))
    
    print("Hi :)")
    for i in player :
        print(i)

def initAll() :
    global mine
    global cycle
    global spot
    global boom, valid_input
    global now_player

    mine = random.randint(1, 12)
    cycle = 1
    spot = [1,2,3,4,5,6,7,8,9,10,11,12]
    boom = False
    now_player = "ohoh"

def nowPlayer(now_cycle) :
    global game
    global player
    global player_num

    turn = now_cycle % player_num
    now_player = player[turn]

    if turn >= 3 :
        print("error")
        game = False

    return now_player

def printMap(cycle, now_player) :
    global spot

    print("\n\t Cycle " , str(cycle) , " | " , now_player , "'s turn")
    print("--------------MAP of Mine Farm--------------")
    for i, item in enumerate(spot):
        print('\t', item, end=' ')
        if (i + 1) % 4 == 0:
            print()
    print("--------------------------------------------")

def detectMine(select) :
    global boom
    global spot
    global mine

    if select == mine :
        boom = True
        return False
    else :
        for i in range(0,12):
            if spot[i] is select :
                spot[i] = 0
        return True

def getChoice(now_player) :
    select = input(now_player + ", Choose a number carefully: ")
    select = int(select)
    if 1 <= select <= 12: 
        if detectMine(select) :  return 1
        else : return 2
    else :
        print("!! You have to choose in range of 1 to 12 !!")
        print("!! and also not yet chosen !!\n\n")
        return 3
    
def gameOver(now_player) :
    global game

    print("\n\nGAME OVER")
    print(now_player + " touched the mine!")
    print(now_player + " has lost the game! \n\n")
    if (input("Guys, want to play New game? (y/n)") == "y") :
        game = True
        initAll()
    else : game = False

# Main function
game = True
while game or boom :
    initAll()
    print(mine)
    playerInput()

    while 0 < cycle < 13 and not boom :
        now_player = nowPlayer(cycle)
        printMap(cycle, now_player)
        get = getChoice(now_player)
        if get == 1 : cycle += 1
        elif get == 3 : continue
        elif get == 2 : 
            gameOver(now_player)
            cycle = 0
        else : 
            print("error")
            