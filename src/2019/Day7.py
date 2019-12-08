import itertools
og = [int(x)
      for x in '3,8,1001,8,10,8,105,1,0,0,21,42,63,76,101,114,195,276,357,438,99999,3,9,101,2,9,9,102,5,9,9,1001,9,3,9,1002,9,5,9,4,9,99,3,9,101,4,9,9,102,5,9,9,1001,9,5,9,102,2,9,9,4,9,99,3,9,1001,9,3,9,1002,9,5,9,4,9,99,3,9,1002,9,2,9,101,5,9,9,102,3,9,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,101,3,9,9,102,2,9,9,4,9,99,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,99,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,99'.split(',')]
# f = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
#      1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
#      999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
# f=[3,3,1105,-1,9,1101,0,0,12,4,12,99,1]
f = og.copy()


def day5_1():
    values = list(itertools.permutations([0, 1, 2, 3, 4], 5))
    count = 0
    highest_value = 0
    for v in values:
        output = 0
        best_seq = []
        output_count = 0
        for x in range(5):
            done = False
            opcode = 0
            f = og.copy()
            # print(output)
            first_input = False
            while not done:
                count += 1

                instruction = ("00000" + str(f[opcode]))[-5:]
                opcode_instruction = instruction[-1:]
                if instruction[-2:] == '99':
                    # print("!!!HALT!!!")
                    done = True
                # print(f"{f[opcode]}-{f[opcode+1]}-{f[opcode+2]}-{f[opcode+3]}")
                # Input
                elif opcode_instruction == '3':
                    # print('input')
                    if not first_input:
                        f[f[opcode + 1]] = v[x]
                        first_input = True
                    else:
                        f[f[opcode + 1]] = output
                    opcode += 2
                # output
                elif opcode_instruction == '4':
                    param_1 = f[f[opcode + 1]
                                ] if instruction[2] == '0' else f[opcode + 1]
                    output = param_1
                    output_count += 1
                    # print(output)
                    opcode += 2
                # add
                elif opcode_instruction == '1':
                    param_1 = f[f[opcode + 1]
                                ] if instruction[2] == '0' else f[opcode + 1]
                    param_2 = f[f[opcode + 2]
                                ] if instruction[1] == '0' else f[opcode + 2]
                    param_3 = f[opcode + 3]
                    f[param_3] = param_1 + param_2
                    opcode += 4
                # Mult
                elif opcode_instruction == '2':
                    param_1 = f[f[opcode + 1]
                                ] if instruction[2] == '0' else f[opcode + 1]
                    param_2 = f[f[opcode + 2]
                                ] if instruction[1] == '0' else f[opcode + 2]
                    param_3 = f[opcode + 3]
                    f[param_3] = param_1 * param_2
                    opcode += 4
                # Jump if true
                elif opcode_instruction == '5':
                    param_1 = f[f[opcode + 1]
                                ] if instruction[2] == '0' else f[opcode + 1]
                    param_2 = f[f[opcode + 2]
                                ] if instruction[1] == '0' else f[opcode + 2]
                    if param_1 != 0:
                        opcode = param_2
                    else:
                        opcode += 3
                # Jump if False
                elif opcode_instruction == '6':
                    param_1 = f[f[opcode + 1]
                                ] if instruction[2] == '0' else f[opcode + 1]
                    param_2 = f[f[opcode + 2]
                                ] if instruction[1] == '0' else f[opcode + 2]
                    if param_1 == 0:
                        opcode = param_2
                    else:
                        opcode += 3
                # Less Than
                elif opcode_instruction == '7':
                    param_1 = f[f[opcode + 1]
                                ] if instruction[2] == '0' else f[opcode + 1]
                    param_2 = f[f[opcode + 2]
                                ] if instruction[1] == '0' else f[opcode + 2]
                    param_3 = f[opcode + 3]
                    if param_1 < param_2:
                        f[param_3] = 1
                    else:
                        f[param_3] = 0
                    opcode += 4
                # equals
                elif opcode_instruction == '8':
                    param_1 = f[f[opcode + 1]
                                ] if instruction[2] == '0' else f[opcode + 1]
                    param_2 = f[f[opcode + 2]
                                ] if instruction[1] == '0' else f[opcode + 2]
                    param_3 = f[opcode + 3]
                    if param_1 == param_2:
                        f[param_3] = 1
                    else:
                        f[param_3] = 0
                    opcode += 4
            # print(output)
        print(output_count)
        if output > highest_value:
            highest_value = output
            best_seq = "".join([str(q) for q in v])
    # print(best_seq)
    print(highest_value)


