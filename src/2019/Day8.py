from itertools import chain
f = [int(char) for char in [x for x in open("input/2019/day8.txt", "r")][0]]
#f = [int(char) for char in '0222112222120000']


def day8_1():
    image_width = 25
    image_hieght = 6

    def generate_image():
        return [[None for y in range(image_width)] for x in range(image_hieght)]
    image = [generate_image()]
    layer = 0
    x = 0
    y = 0
    for c in f:
        image[layer][y][x] = c
        if x >= image_width - 1:
            x = 0
            y += 1
        else:
            x += 1
        if y >= image_hieght:
            y = 0
            x = 0
            layer += 1
            image.append(generate_image())
    if x == 0 and y == 0:
        image.pop()

    for i in image:
        for x in i:
            out = ""
            for y in x:
                out += str(y)
            #print(out)
        #print("========")
    lowest_index = 0
    lowest_count = 9999999999999
    for x in range(len(image)):
        # print(list(chain.from_iterable(image[0])))
        count = count_numbers(image[x], 0)
        # print(count)
        if count < lowest_count:
            lowest_count = count
            lowest_index = x
    one_digits = count_numbers(image[lowest_index], 1)
    two_digits = count_numbers(image[lowest_index], 2)
    print(one_digits * two_digits)


def count_numbers(arg, i):
    count = 0
    for x in arg:
        for y in x:
            if y == i:
                count += 1
    return count


def day8_2():
    image_width = 25
    image_hieght = 6

    def generate_image():
        return [[None for y in range(image_width)] for x in range(image_hieght)]
    image = [generate_image()]
    layer = 0
    x = 0
    y = 0
    for c in f:
        image[layer][y][x] = c
        if x >= image_width - 1:
            x = 0
            y += 1
        else:
            x += 1
        if y >= image_hieght:
            y = 0
            x = 0
            layer += 1
            image.append(generate_image())
    if x == 0 and y == 0:
        image.pop()

    output = generate_image()
    for x in range(len(output)):
        for y in range(len(output[x])):
            output[x][y] = get_pixel(image, x, y)

    for x in output:
        out = ""
        for y in x:
            out += str(y)
        print(out)
    print("========")


def get_pixel(arg, x, y):
    for i in arg:
        if i[x][y] == 0:
            return " "
        elif i[x][y] == 1:
            return "X"


day8_1()
day8_2()
