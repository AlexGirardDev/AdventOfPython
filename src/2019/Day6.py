f = [[x.split(')')[0], x.split(')')[1].replace("\n", "")]
     for x in open("input/2019/day6.txt", "r")]


class Graph:
    def __init__(self):
        self.adj_list = {}

    def add_vertex(self, value):
        if not self.adj_list.get(value):
            self.adj_list[value] = []

    # todo don't add duplicates
    def add_edge(self, v1, v2):
        if self.adj_list.get(v1) is None or self.adj_list.get(v1) is None:
            return
        self.adj_list[v1].append(v2)
        # self.adj_list[v2].append(v1)

    def remove_edge(self, v1, v2):
        if self.adj_list.get(v1) is None or self.adj_list.get(v1) is None:
            return
        self.adj_list[v1].remove(v2)
        self.adj_list[v2].remove(v1)

    def remov_vertex(self, vertex):
        self.adj_list.pop(vertex)
        for x in self.adj_list.items():
            x[1].remove(vertex)

    def depth_first_traversal(self):
        visited = []
        result = []
        # for x in self.adj_list.values():
        #     list.sort(x, reverse=True)

        def recursion(vertex):
            if vertex is None:
                return
            visited.append(vertex)
            result.append(vertex)
            for x in sorted(self.adj_list[vertex]):
                if x not in visited:
                    recursion(x)

        recursion(min(self.adj_list.keys()))
        return result

    def depth_first_traversal_2(self):
        stack = []
        stack.append(min(self.adj_list.keys()))
        discovered = []
        result = []
        while stack:
            vertex = stack.pop()
            if vertex not in discovered:
                result.append(vertex)
                discovered.append(vertex)
                stack = stack + \
                    [x for x in self.adj_list[vertex] if x not in discovered]
        return result

    def breadth_first_traversal(self):
        que = []
        discovered = []
        result = []
        count = 0
        que.append(min(self.adj_list.keys()))
        # discovered.append(min(self.adj_list.keys()))
        while que:
            vertex = que.pop(0)
            count += 1
            if vertex not in discovered:
                result.append(vertex)
                discovered.append(vertex)
                que = que + \
                    [x for x in self.adj_list[vertex] if x not in discovered]
        print(count)
        return result


class Node():
    def __init__(self, value):
        self.children = []
        self.value = value

    def __repr__(self):
        return self.value


def day5_1():
    parent = Node("COM")

    def recur(n):
        #print( 'wow')
        for y in [x for x in f if x[0] == n.value]:
            n.children.append(Node(y[1]))
        for x in n.children:
            recur(x)
    recur(parent)
    print(parent.children)

    def recur2(n, dep):
        dep += 1
        count = 0
        for x in n.children:
            count += recur2(x, dep)
        return count + dep

    print(recur2(parent, 0)-len(f))
# print(count)


def day5_2():
    parent = Node("COM")

    def recur(n):
        #print( 'wow')
        wow = [n]
        for y in [x for x in f if x[0] == n.value]:
            n.children.append(Node(y[1]))
        for x in n.children:
            wow = wow + recur(x)
        return wow
    all_nodes = recur(parent)
    print(all_nodes)
    # print(parent.children)

    def recur2(n, dep):
        dep += 1
        count = 0
        for x in n.children:
            count += recur2(x, dep)
        return count + dep

    def get_me(n, dep):
        if (n.value == 'YOU'):
            return dep
        for x in n.children:
            xd = get_me(x, dep+1)
            if xd:
                return xd
        return None

    def get_san(n, dep):
        if (n.value == 'SAN'):
            return dep
        for x in n.children:
            xd = get_san(x, dep+1)
            if xd:
                return xd
        return None
    lowest_distance = 99999999999999
    for x in all_nodes:
        me = get_me(x, 0)
        san = get_san(x, 0)
        if me is not None and san is not None and me + san < lowest_distance:
            lowest_distance = me + san
    print(lowest_distance)
    #print(recur2(parent, 0)-len(f))


# day5_1()
day5_2()
