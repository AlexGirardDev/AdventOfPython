import itertools
import numpy
from time import perf_counter


class Moon:
    def __init__(self, x, y, z):
        self.pos = [x, y, z]
        self.vel = [0,0,0]
    
    def __repr__(self):
        return f"{self.pos}"

    def update_vel(self):
        for x in range(3):
            self.pos[x] += self.vel[x]

    def total_energy(self):
        kin = 0
        pot = 0
        for x in range(3):
            kin += abs(self.vel[x])
            pot += abs(self.pos[x])
        return kin * pot



# Moon(x=-1, y=0, z=2),
# Moon(x=2, y=-10, z=-7),
# Moon(x=4, y=-8, z=8),
# Moon(x=3, y=5, z=-1)]
moons = [
    Moon(x=-14, y=-4, z=-11),
    Moon(x=-9, y=6, z=-7  ),
    Moon(x=4, y=1, z=4   ),
    Moon(x=2, y=-14, z=-9)]

def time_step():
    for x in [[moons[0], moons[1]], [moons[0], moons[2]], [moons[0], moons[3]],
                [moons[1], moons[2]], [moons[1], moons[3]],
                [moons[2], moons[3]]]:
        for z in range(3):
            if x[0].pos[z] < x[1].pos[z]:
                x[0].vel[z] += 1
                x[1].vel[z] -= 1
            elif x[0].pos[z] > x[1].pos[z]:
                x[0].vel[z] -= 1
                x[1].vel[z] += 1
    for x in moons:
        x.update_vel()

def Day12_1():
    initial_1 =  (
        moons[0].vel[0],
        moons[1].vel[0],
        moons[2].vel[0],
        moons[3].vel[0],)
    initial_2 = (
        moons[0].vel[1],
        moons[1].vel[1],
        moons[2].vel[1],
        moons[3].vel[1])
    initial_3 =  (
        moons[0].vel[2],
        moons[1].vel[2],
        moons[2].vel[2],
        moons[3].vel[2])
    #186028
    done_1 = None
    done_2 = None
    done_3 = None
    for _ in range(1,1000000):
        time_step()
        #eng = sum(x.total_energy() for x in moons)
        now_1 =  (
            moons[0].vel[0],
            moons[1].vel[0],
            moons[2].vel[0],
            moons[3].vel[0],)
        now_2 =  (
            moons[0].vel[1],
            moons[1].vel[1],
            moons[2].vel[1],
            moons[3].vel[1])
        now_3 =  (
            moons[0].vel[2],
            moons[1].vel[2],
            moons[2].vel[2],
            moons[3].vel[2])
        if now_1 == initial_1 and not done_1:
            print(f"1-{_}")
            done_1 = _
        if now_2 == initial_2 and not done_2:
            print(f"2-{_}")
            done_2 = _
        if now_3 == initial_3 and not done_3:
            print(f"3-{_}")
            done_3 = _
        if done_1 and done_2 and done_3:
            break
    print(f"{done_1}-{done_2}-{done_3}")
    print(done_1*done_2*done_3)


    
    ellapsed = "{:10.10f}".format(perf_counter() - start)
    print(str(ellapsed))
#Day12_1()
one = 80714
two = 83812
three = 93014
wow = True
counter = 1
while wow:
    y = one *two* counter
    if  y % three == 0:
        print(y)
        wow = False
    counter +=1
        
wow = True
counter = 1
while wow:
    y = two *three* counter
    if   y % one == 0:
        print(y)
        wow = False
    counter += 1
wow = True
counter = 1
while wow:
    y =  three*one*counter
    if  y % two == 0:
        print(y)
        wow = False
    counter +=1
# print(161427*167623*186028)



