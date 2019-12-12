import itertools
import math
import numpy as np
og = np.transpose([[0 if y =="." else 1 for y in x.strip()] for x in open("input/2019/day10.txt", "r")])
#print(og[1][0])
f = og.copy()

def angle_between(p1, p2):
    ang1 = np.arctan2(*p1[::-1])
    ang2 = np.arctan2(*p2[::-1])
    return np.rad2deg((ang1 - ang2) % (2 * np.pi))

def calculateDistance(p1,p2):  
     dist =  math.sqrt( ((p1[0]-p2[0])**2)+((p1[1]-p2[1])**2) )
     return dist 
def day10_1():
    perm = list(itertools.product(range(len(f)), range(len(f[0]))))
    for i in perm:
        if f[i[0]][i[1]] == 0:
            continue
        count = 0
      
        for z in perm:
            failed = True
            if z == i:
                continue
            for x in perm:
                if f[x[0]][x[1]] == 0 or f[z[0]][z[1]] == 0 or z == x or x == i:
                    continue
                failed = False
                z_dist = calculateDistance(i, z)
                x_dist = calculateDistance( i,x)
                z_ang = angle_between(i, z)
                x_ang  = angle_between( i,x)
                if x_ang == z_ang and  z_dist > x_dist :
                    failed = True
            if not failed:
                count += 1
                #failed = False
        print(f"{i[0]},{i[1]} - {count}")

#print(calculateDistance( (1, 3),(0, 0)))
#print(calculateDistance((0,0),(2,6)))
#day10_1()
i = (0, 0)
z = (9, 3)
x = (6,2)
z_dist = calculateDistance(i, z)
x_dist = calculateDistance(i, x)
z_ang = angle_between(i, z)
x_ang = angle_between(i, x)
print(z_dist)
print(x_dist)
print(z_ang)
print(x_ang)

day10_1()