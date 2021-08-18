# Reproduction of the Eight Queens Algorithm in index.py
# The intention is to maximize functionality and minimize code 
# 
# While the previous program solved a single solution for a given queen. 
# What if we solved every solution to this problem?
# 
# Ideally we can input some queen at point (0, 0),
# find valid solutions from the given queen. 
# After we can attempt the following queens as initial positions
# 
# Repeat this until all solutions are found 

import os
import sys
import time
from dataclasses import dataclass
from typing import overload

import keyboard
from chessboard import display


@dataclass
class Point: 
    x : int 
    y : int 

# Variable declaration
board_dimensions = 8 
unsafe_locations = [] 
queen_locations  = []
safe_locations   = []

# Function declarations

# Clears the console
def clear(): os.system('clear')         # thanks to csestack.org 

# Displays the current status of the chess board
def display_board():
    print("\t  Virtual Board\n\n\t", end = '')  

    print("  ", end='')
    for i in range(board_dimensions): 
        print(" {0} ".format(i), end = '')

    print() 

    for y in range(board_dimensions): 
        print("\t{0}".format(y), end='  ') 
        for x in range(board_dimensions):
            temp_point = Point(x, y) 
            if temp_point in queen_locations: 
                print('Q', end='  ')
                continue
            # if temp_point in unsafe_locations:    # Debug
                # print('X', end=' ') 
            else: 
                print('-', end='  ')
        print()

# Sets unsafe locations for the given queen
def set_unsafe_locations(input_queen): 

    for coordinate in range(board_dimensions): 
        temp_point_one = Point(coordinate, input_queen.y) 
        temp_point_two = Point(input_queen.x, coordinate) 
        unsafe_locations.extend([temp_point_one, temp_point_two])

    diagonal_y = input_queen.y - input_queen.x 
    diagonal_x = input_queen.x + input_queen.y 

    for coordinate in range(board_dimensions): 
        temp_point_one = Point(coordinate, diagonal_y)
        temp_point_two = Point(diagonal_x, coordinate)
        if temp_point_one.x and temp_point_one.y or temp_point_two.x and temp_point_two.y in range(0, board_dimensions): 
            unsafe_locations.extend([temp_point_one, temp_point_two])
        diagonal_x -= 1 
        diagonal_y += 1

# Marks locations safe in the safe_locations array based on new queen placement
def set_safe_locations(): 

    shrink_safe_locations() 

    # Append any safe_locations
    for x in range(board_dimensions): 
        for y in range(board_dimensions): 
            temp_point = Point(x, y) 
            if temp_point not in unsafe_locations: 
                safe_locations.append(temp_point) 

# Shrinks the safe_locations array based on new queen placement 
def shrink_safe_locations():
 
    for x in range(board_dimensions): 
        for y in range(board_dimensions): 
            temp_point = Point(x, y) 
            if temp_point in safe_locations and unsafe_locations: 
                safe_locations.remove(temp_point) 

# Initializes the board with the given queen coordinate 
def place_queen(input_queen): 
    queen_locations.append(input_queen) 
    unsafe_locations.append(input_queen) 
    set_unsafe_locations(input_queen)
    set_safe_locations()

# Resets all arrays to initial settings 
def reset_board(): 
    init_queen = queen_locations[0] 
    queen_locations.clear() 
    unsafe_locations.clear() 
    safe_locations.clear() 
    place_queen(init_queen) 

# Checks if the number of queen on the board is the correct amount 
# Previous functions bind the queens by safe locations on the board.
# Thus, the validity of the board can be confirmed by checking the number of queens.
def is_valid(): 
    if len(queen_locations) == 8: 
        return True 
    elif len(queen_locations) > 8 or len(queen_locations) < 0: 
        raise Exception("Number of queens exceeds the maximum  or minimum number allowed") 
    else: 
        return False

def overloadFunc(e):
    return e.x 

def overloadFunc2(e): 
    return e.y

def purge_locations(locations): 
    locations.sort(key = overloadFunc)
    locations.sort(key = overloadFunc2)

    length = len(locations)
    fresh_array = [] 

    for i in range(length):
        if locations[i].x > 7 or locations[i].x < 0 or locations[i].y > 7 or locations[i].y < 0: 
            continue
        if len(fresh_array) == 0: 
            fresh_array.append(locations[i])
        else: 
            if locations[i] not in fresh_array: 
                fresh_array.append(locations[i])

    return fresh_array


def position_formatter(queen_locations): 
    
    # Position format ex) result 1 from (4, 5) start -> '2Q5/5Q2/3Q4/Q7/7Q/4Q3/6Q1/1Q6'
    # Sort the new_locations by y level (already done) then traverse the layer, counting the number until a queen is found 
    queen_locations.sort(key=overloadFunc2)

    full_string = ""

    for locs in queen_locations: 
        left_side  = locs.x 
        right_side = (board_dimensions - left_side - 1) 
        temp_str = "" 

        if left_side > 0 : temp_str += str(left_side) 
        
        temp_str += "Q"

        if right_side > 0 : temp_str += str(right_side)

        temp_str += "/" 

        full_string += temp_str 
    
    return full_string 
            

# Main 
def main():

    positions = []

    #print(os.__file__)

    try:  

            init_queen = Point(4, 5)

            place_queen(init_queen) 

            current_place = 0

            while True:   
                if current_place > 0: 
                    for places in range(current_place): 
                        safe_locations.remove(safe_locations[0])

                while len(safe_locations) > 0: 
                    for locations in safe_locations: 
                        if not is_valid(): 
                            place_queen(locations)
                        else: 
                            break
                if is_valid(): 
                    display_board()
                    #new_locations = purge_locations(unsafe_locations)
                    #print("Unsafe Locations", new_locations)
                    #print("Queen Locations", queen_locations) 
                    new_queens = queen_locations.copy()
                    positions.append(position_formatter(new_queens)) 
                reset_board() 
                current_place += 1 
                
                if current_place > len(safe_locations): 
                    break 

        # Add functionality to scroll through the found positions   
            current_pos = 0

            while True: 
                display.start(positions[current_pos])
                try: 
                    if keyboard.is_pressed('d') and current_pos < len(positions)-1: 
                        time.sleep(0.1)
                        current_pos += 1
                        print("Solution {0} of {1}".format(current_pos+1, len(positions)))
                    if keyboard.is_pressed('a') and current_pos > 0: 
                        time.sleep(0.1)
                        current_pos -= 1 
                        print("Solution {0} of {1}".format(current_pos+1, len(positions)))
                    if keyboard.is_pressed('c'): 
                        time.sleep(0.1)
                        display.terminate() 
                        break 
                except: 
                    break 
            #with KeyPoller() as keyPoller: 
               #while True: 
                #    if current_pos < len(positions): display.start(positions[current_pos])
                 #   c = keyPoller.poll() 
                  #  if not c is None: 
                   #     if c == "c":
                    #        display.terminate() 
                     #       break 
                      #  if c == "a" and current_pos > 0:
                       #     current_pos -= 1
                        #if c == "d" and current_pos < len(positions)-1: 
                        #    current_pos += 1
                        #print(c)



    except Exception as e: 
            print("Error: {0}".format(e))

main()
 





