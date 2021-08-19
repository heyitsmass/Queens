import os 
import time 
import keyboard
from typing import overload 
from chessboard import display
from dataclasses import dataclass 

@dataclass 
class Point: 
    x : int 
    y : int 
    isQueen : bool 
    isSafe  : bool 


board_dimensions = 8
board = []
queens = []

def sortY(e): 
    return e.y

def init_board(init_point): 
    for x in range(board_dimensions): 
        for y in range(board_dimensions): 
            if x is init_point.x and y is init_point.y: 
                board.append(init_point) 
            else: 
                board.append(Point(x, y, False, True))
    board.sort(key=sortY)

def display_board(): 

    print('\n', end = '')
    
    for i in range(len(board)):

        if board[i].isQueen: 
            print('Q', end = ' ')
        elif not board[i].isSafe: 
            print('X', end = ' ')
        else: 
            print('.', end = ' ')
        
        if i < len(board)-1:
            if board[i+1].y > board[i].y:
                print()

    print('\n')
    

def main(): 

    init_point = Point(4, 5, True, False)

    init_board(init_point)  

    queens.append(init_point) 

    display_board()

    exit()

main()

