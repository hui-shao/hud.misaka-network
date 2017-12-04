print("Ex6 Graph")


class UFlag:
    class Temp:
        pass


class Database:
    class Temp:
        pass


class Graph:
    class UFlag:
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
            print("Node " + str(i) + ":")
            print(str(self.node[i]), end="")
            self.UFlag.currNode = i
            while UFlag.Temp._continue:
                UFlag.Temp._continue = False
                for j in range(len(self.edge[self.UFlag.currNode])):
                    if self.UFlag.currNode != j and self.edge[self.UFlag.currNode][j] >= 1:
                        print("->" + str(self.node[j]), end="")
                        self.UFlag.currNode = j
                        UFlag.Temp._continue = True
                        break


Database.Temp.nodes = [
    0, 1, 2, 3, 4, 5
]
Database.Temp.edges = [
    [0, 5, 0, 7, 0, 0],
    [0, 0, 4, 0, 0, 0],
    [8, 0, 0, 0, 0, 9],
    [0, 0, 5, 0, 0, 6],
    [0, 0, 0, 5, 0, 0],
    [3, 0, 0, 0, 1, 0]
]
Database.Temp.graph1 = Graph(Database.Temp.nodes, Database.Temp.edges)
Database.Temp.graph1.print_edge_table()
