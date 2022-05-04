import pygame
from Node import Node
class Grid:

    def __init__(self, windowX, windowY, gridX, gridY):
        self.gridX = gridX
        self.gridY = gridY
        self.windowY = windowY
        self.windowX = windowX
        self.win = pygame.display.set_mode((windowX, windowY))

        self.grid = [[Node(True, x, y, (0,0,0), self.win, windowY, windowX, gridX, gridY) for y in range(gridX)] for x in range(gridY)]

    def getneighours(self, current_node):
        neighbours = []
        x = current_node.x
        y = current_node.y

        for x in range(-1, 2):
            for y in range(-1, 2):
                neighbourX = current_node.x + x
                neighbourY = current_node.y + y
                if x == 0 and y == 0:
                    continue
                if neighbourX >= 0  and neighbourX < len(self.grid):
                    if neighbourY >= 0 and neighbourY < len(self.grid):
                        neighbours.append(self.grid[neighbourX][neighbourY])

        return neighbours


    def drawgrid(self):
        for x in range(len(self.grid)):
            for y in range(len(self.grid)):
                #pygame.draw.rect(self.win, self.grid[x][y].color, (x * (self.windowX/len(self.grid)), y * (self.windowY/len(self.grid)), 20, 20), 0)
                pygame.draw.line(self.win, (255,255,255), (x * (self.windowX/len(self.grid)), 0), (x * (self.windowX/len(self.grid)), y + self.windowY), 1)
                pygame.draw.line(self.win, (255,255,255), (0, y * (self.windowX/len(self.grid))), (0 + self.windowX, y * (self.windowX/len(self.grid))), 1)



