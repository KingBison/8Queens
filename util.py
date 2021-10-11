import numpy as np
from random import randint

def generateGrid():
    grid = np.zeros([8,8])
    
    for k in range(8):
        queen = randint(0,7)
        grid[queen][k] = 1

    return grid

def getH(grid):
    queen_locs = np.zeros([8,2])
    for k in range(8):
        for i in range(8):
            if grid[i][k] == 1:
                queen_locs[k] = [k, i]

    h = 0

    list_of_k = []
    for queen in queen_locs:
        if queen[1] in list_of_k:
            h = h + 1
        else:
            list_of_k.append(queen[1])

    list_of_i_plus_k = []
    for queen in queen_locs:
        if queen[1] +queen[0] in list_of_i_plus_k:
            h = h + 1
        else:
            list_of_i_plus_k.append(queen[1]+queen[0])

    list_of_i_minus_k = []
    for queen in queen_locs:
        if queen[1] -queen[0] in list_of_i_minus_k:
            h = h + 1
        else:
            list_of_i_minus_k.append(queen[1]-queen[0])
    
    return h

def findLowestNeighbor(grid):
    origional = grid
    origional_h = getH(grid)
    lowest_h = np.copy(grid)
    lower_h_count = 0

    print("Current h: " + str(origional_h))
    print("Current State")
    print(origional)


    for k in range(8):
        for loop in range(8):
            zero_value = grid[0][k]
            for i in range(7):
                grid[i][k] = grid[i+1][k]
            grid[7][k] = zero_value

            if getH(grid) < origional_h:
                lower_h_count = lower_h_count + 1
            
            if getH(grid) < getH(lowest_h):
                lowest_h = np.copy(grid)
  

    print("Neigbors found with lower h: " + str(lower_h_count))
    
    if getH(lowest_h) == 0:
        print("")
        print("Current State")
        print(lowest_h)
        return "done"
    elif lower_h_count == 0:
        return "restart"
    else:
        return lowest_h




    

