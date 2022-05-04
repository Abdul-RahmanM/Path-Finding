import pygame


class Node:

    def __init__(self, walkable, x, y, color, win, windowY, windowX, gridX, gridY):
        self.windowY = windowY
        self.windowX = windowX
        self.gridX = gridX
        self.gridY = gridY
        self.win = win
        self.walkable = walkable
        self.x = x
        self.y = y
        self.color = color
        self.gCost = 0
        self.hCost = 0
        self.parent = None

    def getFcost(self):
        return self.gCost + self.hCost

    def draw(self):
        pygame.draw.rect(self.win, self.color,(self.x * (self.windowX / self.gridX), self.y * (self.windowY / self.gridY), 20, 20), 0)
        #pygame.draw.rect(self.win, self.grid[x][y].color,(x * (self.windowX / len(self.grid)), y * (self.windowY / len(self.grid)), 1000, 1000), 0)


