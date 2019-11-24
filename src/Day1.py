f = list(open("input/day1.txt", "r"))


def day_1_1(arg):
    return sum(int(x) for x in arg)


def day_1_2(arg):
    numbers = set()
    freq = 0
    Done = False
    while not Done:
        for x in f:
            freq += int(x)
            if(freq in numbers):
                Done = True
                break
            else:
                numbers.add(int(freq))
    return freq


print(day_1_1(f))
print(day_1_2(f))
