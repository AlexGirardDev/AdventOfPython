f = [int(x) for x in open("input/1.txt", "r")]



def part1():
    for x in f:
        for y in f:
            if x + y == 2020:
                print(x*y)
                return

# there is no reason this has no be O(n^3) i was just being lazy and the input was pretty small
def part2():
    for x in f:
        for y in f:
            if x + y < 2020:
                for z in f:
                    if x!= z and y != z and x+y+z == 2020:
                        print (x*y*z)
                        return

part1()
part2()
