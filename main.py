# Program Functionality : Effectively determine valid oreintations for eight queens on an 8x8 chess board such that none attack the other 

# Imports 
from dataclasses import dataclass 
import os 
# Variable Declarations
board_dim = 8

# A point structure, reducing the need for 2D arrays to hold (x, y) information. 
# Points should be initialized as: 
# point = Point(x, y) where x and y should be integers within the range(board_dim)

@dataclass 
class Point: 
    x: int 
    y: int 


queen_locations = []        
safe_locations = [] 
unsafe_locations = [] 


# Function Declarations 

def clear(): os.system('clear')         # thanks to csestack.org 


def display_board():
    print("\t  Virtual Board\n\n\t", end = '')  

    print("  ", end='')
    for i in range(board_dim): 
        print("{0} ".format(i), end = '')

    print() 

    for y in range(board_dim): 
        print("\t{0}".format(y), end=' ') 
        for x in range(board_dim):
            temp_point = Point(x, y) 
            if temp_point in queen_locations: 
                print('Q', end=' ')
                continue
            if temp_point in unsafe_locations: 
                print('X', end=' ') 
            else: 
                print('-', end=' ')
        print()


# Setting unsafe locations takes three components: 
# 1. Setting all the vertical positions from the queen as unsafe. 
# 2. Setting all the horizontal positions from the queen as unsafe. 
# 3. Setting all the diagonal positions from the queen in both directions as unsafe. 

def set_unsafe_locations(point):
    # Horizontal: 
    start_y = point.y

    for x in range(board_dim):
        temp_point = Point(x, start_y)
        if temp_point not in queen_locations: 
            unsafe_locations.append(temp_point) 
    
    # Vertical: 
    start_x = point.x 

    for y in range(board_dim): 
        temp_point = Point(start_x, y)
        if temp_point not in queen_locations: 
           unsafe_locations.append(temp_point) 

    # Diagonal:
    # Left to right 
    
    start_y = start_y - start_x     # Result from y = mx + b (new start_y = b)

    for x in range(board_dim): 
        temp_point = Point(x, start_y) 
        if temp_point not in queen_locations and temp_point.x < 8 and temp_point.y < 8: 
            unsafe_locations.append(temp_point) 
        start_y += 1    

    # Right to left

    start_x = (point.x) + point.y

    for y in range(board_dim): 
        temp_point = Point(start_x, y)
        if temp_point not in queen_locations: 
            unsafe_locations.append(temp_point) 
        start_x -= 1 

def check_orientations(): 

    for y in range(board_dim): 
        for x in range(board_dim): 
            temp_point = Point(x, y)
            if temp_point not in unsafe_locations and queen_locations: 
                print(temp_point) # Safe Locations 


def place_queen(point): 
    queen_locations.append(point) 
    set_unsafe_locations(point)

try: 
    # Introductory Message 
    print("\n  Finding Valid Orientations...\n")

    display_board() 

    print("\n Input initial queen coordinate x: ", end = '')
    input_x = int(input())
    print(" Input initial queen coordinate y: ", end = '')
    input_y = int(input())

    if input_x > 7 or input_x < 0: 
        raise ValueError('x coordinate "{0}" exceeds the board width.'.format(input_x)) 
    if input_y > 7 or input_y < 0: 
        raise ValueError('y coordinate "{0}" exceeds the board length.'.format(input_y))
        
    p = Point(input_x, input_y) 
    clear() 

    place_queen(p) 

    print("\n  Finding Valid Orientations...\n")

    display_board() 

    check_orientations()

except Exception as e: 
    print("An error has occured: {0}".format(e))

exit()