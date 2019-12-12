import itertools
import math
import numpy as np
import os.path
import os
from os import path
path = "C:\Dropbox\Github\AdventOfPython\Input\\2019\Day10.txt"
f = np.transpose([[0 if y == "." else 1 for y in x.strip()] for x in open(path, "r")])
print(path)
def angle_between(p1, p2):
    ang1 = np.arctan2(*p1[::-1])
    ang2 = np.arctan2(*p2[::-1])
    return np.rad2deg((ang1 - ang2) % (2 * np.pi))

def angle_between_2(p1, p2):
    ang = math.degrees(math.atan2(p2[1] - p1[1], p2[0] - p1[0])) +90
    if ang < 0:
        ang += 360
    
    return ang

# print(angle_between_2((3, 3), (3, 2)))
# print(angle_between_2((3, 3), (4, 2)))
# print(angle_between_2((3, 3), (4, 3)))
# print(angle_between_2((3, 3), (4, 4)))
# print(angle_between_2((3, 3), (3, 4)))
# print(angle_between_2((3, 3), (2, 4)))
# print(angle_between_2((3, 3), (2, 3)))
# print(angle_between_2((3, 3), (2, 2)))


def day9_2():
    x = 31
    y = 20
    diff = 0
    counter = 0
    asteroids_to_die = []
    wow = True
    #print(path)
    output = []
    while wow:
        diff += len(asteroids_to_die)
        asteroids_to_die = []
        wow = False
        for x2 in range(len(f)):
            for y2 in range(len(f[0])):
                if f[x2][y2] == 1 :#and counter<=199:
                    los = check_line_of_sight(x, y, x2, y2)
                    if los is None:
                        continue
                    if (los == 2):
                        asteroids_to_die.append((x2, y2, angle_between_2((x, y), (x2, y2))))
                        wow = True
                       
                        #asteroids_to_die.sort(key=lambda z: z[2])
                        counter += 1
        for z in asteroids_to_die:
            f[z[0]][z[1]] = 0
        asteroids_to_die.sort(key=lambda z: z[2])
        output = output + asteroids_to_die
    for z in output:
        print(f"{x}-{y},{z[0]},{z[1]},1")
    #print(asteroids_to_die[200 - diff])
    
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

day9_2()
