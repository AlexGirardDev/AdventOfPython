import itertools
import math
f = [[y != "." for y in x] for x in open("input/2019/day10.txt", "r")]


def day9_1():

    doesColide(3, 9, 0, 0)
    doesColide(0, 3, 9, 0)
    doesColide(0, 0, 3, 9)
    doesColide(9, 0, 0, 3)
    # for x in f:
    #     for y in x:
    #         for x2 in f:
    #             for y2 in y:


def doesColide(x, y, x2, y2):
    print(f"--{x},{y},{x2},{y2}--")
    x_dif = x2 - x
    y_dif = y2 - y

    x_ang = x_dif / y_dif
    y_ang = y_dif / x_dif
    new_x = 0
    new_y = 0

    for z in range(1, abs(x_dif)):
        new_x = abs(x_dif) - z
        new_y = abs(y_dif) - (y_ang * z)
        if x_dif < 0 and y_dif < 0:
            new_x = x2 + new_x
            new_y = y2 + new_y
        elif x_dif > 0 and y_dif < 0:
            new_x = x2 - new_x
            new_y = y - (new_y-y)
        elif x_dif > 0 and y_dif > 0:
            new_x = x2 - new_x
            new_y = y2 - new_y
        elif x_dif < 0 and y_dif > 0:
            new_x = x - new_x
            new_y = new_y - y2
        if (new_x*1.0).is_integer() and (new_y*1.0).is_integer():
            print(f"{new_x},{new_y}")
    # if x_dif < y_dif:
    #     y_ang = y_dif/x_dif
    #     for z in range(1, y_dif):
    #         new_x = (y_dif - z) / y_ang - x_dif
    #         if (new_x - int(new_x) == 0):
    #             print(f"{x + new_x},{y2 + y_dif - z }")
    # if x_dif == y_dif:
    #     for z in range(y_dif):
    #         print(f"{x_dif-z},{y_dif-z}")


# def doesColide(x, y, x2, y2):
#     x_dif = x2 - x
#     y_dif = y2 - y

#     if x_dif > y_dif:
#         x_ang = x_dif / y_dif
#         for z in range(1, x_dif):
#             new_y = (x_dif - z)/x_ang + y_dif
#             if (new_y - int(new_y) == 0):
#                 print(f"{x2 + x_dif},{new_y}")
#     if x_dif < y_dif:
#         y_ang = y_dif/x_dif
#         for z in range(1, y_dif):
#             new_x = (y_dif - z) / y_ang - x_dif
#             if (new_x - int(new_x) == 0):
#                 print(f"{x + new_x},{y2 + y_dif - z }")
#     if x_dif == y_dif:
#         for z in range(y_dif):
#             print(f"{x_dif-z},{y_dif-z}")


def day9_2():
    pass


day9_1()
