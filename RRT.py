import pygame
import tkinter as tk
from RequiredRRT import RRTGraph
from RequiredRRT import RRTMap

def main():
    dimensions = (600, 1000)
    print("Default dimention of Map is (600,1000)px \n")
    
    # start = (int(input("start x = ")),int(input("Start y = ")))
    # goal = (int(input("Goal X co-oridinate = ")), int(input("Goal Y co-ordinate = ")))
    # obsdim = int(input("Enter Obstical Dimention = "))
    # obsnum = int(input("Enter No. of Obsticals "))
    start = (50,50)
    goal = (510,510)
    obsdim = 30
    obsnum = 50
    iteration = 0
 
    pygame.init()
    map = RRTMap(start, goal, dimensions, obsdim, obsnum)
    graph = RRTGraph(start, goal, dimensions, obsdim, obsnum)

    obstacles = graph.makeobs()
    map.drawMap(obstacles)

    while(not graph.path_to_goal()):

        if iteration % 4 == 0:
            X, Y, parent = graph.bias(goal)
            pygame.draw.circle(map.map, map.gray, (X[-1], Y[-1]), map.nodeRad+2, 0)
            pygame.draw.line(map.map, map.blue, (X[-1], Y[-1]), (X[parent[-1]],Y[parent[-1]]), map.edgeThickness)

        else:
            x, y, parent = graph.expand()
            pygame.draw.circle(map.map, map.gray, (X[-1], Y[-1]), map.nodeRad+2, 0)
            pygame.draw.line(map.map, map.blue, (X[-1], Y[-1]), (X[parent[-1]], Y[parent[-1]]), map.edgeThickness)
        
        if iteration % 5 == 0:
            pygame.display.update()
        iteration += 1
        pygame.display.update()
        pygame.event.clear()
        pygame.event.wait(100)  
        

    map.drawPath(graph.getPathCoords())
    pygame.display.update()
    pygame.event.clear()
    pygame.event.wait(0)       




if __name__ == '__main__':
    # main()
    result = False
    while not result:
        try:
            main()
            result = True
        except:
            result = False