from util import *

grid = generateGrid()
state_changes = 0
restarts = 0
findLowestNeighbor(grid)
done = False
while not done:
    out = findLowestNeighbor(grid)

    if out == "done":
        print("Solution Found!")
        print("State changes: " + str(state_changes))
        print("Restarts: " + str(restarts))
        done = True
    elif out == "restart":
        print("RESTART")
        restarts += 1
        grid = generateGrid()
    else:
        print("Setting new current state")
        state_changes += 1
        grid = out

    print("")

