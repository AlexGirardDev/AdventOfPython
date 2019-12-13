
class Computer():
    def __init__(self, input, phase,extra_memory = 0):
        self.input = input + [0] * extra_memory
        self.phase = phase
        self.done = False
        self.first_input = False
        self.opcode = 0
        self.last_output = 0
        self.relative_index = 0

    def iterate(self, input):
        output = 0

        def get_param_1():
            if instruction[2] == '0':
                return self.input[self.input[self.opcode + 1]]
            if instruction[2] == '1':
                return self.input[self.opcode + 1]
            elif instruction[2] == '2':
                return self.input[self.input[self.opcode + 1] + self.relative_index]
            else:
                print("ERROR")

        def get_param_2():
            if instruction[1] == '0':
                return self.input[self.input[self.opcode + 2]]
            if instruction[1] == '1':
                return self.input[self.opcode + 2]
            elif instruction[1] == '2':
                return self.input[self.input[self.opcode + 2] + self.relative_index]
            else:
                print("ERROR")

        def get_param_3():
            if instruction[0] == '0':
                return self.input[self.opcode + 3]
            if instruction[0] == '1':
                return self.input[self.opcode + 3]
            elif instruction[0] == '2':
                return self.input[self.opcode + 3] + self.relative_index
            else:
                print("ERROR")
        while True:
            instruction = ("00000" + str(self.input[self.opcode]))[-5:]
            opcode_instruction = instruction[-1:]
            if instruction[-2:] == '99':
                self.done = True
                return None
                # print("!!!HALT!!!")
                self.done = True
            # print(f"{self.input[opcode]}-{self.input[opcode+1]}-{self.input[opcode+2]}-{self.input[opcode+3]}")
            # Input
            elif opcode_instruction == '3':
                # print('input')
                self.input[get_param_3()] = self.phase
                self.opcode += 2
            # output
            elif opcode_instruction == '4':
                param_1 = get_param_1()
                output = param_1
                # print(output)
                self.opcode += 2
                self.last_output = output
                return output
            # add
            elif opcode_instruction == '1':
                param_1 = get_param_1()
                param_2 = get_param_2()
                param_3 = get_param_3()
                self.input[param_3] = param_1 + param_2
                self.opcode += 4
            # Mult
            elif opcode_instruction == '2':
                param_1 = get_param_1()
                param_2 = get_param_2()
                param_3 = get_param_3()
                self.input[param_3] = param_1 * param_2
                self.opcode += 4
            # Jump if true
            elif opcode_instruction == '5':
                param_1 = get_param_1()
                param_2 = get_param_2()
                if param_1 != 0:
                    self.opcode = param_2
                else:
                    self.opcode += 3
            # Jump if False
            elif opcode_instruction == '6':
                param_1 = get_param_1()
                param_2 = get_param_2()
                if param_1 == 0:
                    self.opcode = param_2
                else:
                    self.opcode += 3
            # Less Than
            elif opcode_instruction == '7':
                param_1 = get_param_1()
                param_2 = get_param_2()
                param_3 = get_param_3()
                if param_1 < param_2:
                    self.input[param_3] = 1
                else:
                    self.input[param_3] = 0
                self.opcode += 4
            # equals
            elif opcode_instruction == '8':
                param_1 = get_param_1()
                param_2 = get_param_2()
                param_3 = get_param_3()
                if param_1 == param_2:
                    self.input[param_3] = 1
                else:
                    self.input[param_3] = 0
                self.opcode += 4
            elif opcode_instruction == '9':
                param1 = get_param_1()
                self.relative_index += param1
                self.opcode += 2
            else:
                print("ERROR")

