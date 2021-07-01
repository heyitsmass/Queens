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
            # if temp_point in unsafe_locations: 
                # print('X', end=' ') 
            else: 
                print('-', end=' ')
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
        
# Main 
try: 

    input_x = int(input("Enter x coordinate: "))
    input_y = int(input("Enter y coordinate: ")) 
    initial_queen = Point(input_x, input_y)

    place_queen(initial_queen) 

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
            break 
        reset_board()
        current_place += 1

    if not is_valid(): 
        raise Exception("No Solution")
    else: 
        print("\nFound Solution:")
        display_board()

except Exception as e: 
    print("Error: {0}".format(e))

exit()