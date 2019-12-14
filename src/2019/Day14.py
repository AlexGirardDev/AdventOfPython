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
print(ores)


def calc_ore_cost(ore):
    if ore.name == "ORE":
        return ore.output
    total = 0 
    for x in ore.requriments:
        required_ore = ores[x[0]]
        requried_ammount  = ores[1]
        
    return total


counter = 0
print(counter)
print(calc_ore_cost(ores["FUEL"]))
