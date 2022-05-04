from tkinter import *
from tkinter import ttk

import pygame

from Algorithms.Astar import Astar
from Algorithms.BreadthFirst import BreadthFirst
from Grid import Grid

root = Tk()

grid = Grid(1000, 1000, 50, 50)
Red = (255,0,0)
Blue = (0,0,255)
Green = (0,255,0)
White = (255,255,255)
Yellow = (255,255,0)
Black = (0,0,0)
Pink = (255, 0, 136)

def main(startBox, targetBox, showSteps, algorithm):
    algorithm = algorithm.get()
    try:
        startX, startY = startBox.get().split(',')
        targetX, targetY = targetBox.get().split(',')

    except ValueError:
        error = Label(root, text="Only input numbers as (x,y)")
        error.grid(row=8, column=1, sticky=W)
        root.mainloop()

    try:
        start_node = grid.grid[int(startX)][int(startY)]
        target_node = grid.grid[int(targetX)][int(targetY)]

    except IndexError:
        error = Label(root, text=" VALUES OUT OF GRID RANGE ")
        error.grid(row=8, column=1, sticky=W)
        root.mainloop()

    root.destroy()

    start_node.color = Red
    target_node.color = Pink

    start_node.draw()
    target_node.draw()

    clock = pygame.time.Clock()
    run = True
    while run:
        clock.tick(30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    if algorithm == "Astar":
                        Astar(start_node, target_node, grid, showSteps)
                        grid.drawgrid()

                    elif algorithm == "Breadth-first":
                        BreadthFirst(start_node, target_node, grid, showSteps)
                        grid.drawgrid()


        # Barrier Creation
        if pygame.mouse.get_pressed() == (True, False, False):
            mouse_pos = pygame.mouse.get_pos()
            x, y = mouse_pos
            x = int(x/20)
            y = int(y/20)
            clicked_node = grid.grid[x][y]
            if clicked_node != target_node:
                if clicked_node != start_node:
                    clicked_node.color = White
                    clicked_node.walkable = False
                    clicked_node.draw()
        pygame.display.update()

def getEntry():
    root.geometry("300x300")
    showSteps = IntVar()

    # Label and Input Box for Start_node location
    label = Label(root, text="StartPos(x,y): ", font=("Courier 15 bold"))
    label.grid(row=1, column=1, sticky=W)

    startBox = Entry(root, width=40)
    startBox.grid(row=1, column=2, sticky=E)

    # Label and Input Box for Target_node location
    label = Label(root, text="TargetPos(x,y): ", font=("Courier 15 bold"))
    label.grid(row=2, column=1, sticky=W, pady= 10)

    targetBox = Entry(root, width=40)
    targetBox.grid(row=2, column=2, sticky=E)

    # Check Box to show steps or not
    stepsCheck = ttk.Checkbutton(root, text='Steps :', onvalue=1, offvalue=0, variable = showSteps)
    stepsCheck.grid(row=5, column=2, sticky=W, pady= 5)

    # Drop-down menu for different algorithms
    menu = StringVar()
    menu.set("Astar")
    algoOptions = ttk.OptionMenu(root, menu, "Algorithms", "Breadth-first", "Astar")
    algoOptions.grid(row=5, column=1, sticky=W, pady= 5)
    algorithm = menu

    # Run button
    runButton = ttk.Button(root, text="Confirm", width=20, command = lambda : main(startBox, targetBox, showSteps, algorithm))
    runButton.grid(row=7, column=1, sticky=E, pady= 10)

    root.mainloop()

getEntry()
