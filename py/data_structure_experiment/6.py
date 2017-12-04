import copy


print("Ex6 Graph")


class Temp:
    pass


class UFlag:
    pass


class Database:
    pass


class Graph:
    class UFlag:
        class Temp:
            pass

    def __init__(self, nodes: list, edges: list):
        self.node = nodes
        self.edge = edges
        """
        edge table:
        row - source
        column - target
        """

    def print_edges(self):
        for i in range(len(self.edge)):
            print(self.edge[i])

    def print_edge_table(self):
        for i in range(len(self.edge)):
            print(str(self.node[i]), end="")
            self.UFlag.curr_node = i
            Temp._continue = True
            self.UFlag.Temp.visited = [False] * len(self.node)
            self.UFlag.Temp.visited[i] = True
            while Temp._continue:
                Temp._continue = False
                for j in range(len(self.edge[self.UFlag.curr_node])):
                    if self.UFlag.curr_node != j and self.edge[self.UFlag.curr_node][j] >= 1 \
                            and self.UFlag.Temp.visited[j] is False:
                        print("->" + str(self.node[j]), end="")
                        self.UFlag.Temp.visited[j] = True
                        self.UFlag.curr_node = j
                        Temp._continue = True
                        break
            print()

    def dfs_legacy(self):
        def dfs_core(edges, solution_set, visited, way):
            visited[way[-1]] = True
            found = 0
            for x in range(len(edges[way[-1]])):
                if visited[x] is False and edges[way[-1]][x] >= 1 and way[-1] != x:
                    dfs_core(edges, solution_set, copy.deepcopy(visited), copy.deepcopy(way) + [x])
                    found += 1
            if found is 0:
                solution_set += [way]

        self.UFlag.Temp.solution = []
        for i in range(len(self.node)):
            self.UFlag.Temp.visited = [False] * len(self.node)
            dfs_core(self.edge, self.UFlag.Temp.solution, self.UFlag.Temp.visited, [i])

        for i in range(len(self.UFlag.Temp.solution)):
            print(self.UFlag.Temp.solution[i])


Temp.nodes = [
    0, 1, 2, 3, 4, 5
]
Temp.edges = [
    [0, 5, 0, 7, 0, 0],
    [0, 0, 4, 0, 0, 0],
    [8, 0, 0, 0, 0, 9],
    [0, 0, 5, 0, 0, 6],
    [0, 0, 0, 5, 0, 0],
    [3, 0, 0, 0, 1, 0]
]
Database.graph1 = Graph(Temp.nodes, Temp.edges)
print("Matrix:")
Database.graph1.print_edges()
print("Links:")
Database.graph1.print_edge_table()
print("dfs:")
Database.graph1.dfs_legacy()
