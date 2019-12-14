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
    if ore == "ORE":
        return 1
    total = 0
    ore1 = ores[ore]
    for x in ores[ore].requriments:

        requirment = ores[x[0]]
        produces = requirment.output
        requires = 0
        if (x[1] <= produces):
            requires = 1
        else:
            requires = x[1] // produces
        if x[0] == "ORE":
            total += requirment.output
        elif x[1] != 0:
            for _ in range(requires):
                total += calc_ore_cost(x[0])
    return total


counter = 0
print(counter)
print(calc_ore_cost("FUEL"))
