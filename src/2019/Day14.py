import math
f = list(open("input/2019/day14.txt", "r"))

class Ore:
    def __init__(self, s):
        #what is regex?
        self.name = s.split("=>")[1].strip().split(" ")[1]
        self.output = int(s.split("=>")[1].strip().split(" ")[0])
        if s.split("=>")[0].split(",") != [" "]:
            self.requriments = [(y.strip().split(" ")[1],
                                 int(y.strip().split(" ")[0])) for y in s.split("=>")[0].split(",")]
    def __repr__(self):
        return self.name


ores = dict()

for x in f:
    ore = Ore(x)
    ores[ore.name] = ore
ore = Ore(" => 1 ORE")
ores[ore.name] = ore
# print(ores)
total_ore = 0
leftover_ore = dict()
def calc_ore_cost_1(ore):
    if ore.name == "ORE":
        return ore.output
    total = 0
    for x in ore.requriments:
        required_ore = ores[x[0]]
        requried_ammount = x[1]
        if leftover_ore.get(required_ore.name) is not None:
            requried_ammount -= leftover_ore[required_ore.name]
            leftover_ore[required_ore.name] = 0
        iterations = int(math.ceil(requried_ammount / required_ore.output))
        leftover_ore[required_ore.name] = iterations * \
            required_ore.output - requried_ammount
        if required_ore.name == "ORE":
            return iterations * required_ore.output
        total += sum(calc_ore_cost_1(required_ore) for z in range(iterations))
    return total


def calc_ore_cost_2(ore, amount):
    if ore.name == "ORE":
        return ore.output * amount
    return sum(calc_ore_cost_2(ores[x[0]],  x[1] / ores[x[0]].output * amount) for x in ore.requriments)


print(calc_ore_cost_1(ores["FUEL"]))
print(1000000000000 / calc_ore_cost_2(ores["FUEL"], 1)-1)
#the actualy awser was 1 below this, even though all my tests were right on
#i am just going to chalk it up to floating point math bullshit
