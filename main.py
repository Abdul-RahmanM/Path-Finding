from tkinter import *
from tkinter import ttk

import pygame

from Astar import Astar
from BreadthFirst import BreadthFirst
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
    algo_ran = False
    algorithm = algorithm.get()

    #Verify user input was valid
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

    if algorithm == "Algorithms":
        error = Label(root, text=" Please select an algorithm ")
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
        if algo_ran == False:
            run_text = grid.STAT_FONT.render("Press X to run", 1, (255, 0, 0))
            grid.win.blit(run_text, (grid.windowX - 10 - run_text.get_width(), 10))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                pygame.display.quit()
                quit()



            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_x:
                    if algo_ran == True:
                        grid.reset()
                    algo_ran = True
                    if algorithm == "Astar":
                        Astar(start_node, target_node, grid, showSteps)
                    elif algorithm == "Breadth-first":
                        BreadthFirst(start_node, target_node, grid, showSteps)
                    for x in range(len(grid.grid)):
                        for y in range(len(grid.grid)):
                            grid.grid[x][y].draw()
                    grid.drawgrid()
                    reset_text = text = grid.STAT_FONT.render("Click Anywhere To Reset", 1, (255, 0, 0))
                    grid.win.blit(reset_text, (grid.windowX - 10 - text.get_width(), 10))


        # Barrier Creation Destruction and reset
        mouse_pos = pygame.mouse.get_pos()
        x, y = mouse_pos
        x = int(x / 20)
        y = int(y / 20)
        if pygame.mouse.get_pressed() == (True, False, False) or pygame.mouse.get_pressed() == (False,False,True):
            clicked_node = grid.grid[x][y]

            if algo_ran == True:
                start_node.draw()
                target_node.draw()
                grid.reset()
                algo_ran = False

            if pygame.mouse.get_pressed() == (True, False, False):
                if clicked_node != target_node:
                    if clicked_node != start_node:
                        clicked_node.color = White
                        clicked_node.walkable = False
                        clicked_node.draw()

            if pygame.mouse.get_pressed() == (False,False,True):
                if clicked_node != target_node:
                    if clicked_node != start_node:
                        clicked_node.color = Black
                        clicked_node.walkable = True
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
