f = [x for x in open("input/2.txt", "r")]



def part1():
    totalCount = 0
    for x in f:
        min = int(x.split("-")[0])
        max = int(x.split("-")[1].split()[0])
        letter = x.split()[1].split(":")[0]
        password = x.split()[2]
        count = 0
        for y in password:
            # print(y + letter)
            if y == letter:
                count+= 1
        if count>= min and count <=max:
            totalCount+= 1
    print(totalCount)

def part2():
    totalCount = 0
    for x in f:
        min = int(x.split("-")[0])-1
        max = int(x.split("-")[1].split()[0])-1
        letter = x.split()[1].split(":")[0]
        password = x.split()[2]
        count = 0
        for y in range(len(password)):
            # print(str(min)+ "-" +str(max) +"-" + str(y) +"-"+str(password[y]) +"-"+str(letter))
            if (min == y or max == y) and password[y] == letter:
                count+= 1
        if count==1:
            totalCount+= 1
    print(totalCount)

part1()
part2()
