f = list(open("input/day3.txt", "r"))


def day3_1(arg):
    grid_size = 1000
    grid = [[[] for y in range(grid_size)] for x in range(grid_size)]

    for a in arg:
        a = str.replace(str.replace(a, " ", ""),"\\n","")
        id =int(str.replace(str.replace(a, "#", ""), " ", "").split("@")[0])
        x_pos = int(a.split("@")[1].split(",")[0])
        y_pos = int(a.split("@")[1].split(",")[1].split(":")[0])
        w_grid = int(a.split(":")[1].split("x")[0])
        h_grid = int(a.split("x")[1])
        print(id)
        for x in range(w_grid):
            for y in range(h_grid):
                grid[x_pos + x][y_pos + y].append(id)
        
    result = 0
    for x in grid:
        for y in x:
            if len(y) > 1:
                result +=1

    return result


print(day3_1(f))
