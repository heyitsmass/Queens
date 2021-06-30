from dataclasses import dataclass 
import os 

# Point type declaration
@dataclass 
class Point: 
    x: int 
    y: int 

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
        print("{0} ".format(i), end = '')

    print() 

    for y in range(board_dimensions): 
        print("\t{0}".format(y), end=' ') 
        for x in range(board_dimensions):
            temp_point = Point(x, y) 
            if temp_point in queen_locations: 
                print('Q', end=' ')
                continue
            if temp_point in unsafe_locations: 
                print('X', end=' ') 
            else: 
                print('-', end=' ')
        print()

# Sets unsafe locations for the given queen
def set_unsafe_locations(input_queen): 

    for x in range(board_dimensions):  
        temp_point = Point(x, input_queen.y)
        unsafe_locations.append(temp_point) 
    
    for y in range(board_dimensions): 
        temp_point = Point(input_queen.x, y) 
        unsafe_locations.append(temp_point) 

    diagonal_y = input_queen.y - input_queen.x

    for x in range(board_dimensions): 
        temp_point = Point(x, diagonal_y)
        if temp_point not in queen_locations and temp_point.x in range(0, board_dimensions) and temp_point.y in range(0, board_dimensions):
            unsafe_locations.append(temp_point)
        diagonal_y += 1 
    
    diagonal_x = input_queen.x + input_queen.y 
    for y in range(board_dimensions): 
        temp_point = Point(diagonal_x, y)
        if temp_point not in queen_locations and temp_point.x in range(0, board_dimensions) and temp_point.y in range(0, board_dimensions):
            unsafe_locations.append(temp_point)
        diagonal_x -= 1

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
    print("Appending Queen: ({0}, {1})".format(input_queen.x, input_queen.y))
    queen_locations.append(input_queen) 
    unsafe_locations.append(input_queen) 
    set_unsafe_locations(input_queen)
    set_safe_locations()
    print("Safe Locations : {0}".format(safe_locations)) 

# Resets all arrays to initial settings 
def reset_arrays(): 
    init_queen = queen_locations[0] 
    queen_locations.clear() 
    unsafe_locations.clear() 
    safe_locations.clear() 
    place_queen(init_queen) 

# Checks if the number of queen on the board is the correct amount 
# Previous functions bind the queens by safe locations on the board.
# Thus, the validity of the board can be confirmed by checking the number of queens.
def is_valid(): 
    if len(queen_locations) == 7: 
        return True 
    elif len(queen_locations) > 7 or len(queen_locations) < 0: 
        print("Number of queens exceeds the maximum  or minimum number allowed")
        raise 
    else: 
        return False
    

# Main 
try: 

    display_board() 

    print("Enter x coordinate:", end = ' ') 
    input_x = int(input())
    print("Enter y coordinate:", end = ' ')
    input_y = int(input()) 
    initial_queen = Point(input_x, input_y)

    place_queen(initial_queen) 

    display_board() 

    # double for loop iteration

    place_queen(safe_locations[1])

    display_board() 

    place_queen(safe_locations[0])

    display_board() 

    place_queen(safe_locations[0])
    
    display_board() 

    place_queen(safe_locations[0]) 

    display_board() 

except Exception as e: 
    print("Error: {0}".format(e))

exit()