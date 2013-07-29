import pygame, sys
from pygame.locals import *
import random

FPS = 5
WINDOWWIDTH = 600
WINDOWHEIGHT = 400
CELLSIZE = 10

assert WINDOWWIDTH % CELLSIZE == 0, "Window width must be a multiple of cell size"
assert WINDOWHEIGHT % CELLSIZE == 0, "Window height must be a multiple of cell size"

CELLWIDTH = WINDOWWIDTH / CELLSIZE #number of cells wide
CELLHEIGHT = WINDOWHEIGHT / CELLSIZE #number of cells high

#set up the colours
BLACK =  	(0,    0,  0)
WHITE =		(255,255,255)
DARKGREY =	(40,  40, 40)
GREEN =		(0,  255,  0)

#Draws the grid lines
def drawGrid():
	for x in range(0, WINDOWWIDTH, CELLSIZE): #draw vertical lines
		pygame.draw.line(DISPLAYSURF, DARKGREY, (x,0),(x,WINDOWHEIGHT))
	for y in range(0, WINDOWHEIGHT, CELLSIZE): #draw horizontal lines
		pygame.draw.line(DISPLAYSURF, DARKGREY, (0,y), (WINDOWWIDTH,y))

def blankGrid():
	gridDict = {}
	for y in range (CELLHEIGHT):
		for x in range (CELLWIDTH):
			gridDict[x,y] = 0
	return gridDict

def startingGridRandom(lifeDict):
	for item in lifeDict:
		lifeDict[item] = random.randint(0,1)
	return lifeDict

def colourGrid(item, lifeDict):
	x = item[0]
	y = item[1]
	y = y * CELLSIZE # transplates array into grid size
	x = x * CELLSIZE 
	if lifeDict[item] == 0:
		pygame.draw.rect(DISPLAYSURF, WHITE, (x, y, CELLSIZE, CELLSIZE))
	if lifeDict[item] == 1:
		pygame.draw.rect(DISPLAYSURF, GREEN, (x, y, CELLSIZE, CELLSIZE))
	return None

def getNeighbours(item, lifeDict):
	neighbours = 0
	for x in range (-1, 2):
		for y in range (-1, 2):
			checkCell = (item[0]+x, item[1]+y)
			if checkCell[0] < CELLWIDTH and checkCell[0] >=0:
				if checkCell[1] < CELLHEIGHT and checkCell[1] >=0:
					if lifeDict[checkCell] == 1:
						if x == 0 and y == 0:
							neighbours += 0
						else:
							neighbours += 1
	return neighbours

def tick(lifeDict):
	newTick = {}
	for item in lifeDict:
		numberNeighbours = getNeighbours(item, lifeDict)
		if lifeDict[item] == 1:
			if numberNeighbours < 2:
				newTick[item] = 0
			elif numberNeighbours > 3:
				newTick[item] = 0
			else:
				newTick[item] = 1
		elif lifeDict[item] == 0:
			if numberNeighbours == 3:
				newTick[item] = 1
			else:
				newTick[item] = 0
	return newTick

def main():
	pygame.init()
	global DISPLAYSURF
	FPSCLOCK = pygame.time.Clock()
	DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH,WINDOWHEIGHT))
	pygame.display.set_caption('Game of Life')
	
	DISPLAYSURF.fill(WHITE) #fills the screen white

	lifeDict = blankGrid() # creates library and populates to match blank grid
	lifeDict = startingGridRandom(lifeDict) #assign random life
	for item in lifeDict:
		colourGrid(item, lifeDict)

	while True: #main game loop
		for event in pygame.event.get():
			if event.type == QUIT:
				pygame.quit()
				sys.exit()
		# runs a tick
		lifeDict = tick(lifeDict)
		# colours the live cells, blancks the dead
		for item in lifeDict:
			colourGrid(item, lifeDict)
		drawGrid()
		pygame.display.update()
		FPSCLOCK.tick(FPS)

if __name__=='__main__':
	main()
