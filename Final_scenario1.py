import math

# Coordinates list to store the path   
path_coordinates = []

def find_end_point(x1, y1, distance, direction):
    if direction == 'N':
        x2, y2 = x1, y1 + distance
    elif direction == 'S':
        x2, y2 = x1, y1 - distance 
    elif direction == 'E':
        x2, y2 = x1 + distance, y1
    elif direction == 'W':
        x2, y2 = x1 - distance, y1
    elif direction == 'NE':
        x2, y2 = x1 + distance / math.sqrt(2), y1 + distance / math.sqrt(2)
    elif direction == 'NW':
        x2, y2 = x1 - distance / math.sqrt(2), y1 + distance / math.sqrt(2)
    elif direction == 'SE':
        x2, y2 = x1 + distance / math.sqrt(2), y1 - distance / math.sqrt(2)
    elif direction == 'SW':
        x2, y2 = x1 - distance / math.sqrt(2), y1 - distance / math.sqrt(2)
    else:
        raise ValueError("Invalid direction provided!")
    
    return x2, y2

def calculate_manhattan_distance(x1, y1, x2, y2):
    return abs(x2 - x1) + abs(y2 - y1)

def plot_manhattan_distance(x1, y1, x2, y2):
    # Calculate the Manhattan distance path
    if x1 != x2:
        path_coordinates.extend([(i, y1) for i in range(min(x1, x2), max(x1, x2) + 1)])   
    if y1 != y2:
        path_coordinates.extend([(x2, i) for i in range(min(y1, y2), max(y1, y2) + 1)])   

x1 = int(input("Provide x1: "))
y1 = int(input("Provide y1: "))
distance = int(input("Provide distance from start to goal: "))
direction = input("Provide direction: ").upper()

destination = find_end_point(x1, y1, distance, direction)
x2, y2 = destination[0], destination[1]

plot_manhattan_distance(x1, y1, x2, y2)

print("Manhattan Path Coordinates:", path_coordinates)

Ir = []  # Assuming IR sensor data will be populated here
direction_dict = {}

def eval_Free_Directions(Ir):
    for i in range(len(Ir)):
        if Ir[i] < 10:
            integer_value = 0
        else:
            integer_value = 1
            
        if i == 0:
            ch = 'N' 
        elif i == 1:
            ch = 'S'
        elif i == 2:
            ch = 'E'
        else:
            ch = 'W'
        
        direction_dict[ch] = [integer_value]
    return direction_dict

def movement_Define(direction_dict):
    final_direction = None
    for d in 'ESNW':
        if direction_dict[d][0] == 1:
            print(f"Move to {d}")
            final_direction = d
            break
    return final_direction

possible_Directions = eval_Free_Directions(Ir)
possible_motion = movement_Define(possible_Directions)

len1 = len(path_coordinates)
curr_cell = (x1, y1)
goal = (x2, y2)

while curr_cell != goal:
    if curr_cell in path_coordinates:
        index_of_cell = path_coordinates.index(curr_cell) + 1
        temp_cell = path_coordinates[index_of_cell]
        if temp_cell[0] > curr_cell[0] and temp_cell[1] == curr_cell[1]:
            d = 'N'
        elif temp_cell[0] < curr_cell[0] and temp_cell[1] == curr_cell[1]:
            d = 'S'
        elif temp_cell[0] == curr_cell[0] and temp_cell[1] > curr_cell[1]:
            d = 'E'
        else:
            d = 'W'
        curr_cell = temp_cell
    elif curr_cell not in path_coordinates:
        plot_manhattan_distance(curr_cell[0], curr_cell[1], x2, y2)
        len2 = len(path_coordinates)
        if len2 < len1:
            index_of_cell = path_coordinates.index(curr_cell) + 1
            temp_cell = path_coordinates[index_of_cell]
            if temp_cell[0] > curr_cell[0] and temp_cell[1] == curr_cell[1]:
                d = 'N'
            elif temp_cell[0] < curr_cell[0] and temp_cell[1] == curr_cell[1]:
                d = 'S'
            elif temp_cell[0] == curr_cell[0] and temp_cell[1] > curr_cell[1]:
                d = 'E'
            else:
                d = 'W'
            curr_cell = temp_cell
    else:
        print("Wrong coordinates")
