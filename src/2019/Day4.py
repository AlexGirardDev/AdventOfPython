def day4_1():
    counter = 0
    for x in range(353096, 843212):
        if (check_password_1(str(x))):
            counter += 1
    print(counter)


def check_password_1(x):
    num_len = len(x)
    double_done = False
    for y in range(num_len):
        if y < num_len - 1 and x[y + 1] == x[y]:
            double_done = True
        if (y < num_len - 1 and x[y] > x[y + 1]):
            return False
    return double_done


def day4_2():
    counter = 0
    for x in range(353096, 843212):
        if (check_password_2(str(x))):
            counter += 1
    print(counter)


def check_password_2(x):
    num_len = len(x)
    double_done = False
    for y in range(num_len):
        #I hate this but when i was doing it fast having these 3 split up made it easier to write
        if y < num_len - 1 and x[y + 1] == x[y]:
            if (y == 0 or x[y - 1] != x[y]):
                if (y >= num_len - 2 or x[y + 2] != x[y]):
                    double_done = True

        if (y < num_len - 1 and x[y] > x[y + 1]):
            return False
    return double_done


day4_1()
day4_2()
