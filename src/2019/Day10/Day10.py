import itertools
import math
import numpy as np
import os.path
import os
from os import path
path = "C:\Dropbox\Github\AdventOfPython\Input\\2019\Day10.txt"
og = np.transpose([[0 if y == "." else 1 for y in x.strip()] for x in open(path, "r")])
f = og.copy()
output_result = False #this needs to be set to False if you want to run the visualizer
if output_result:
    print(path)
def day9_1():
    best_cords = []
    highest_count = 0
    for x in range(len(og)):
        for y in range(len(og[x])):
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
                        if not output_result:
                            print(f"{x}-{y},{x2},{y2},{los}")
            if count > highest_count:
                highest_count = count
                best_cords = [x,y]
            if output_result:
                print(f"{x},{y} - {count}")
    print(highest_count)
    print(best_cords)


def check_line_of_sight(x, y, x2, y2):
    if [x,y] == [x2, y2]:
        return 1
    x_dif = x2 - x
    y_dif = y2 - y
    new_x = 0
    new_y = 0
    if (abs(y_dif) == abs(x_dif)):
        for z in range(1, abs(y_dif)):
            new_x = x - z if x_dif < 0 else z + x
            new_y = y - z if y_dif < 0 else z + y
            if (f[int(new_x)][int(new_y)] != 0):
                return 1
        return 2
    if x_dif == 0 or y_dif == 0:
        for z in range(1, abs(y_dif + x_dif)):
            if x_dif != 0:
                new_x = x + z if x_dif > 0 else x - z
            if y_dif != 0:
                new_y = y + z if y_dif > 0 else y - z
            if (f[new_x][new_y] != 0):
                return 1
        return 2
    x_ang = x_dif / y_dif if y_dif != 0 else 0
    y_ang = y_dif / x_dif if x_dif != 0 else 0
    for z in range(1, abs(x_dif)):
        if (not (y_ang * z * 1.0).is_integer()):
            continue
        new_x = x + (abs(x_dif) - z) if x_dif >= 0 else x - (abs(x_dif) - z)
        new_y = y + (abs(y_dif) - abs(y_ang * z)) if y_dif >= 0 else y - (abs(y_dif) - abs(y_ang * z))
        if (new_x * 1.0).is_integer() and (new_y * 1.0).is_integer() and f[int(new_x)][int(new_y)] != 0:
            return 1
    return 2

day9_1()
