import itertools
import math
og = [[(0 if y == "." else 1) for y in x] for x in open("input/2019/day10.txt", "r")][::-1]
f = og.copy()
def day9_1():
    print(og[1][0])
    for x in range(len(og)):
        for y in range(len(og[x])):
            f = og.copy()
            if f[x][y] == 0:
                continue
            count = 0
            for x2 in range(len(f)):
                for y2 in range(len(f[x2])):
                    if f[x2][y2] == 1:
                        los = check_line_of_sight(x, y, x2, y2)
                        
                        if los is None:
                            continue
                        
                        if (los == 2):
                            count += 1
                        f[x2][y2] = los
            print(f"{x},{y} - {count}")


def check_line_of_sight(x, y, x2, y2):
    #print(f"--{x},{y},{x2},{y2}--")
    if {x, y} == {x2, y2}:
        return 1
    x_dif = x2 - x
    y_dif = y2 - y


    try:
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
            if (new_x * 1.0).is_integer() and (new_y * 1.0).is_integer():
                if (f[int(new_x)][int(new_y)] != 0):
                    return f[int(x2)][int(y2)]

                #print(f"{new_x},{new_y}")
        return 2
    except ZeroDivisionError:
        return None #f[int(new_x)][int(new_y)]
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
