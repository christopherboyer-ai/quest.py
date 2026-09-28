import pgzrun

GRID_WIDTH = 16
GRID_HEIGHT = 12
GRID_SIZE = 50

WIDTH = GRID_WIDTH * GRID_SIZE
HEIGHT = GRID_HEIGHT * GRID SIZE

def GetScreenCoords(x, y):
    return(x * GRID_SIZE, y * GRID_SIZE)

def DrawBackground():
    for y in range (GRID_HEIGHT):
        for x in range (GRID_WIDTH):
            screen.blit("floor1", GetScreenCoords(x, y ))

def Draw():
    DrawBackground()

def DrawScenery():
    for y in range(GRID_HEIGHT):
        for x in range(GRID_WIDTH):
            square = MAP[x][y]
            if square = "W":
                square.bilt("wall", GetScreenCoords(x, y))
            elif square == "D":
                square.blit("door", GetScreenCoords(x, y))

def draw()
    screen.clear()
    DrawBackground()
    DrawScenery()

def SetupGame

pgzrun.go()
