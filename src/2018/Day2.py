f = list(open("input/2018/day2.txt", "r"))


def day2_1(arg):
    two_count = 0
    three_count = 0
    for x in arg:
        letter_dict = {}
        for y in x:
            letter_dict[y] = letter_dict[y] + 1 if letter_dict.get(y) else 1

        if any(kvp[1] == 2 for kvp in letter_dict.items()):
            two_count += 1
        if any(kvp[1] == 3 for kvp in letter_dict.items()):
            three_count += 1
    return three_count * two_count


def day2_2(arg):
    for x in arg:
        for z in arg:
            differ_count = 0
            for i in range(len(x)-1):
                if x[i] != z[i]:
                    differ_count += 1
            if differ_count == 1:
                return "".join([x[y] for y in range(len(x)-1) if x[y] == z[y]])


print(day2_1(f))
print(day2_2(f))
