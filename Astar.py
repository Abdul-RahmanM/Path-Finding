import pygame

Red = (255,0,0)
Blue = (0,0,255)
Green = (0,255,0)
White = (255,255,255)
Yellow = (255,255,0)
Pink = (255, 0, 136)

def Astar(start_node, target_node, grid, showSteps):
    showSteps = showSteps.get()
    unexplored = []
    explored = []
    unexplored.append(start_node)

    while len(unexplored) > 0:

        start_node.color = Red
        target_node.color = Pink
        start_node.draw()
        target_node.draw()

        current_node = unexplored[0]

        for node in unexplored:
            if node.getFcost() < current_node.getFcost() or (node.getFcost() == current_node.getFcost() & node.hCost < current_node.hCost):
                current_node = node

        unexplored.remove(current_node)
        explored.append(current_node)


        if current_node == target_node:
            path = retrace(current_node, start_node)
            for node in path:
                if node != target_node:
                    node.color = Blue
                    node.draw()

            return

        neighbours = grid.getneighours(current_node)

        for neighbour in neighbours:
            if neighbour.walkable == True:
                if neighbour.color != (255, 0, 0) or (0, 255, 0):
                    if showSteps == 1:
                        if neighbour in unexplored:
                            neighbour.color = Green
                        elif neighbour in explored:
                            neighbour.color = Yellow
                        neighbour.draw()
                        pygame.display.update()

                if neighbour in explored:
                    continue
                newNeighbourGcost = current_node.gCost + getDist(current_node, neighbour)
                if newNeighbourGcost < neighbour.gCost or neighbour not in unexplored:
                    neighbour.gCost = newNeighbourGcost
                    neighbour.hCost = getDist(neighbour, target_node)

                    neighbour.parent = current_node

                    if not neighbour in unexplored:
                        unexplored.append(neighbour)



def getDist(current_node, neighbour_node):
    distanceX = abs(current_node.x - neighbour_node.x)
    distanceY = abs(current_node.y - neighbour_node.y)

    if distanceX > distanceY:
        return 14 * distanceY + 10*(distanceX-distanceY)
    else:
        return 14 * distanceX + 10*(distanceY-distanceX)

def retrace(current_node, start_node):
    path = []

    while current_node != start_node:
        if current_node.parent != None:
            path.append(current_node)
            current_node = current_node.parent
    path.reverse()
    return path