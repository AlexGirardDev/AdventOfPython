f = [int(y)
     for y in [x for x in open("input/2019/day2.txt", "r")][0].split(',')]
input = f.copy()


def day1_1():
    opcode = 0
    while True:
        if (f[opcode] == 99):
            print(f[0])
            return
        add = f[opcode] == 1
        pos1 = f[opcode + 1]
        pos2 = f[opcode + 2]
        pos_result = f[opcode + 3]
        if add:
            f[pos_result] = f[pos1] + f[pos2]
        else:
            f[pos_result] = f[pos1] * f[pos2]

        opcode += 4
    # print(f)


def day2_2():
    opcode = 0
    for noun in range(100):
        for verb in range(100):
            f = input.copy()
            f[1] = noun
            f[2] = verb
            opcode = 0
            while True:
                if (f[opcode] == 99):
                    if f[0] == 19690720:
                        print(f"{100 * noun + verb}")
                        return
                    break
                add = f[opcode] == 1
                idx1 = f[opcode + 1]
                idx2 = f[opcode + 2]
                idx3 = f[opcode + 3]
                if add:
                    f[idx3] = f[idx1] + f[idx2]
                else:
                    f[idx3] = f[idx1] * f[idx2]

                opcode += 4


day1_1()
day2_2()
