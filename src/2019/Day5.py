f = [int(x) for x in '3,225,1,225,6,6,1100,1,238,225,104,0,1101,82,10,225,101,94,44,224,101,-165,224,224,4,224,1002,223,8,223,101,3,224,224,1,224,223,223,1102,35,77,225,1102,28,71,225,1102,16,36,225,102,51,196,224,101,-3468,224,224,4,224,102,8,223,223,1001,224,7,224,1,223,224,223,1001,48,21,224,101,-57,224,224,4,224,1002,223,8,223,101,6,224,224,1,223,224,223,2,188,40,224,1001,224,-5390,224,4,224,1002,223,8,223,101,2,224,224,1,224,223,223,1101,9,32,224,101,-41,224,224,4,224,1002,223,8,223,1001,224,2,224,1,223,224,223,1102,66,70,225,1002,191,28,224,101,-868,224,224,4,224,102,8,223,223,101,5,224,224,1,224,223,223,1,14,140,224,101,-80,224,224,4,224,1002,223,8,223,101,2,224,224,1,224,223,223,1102,79,70,225,1101,31,65,225,1101,11,68,225,1102,20,32,224,101,-640,224,224,4,224,1002,223,8,223,1001,224,5,224,1,224,223,223,4,223,99,0,0,0,677,0,0,0,0,0,0,0,0,0,0,0,1105,0,99999,1105,227,247,1105,1,99999,1005,227,99999,1005,0,256,1105,1,99999,1106,227,99999,1106,0,265,1105,1,99999,1006,0,99999,1006,227,274,1105,1,99999,1105,1,280,1105,1,99999,1,225,225,225,1101,294,0,0,105,1,0,1105,1,99999,1106,0,300,1105,1,99999,1,225,225,225,1101,314,0,0,106,0,0,1105,1,99999,8,226,226,224,1002,223,2,223,1006,224,329,101,1,223,223,1008,677,677,224,102,2,223,223,1006,224,344,101,1,223,223,1107,226,677,224,102,2,223,223,1005,224,359,101,1,223,223,1008,226,226,224,1002,223,2,223,1006,224,374,1001,223,1,223,1108,677,226,224,1002,223,2,223,1006,224,389,1001,223,1,223,7,677,226,224,1002,223,2,223,1006,224,404,101,1,223,223,7,226,226,224,1002,223,2,223,1005,224,419,101,1,223,223,8,226,677,224,1002,223,2,223,1006,224,434,1001,223,1,223,7,226,677,224,1002,223,2,223,1006,224,449,1001,223,1,223,107,226,677,224,1002,223,2,223,1005,224,464,1001,223,1,223,1007,677,677,224,102,2,223,223,1005,224,479,101,1,223,223,1007,226,226,224,102,2,223,223,1005,224,494,1001,223,1,223,1108,226,677,224,102,2,223,223,1005,224,509,101,1,223,223,1008,677,226,224,102,2,223,223,1005,224,524,1001,223,1,223,1007,677,226,224,102,2,223,223,1005,224,539,101,1,223,223,1108,226,226,224,1002,223,2,223,1005,224,554,101,1,223,223,108,226,226,224,102,2,223,223,1005,224,569,101,1,223,223,108,677,677,224,102,2,223,223,1005,224,584,101,1,223,223,1107,226,226,224,1002,223,2,223,1006,224,599,101,1,223,223,8,677,226,224,1002,223,2,223,1006,224,614,1001,223,1,223,108,677,226,224,102,2,223,223,1006,224,629,1001,223,1,223,1107,677,226,224,1002,223,2,223,1006,224,644,1001,223,1,223,107,677,677,224,102,2,223,223,1005,224,659,101,1,223,223,107,226,226,224,102,2,223,223,1006,224,674,1001,223,1,223,4,223,99,226'.split(',')]
# f = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
#      1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
#      999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]
#f=[3,3,1105,-1,9,1101,0,0,12,4,12,99,1]


def day5_1():
    opcode = 0
    input = 5
    while True:
        instruction = ("00000" + str(f[opcode]))[-5:]
        opcode_instruction = instruction[-1:]
        if instruction[-2:] == '99':
            print("!!!HALT!!!")
            return
        #print(f"{f[opcode]}-{f[opcode+1]}-{f[opcode+2]}-{f[opcode+3]}")
        # Input
        if opcode_instruction == '3':
            f[f[opcode + 1]] = input("prompt")
            opcode += 2
        # output
        elif opcode_instruction == '4':
            param_1 = f[f[opcode + 1]
                        ] if instruction[2] == '0' else f[opcode + 1]
            print(param_1)
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


def day5_2():
    pass


day5_1()
day5_2()
