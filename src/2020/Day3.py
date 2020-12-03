import numpy as np
f = [x for x in open("Input/3.txt", "r")]


def printGrid(grid):
    for yy in range(len(grid)):
        str = ""
        for xx in range(len(grid[yy])):
            if grid[yy][xx]== True:
                str+= "#"
            elif grid[yy][xx]== False:
                str+= "."
            else:
                str+= grid[yy][xx]

        print(str)



def part1():
    grid =[] 
    for r in f:
        newGrid = []
        for z in r:
            if(z=="#"):
                newGrid.append(1)
            else:
                newGrid.append(0)

        if len(newGrid):
            newGrid.pop()
            grid.append(newGrid)

    maxY =len(grid)
    maxX =len(grid[0])
    x=0
    y=0
    count= 0
    while True:
        x += 3
        y += 1
        if(x>=maxX-1):
            x = x- maxX 
        if(y>=maxY):
            break
        if grid[y][x] :
            count += 1
    print(count)




def part2():
    grid =[] 
    for r in f:
        newGrid = []
        for z in r:
            if(z=="#"):
                newGrid.append(1)
            else:
                newGrid.append(0)
        if len(newGrid):
            newGrid.pop()
            grid.append(newGrid)
    increments = [[1,1],[3,1],[5,1],[7,1],[1,2]]
    total= 1
    for i in increments:
        maxY =len(grid)
        maxX =len(grid[0])
        x=0
        y=0
        count= 0
        while True:
            x += i[0]
            y += i[1]
            if(x>=maxX-1):
                x = x - maxX 
            if(y>=maxY):
                break
            if grid[y][x] :
                count += 1
        total *= count
    print(total)
part1()
part2()
