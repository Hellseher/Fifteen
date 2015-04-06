#! /usr/bin/env python
# _*_ coding: UTF-8 _*_
# File          :  game_fifteen.py
# Created       :  Mon 06 Apr 2015 23:32:28
# Last Modified :  Mon 06 Apr 2015 23:58:27
# Maintainer    :  sharlatan, <sharlatanus@gmail.com>
# License       :  Same as Python (GPL)
# Credits:
#
"""
..:: Description ::..


"""


from random import randint
from os import system
from time import sleep
import sys


global MIN, MAX, board
MIN = 3
MAX = 9


def great_player():

    system('clear')
    l = "   Welcome to GAME 15!"
    print "=" * len(l) + "=="
    print l
    print "=" * len(l) + "=="


def init(alen):
    """ initilize the board, no drawing """

    step = 0
    A = []
    # set of random numbers
    while step < alen * alen:
        s = randint(0, alen * alen - 1)
        if s not in A:
            A.append(s)
            step += 1
    # initilize 2d array and fill it with numbers from A[]
    B = [[0 for i in range(alen)] for j in range(alen)]
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
            if j == i[0]:  # the begining of the line
                if j == 0:
                    print "|    |",
                else:
                    print "| %2s |" % j,
            elif j == i[-1]:  # the end of line
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
    """move the tile if posible takes tile value and board dimention"""

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


def error(*argv):
    if len(argv) == 0:
        print ("Wrong initialize of the Game.")
        print ("Usage: ./game_fifteen.py [dimention]")
        quit()
    elif argv[0] < MIN or argv[0] > MAX:
        print ("Board must be between %i x %i and %i x %i,\
        inclusive.\n") % (MIN, MIN, MAX, MAX)
        quit()


def main():
    """ main function to set up the Game 15"""

    if len(sys.argv) != 2:
        error()
    d = int(sys.argv[1])
    error(d)

    great_player()

    board = init(d)    # initialize the board
    while True:
        system('clear')
        drawboard(board)  # draw the current state of the board

        if won(board):
            print "Congrat!"
            break
        tile = int(raw_input('Tile to move: '))  # promt for move
        if movetile(tile, board) is not True:
            print "Illegal move... try again"
            sleep(3)


if __name__ == '__main__':
    main()
