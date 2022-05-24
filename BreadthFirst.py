import pygame
Red = (255,0,0)
Blue = (0,0,255)
Green = (0,255,0)
White = (255,255,255)
Yellow = (255,255,0)
Pink = (255, 0, 136)

def BreadthFirst(start_node, target_node, grid, showSteps):
    unexplored = []
    explored = []
    unexplored.append(start_node)
    showSteps = showSteps.get()

    start_node.color = Red
    target_node.color = Pink
    start_node.draw()
    target_node.draw()

    while len(unexplored) > 0:
        current_node = unexplored[0]
        neighbours = grid.getneighours(current_node)
        if current_node == target_node:
            path = retrace(current_node, start_node)
            for node in path:
                if node != target_node:
                    node.color = Blue
                    node.draw()
            return

        for neighbour in neighbours:
            if neighbour.walkable:
                if showSteps == 1:
                    if neighbour in explored:
                        neighbour.color = Yellow
                    elif neighbour in unexplored:
                        neighbour.color = Green
                    neighbour.draw()
                    pygame.display.update()

                if neighbour not in explored:
                    if neighbour not in unexplored:
                        unexplored.append(neighbour)
                        neighbour.parent = current_node

        unexplored.remove(current_node)
        explored.append(current_node)


def retrace(current_node, start_node):
    path = []
    while current_node != start_node:
        if current_node.parent !=  None:
            path.append(current_node)
            current_node = current_node.parent
    path.reverse()
    return path