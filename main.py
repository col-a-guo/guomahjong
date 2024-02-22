import random

suits = ["bing", "tiao", "wan"]
numbers = [1,2,3,4,5,6,7,8,9]
dragons = ["zhong", "fa", "bai"]
winds = ["n", "s", "e", "w"]

#HANDS:

#PRIMARY:


#Hun Yao - 1/9/word in each set

#Si Gui Er - 


tiles = []

for i in range(4):
    for suit in suits:
        for number in numbers:
            tiles.append((suit, number))
    for dragon in dragons:
        tiles.append(dragon, -1)
    for wind in winds:
        tiles.append(wind, -1)

turn = 1



#decides how to discard; returns discard and new target if any
def discard(hand, pile, passed, target):

#decides if to eat; returns discard and new target if any
def chi(hand, pile, passed, target):

#decides if to pong; returns discard and new target if any
def pong(hand, pile, passed, target):

#decides what to do
def decision(hand, pile, passed, turn, player, target):
    if player == turn:
        return discard(hand, pile, passed, target)
    if player == (turn+1)%4:
        return chi(hand, pile, passed, target)
    else:
        return pong(hand, pile, passed, target)
    
hands = [[],[],[],[]]

for player_to_draw in range(4):
    for start_tile in range(13):
        tiledraw = random.randint(0, len(tiles)-1)
        hands[player_to_draw].append(tiles.pop(tiledraw))

turn = 0

while tiles != []:
    
