import math
f = list(open("input/2019/day14.txt", "r"))


class Ore:
    def __init__(self, s):
        self.name = s.split("=>")[1].strip().split(" ")[1]
        self.output = int(s.split("=>")[1].strip().split(" ")[0])
        if s.split("=>")[0].split(",") != [" "]:
            self.requriments = [(y.strip().split(" ")[1],
                                 int(y.strip().split(" ")[0])) for y in s.split("=>")[0].split(",")]

    def __hash__(self):
        return hash(self.name)

    def __eq__(self, other):
        return self.name == other.name

    def __repr__(self):
        return self.name


ores = dict()

for x in f:
    ore = Ore(x)
    ores[ore.name] = ore
ore = Ore(" => 1 ORE")
ores[ore.name] = ore
#print(ores)

total_ore = 0
leftover_ore = dict()
def calc_ore_cost(ore):
    if ore.name == "ORE":
        total_ore =  ore.output
        return ore.output
    total = 0 
    for x in ore.requriments:
        required_ore = ores[x[0]]
        requried_ammount = x[1] 
        if leftover_ore.get(required_ore.name) is not None:
            requried_ammount -= leftover_ore[required_ore.name]
            leftover_ore[required_ore.name] = 0

        iterations = int(math.ceil(requried_ammount / required_ore.output))
        if required_ore.name == "ORE":
            return iterations * required_ore.output
        leftover_ore[required_ore.name] = iterations * required_ore.output - requried_ammount
        for z in range(iterations):
            total += calc_ore_cost(required_ore)
        
    return total



#print(counter)
fuel = 1000000000000
counter = 0
print(calc_ore_cost(ores["FUEL"]))
print(calc_ore_cost(ores["FUEL"]))
print(calc_ore_cost(ores["FUEL"]))
print(calc_ore_cost(ores["FUEL"]))
print(calc_ore_cost(ores["FUEL"]))
#return

# while (fuel > 0):
#     print(fuel)
#     fuel -= calc_ore_cost(ores["FUEL"])
#     counter += 1
# print(counter) 
