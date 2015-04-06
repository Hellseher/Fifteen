#!/user/bin/python

# fifteen.py
#Game of fifteen

from random import randint
from os import system
from time import sleep
import sys


global MIN, MAX, board
MIN = 3
MAX = 9


def great_player():
    """ great the user """

    system('clear')
    """   great the player"""
    l = "   Welcome to GAME 15!"
    print "=" * len(l) + "=="
    print l
    print "=" * len(l) + "=="


def init(alen):
    """initilize the board, no drawing it fill the board with random numbers"""

    step = 0
    A = []
    # set of random numbers
    while step < alen * alen:
        s = randint(0, alen * alen - 1)
        if s not in A:
            A.append(s)
            step += 1


    # initilize 2d array and fill it with numbers from A[]
    B = [[0 for i in range(alen)] for j in range(alen)];
    h = 0

    for i in range(alen):
        for j in range(alen):
            B[i][j] = A[h]
            h += 1

    return B



def drawboard(board):
    """draw the board"""

    for i in board:
        print "======" * len(board)
        for j in i:
            if j == i[0]: # the begining of the line
                if j == 0:
                    print "|    |",
                else:
                    print "| %2s |" % j,
            elif j == i[-1]: # the end of line
                if j == 0:
                    print "    |"
                else:
                    print " %2s |" % j
            else:
                if j == 0:
                    print "    |",
                else:
                    print " %2s |" % j,
    print "======" * len(board)


def movetile(tile, board):
    """move the tile if posible
        takes tile value and board dimention"""

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == tile:
                tile_i = i
                tile_j = j
            if board[i][j] == 0:
                nul_i = i
                nul_j = j

    if tile_i - 1 == nul_i and tile_j == nul_j:
        board[tile_i][tile_j] = 0
        board[nul_i][nul_j] = tile
        return True

    elif tile_i + 1 == nul_i and tile_j == nul_j:
        board[tile_i][tile_j] = 0
        board[nul_i][nul_j] = tile
        return True

    elif tile_i == nul_i and tile_j - 1 == nul_j:
        board[tile_i][tile_j] = 0
        board[nul_i][nul_j] = tile
        return True

    elif tile_i == nul_i and tile_j + 1 == nul_j:
        board[tile_i][tile_j] = 0
        board[nul_i][nul_j] = tile
        return True
    else:
        return False


def won(board):
    """check weather the board in wining position"""

    n = 1
    p = len(board)*len(board) - 1

    for i in range(len(board)):
        for j in range(len(board)):
            if n == board[i][j]:
                n += 1

    if p == n:
        return True
    else:
        return False


def error():
    print ("Wrong initialize of the Game.")
    print ("Usage: ./game_fifteen.py [dimention]")
    quit()


def main():
    """ main function to set up the Game 15"""

    great_player()

    if len(argv) < 2: # ensure proper usage
        print "Usage: ./fifteen [dimention]\n"
        return

    d = int(argv[1])
    if d < MIN or d > MAX:
        print ("Board must be between %i x %i and %i x %i,\
        inclusive.\n") % (MIN, MIN, MAX, MAX)
        return

    board = init(d)    # initialize the board

    while True:
        system('clear')

        drawboard(board) # draw the current state of the board

        if won(board) == True:
            print "Congrat!"
            break

        tile = int(raw_input('Tile to move: ')) #promt for move

        if movetile(tile, board) != True:
            print "Illegal move... try again"
            sleep(3)



    #b = int(argv[1]) # board dim
    #
    #print movetile(1,board)

if __name__ == '__main__':
    main()

