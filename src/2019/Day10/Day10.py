import itertools
import math
import numpy as np
import os.path
import os
from os import path
path = "C:\Dropbox\Github\AdventOfPython\Input\\2019\Day10.txt"
#print(os.getcwd())
print(path)
og = np.transpose([[0 if y == "." else 1 for y in x.strip()] for x in open(path, "r")])
#print(og)#
#print(og[1][0])
f = og.copy()
output_result = "AOC10_2019" not in os.getcwd()
def day9_1():

    
    # print(check_line_of_sight(1,2,0,3))
    # return



    highest_count = 0
    for x in range(len(og)):
        for y in range(len(og[x])):
            
            #x = 3
            #y = 4
            f = og.copy()
            if f[x][y] == 0:
                continue
            count = 0
            for x2 in range(len(f)):
                for y2 in range(len(f[0])):
                    if f[x2][y2] == 1:
                        los = check_line_of_sight(x, y, x2, y2)

                        if los is None:
                            continue
                        if (los == 2):
                            count += 1
                            #print(f"{x2},{y2}")
                        if not output_result:
                            print(f"{x}-{y},{x2},{y2},{los}")
                        #f[x2][y2] = los
            if count > highest_count:
                highest_count = count
            if output_result:
                pass#print(f"{x},{y} - {count}")
            #return
    print(highest_count)


def check_line_of_sight(x, y, x2, y2):
    # print(f"--{x},{y},{x2},{y2}--")
    if [x,y] == [x2, y2]:
        return 1
    x_dif = x2 - x
    y_dif = y2 - y
    if (abs(y_dif) == abs(x_dif)):
        for z in range(1, abs(y_dif)):
            new_x = x - z if x_dif < 0 else z + x
            new_y = y - z if y_dif < 0 else z + y
            #print(f"{new_x},{new_y}")
            if (f[int(new_x)][int(new_y)] != 0):
                return 1
        return 2

    if (x_dif == 0):
        if (y_dif > 0):
            for z in range(1,y_dif):
                if (f[x][y + z] != 0):
                    return 1
            return 2
        else:
            for z in range(1,abs(y_dif)):
                if (f[x][y - z] != 0):
                    return 1
            return 2
    if (y_dif == 0):
        if (x_dif > 0):
            for z in range(1,x_dif):
                if (f[x+z][y] != 0):
                    return 1
            return 2
        else:
            for z in range(1,abs(x_dif)):
                if (f[x-z][y] != 0):
                    return 1
            return 2
    x_ang = x_dif / y_dif
    y_ang = y_dif / x_dif
    new_x = 0
    new_y = 0
    for z in range(1, abs(x_dif)):
        if (not (y_ang * z).is_integer()):
            continue
        new_x = abs(x_dif) - z
        new_y = abs(y_dif) - abs(y_ang * z)
        new_x = x + new_x if x_dif >= 0 else x - new_x
        new_y = y + new_y if y_dif >= 0 else y - new_y
        if (new_x * 1.0).is_integer() and (new_y * 1.0).is_integer():
            #print(f"{new_x},{new_y}")
            if (f[int(new_x)][int(new_y)] != 0):
                return 1
    return 2

day9_1()