class IntCode():
    def __init__(self, int_code, phase):
        self.int_code = int_code
        self.phase = phase
        self.input = 0
        self.done = False
        self.first_input = False
        self.opcode = 0
        self.last_output = 0

    def get_param(self, i, inst):
        return self.int_code[self.int_code[self.opcode + i]
                             ] if inst[3-i] == '0' else self.int_code[self.opcode + 1]

    def opcode_input(self, instruction):
        if not self.first_input:
            self.int_code[self.int_code[self.opcode + 1]] = self.phase
            self.first_input = True
        else:
            self.int_code[self.int_code[self.opcode + 1]] = self.input
            self.opcode += 2

    def iterate(self, input):
        self.input = input
        output = 0
        while True:
            instruction = ("00000" + str(self.int_code[self.opcode]))[-5:]
            opcode_instruction = instruction[-1:]
            if instruction[-2:] == '99':
                self.done = True
                return self.last_output
                # print("!!!HALT!!!")
                self.done = True
            # print(f"{self.input[opcode]}-{self.input[opcode+1]}-{self.input[opcode+2]}-{self.input[opcode+3]}")
            # Input
            elif opcode_instruction == '3':
                # print('input')
                self.opcode_input(instruction)
            # output
            elif opcode_instruction == '4':
                param_1 = self.get_param(1, instruction)
                output = param_1
                self.opcode += 2
                self.last_output = output
                return output
            # add
            elif opcode_instruction == '1':
                param_1 = self.int_code[self.int_code[self.opcode + 1]
                                        ] if instruction[2] == '0' else self.int_code[self.opcode + 1]
                param_2 = self.int_code[self.int_code[self.opcode + 2]
                                        ] if instruction[1] == '0' else self.int_code[self.opcode + 2]
                param_3 = self.int_code[self.opcode + 3]
                self.int_code[param_3] = param_1 + param_2
                self.opcode += 4
            # Mult
            elif opcode_instruction == '2':
                param_1 = self. int_code[self.int_code[self.opcode + 1]
                                         ] if instruction[2] == '0' else self.int_code[self.opcode + 1]
                param_2 = self.int_code[self.int_code[self.opcode + 2]
                                        ] if instruction[1] == '0' else self.int_code[self.opcode + 2]
                param_3 = self.int_code[self.opcode + 3]
                self.int_code[param_3] = param_1 * param_2
                self.opcode += 4
            # Jump if true
            elif opcode_instruction == '5':
                param_1 = self.int_code[self.int_code[self.opcode + 1]
                                        ] if instruction[2] == '0' else self.int_code[self.opcode + 1]
                param_2 = self.int_code[self.int_code[self.opcode + 2]
                                        ] if instruction[1] == '0' else self.int_code[self.opcode + 2]
                if param_1 != 0:
                    self.opcode = param_2
                else:
                    self.opcode += 3
            # Jump if False
            elif opcode_instruction == '6':
                param_1 = self.int_code[self.int_code[self.opcode + 1]
                                        ] if instruction[2] == '0' else self.int_code[self.opcode + 1]
                param_2 = self.int_code[self.int_code[self.opcode + 2]
                                        ] if instruction[1] == '0' else self.int_code[self.opcode + 2]
                if param_1 == 0:
                    self.opcode = param_2
                else:
                    self.opcode += 3
            # Less Than
            elif opcode_instruction == '7':
                param_1 = self.int_code[self.int_code[self.opcode + 1]
                                        ] if instruction[2] == '0' else self.int_code[self.opcode + 1]
                param_2 = self.int_code[self.int_code[self.opcode + 2]
                                        ] if instruction[1] == '0' else self.int_code[self.opcode + 2]
                param_3 = self.int_code[self.opcode + 3]
                if param_1 < param_2:
                    self.int_code[param_3] = 1
                else:
                    self.int_code[param_3] = 0
                self.opcode += 4
            # equals
            elif opcode_instruction == '8':
                param_1 = self.int_code[self.int_code[self.opcode + 1]
                                        ] if instruction[2] == '0' else self.int_code[self.opcode + 1]
                param_2 = self.int_code[self.int_code[self.opcode + 2]
                                        ] if instruction[1] == '0' else self.int_code[self.opcode + 2]
                param_3 = self.int_code[self.opcode + 3]
                if param_1 == param_2:
                    self.int_code[param_3] = 1
                else:
                    self.int_code[param_3] = 0
                self.opcode += 4


def day5_2():
    values = list(itertools.permutations([9, 8, 7, 6, 5], 5))
    count = 0
    highest_value = 0
    for v in values:
        amps = [IntCode(f.copy(), v[x]) for x in range(5)]
        prev_output = amps[0].iterate(0)
        idx = 1
        keep_going = True
        counter = 0
        while keep_going:
            counter += 1
            prev_output = amps[idx].iterate(prev_output)
            if idx == 4:
                idx = 0
            else:
                idx += 1
            if amps[idx].done:
                keep_going = False
        print(counter)
        if highest_value < prev_output:
            highest_value = prev_output
    print(highest_value)


# day5_1()
day5_2()
