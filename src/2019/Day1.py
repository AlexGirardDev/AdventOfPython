f = [int(x) for x in open("input/2019/day1.txt", "r")]


def calc_mass(x):
    return x // 3 - 2


def day2_1():
    print(str(sum([calc_mass(x) for x in f])))


def day2_2():
    total = 0
    for x in f:
        total_weight = calc_mass(x)
        extra_weight = calc_mass(total_weight)
        while extra_weight > 0:
            # print(f"t:{total_weight}e:{extra_weight}")
            total_weight += extra_weight
            extra_weight = calc_mass(extra_weight)
        # print(total_weight)
        total += total_weight
    print(total)


# day2_1()
# day2_2()
