import random
import math
import queue
from operator import attrgetter
from collections import namedtuple

SCALE_OF_DATA = 40

print("Ex 5-1 Solving package problem with greedy method")


# Hey, we got a "rage" and some armor equipment here.
# Different equipment needs different power and give different armor.
# We only have fixed power so we must find a way to give her the most armor.
# We have no time yet. Equipment must be completed as soon as possible

# Generate data
class Equipment:
    def __init__(self, power, armor):
        self.power = power
        self.armor = armor
        self.id = id(self) % 10000

        if power == 0:
            self.ratio = math.inf
        else:
            self.ratio = armor / power


sto = []
for i in range(0, 20):
    sto += [Equipment(random.randint(0, SCALE_OF_DATA), random.randint(0, SCALE_OF_DATA))]

maximum_power = random.randint(0, SCALE_OF_DATA * 3)

# Sort data
sto = sorted(sto, key=attrgetter("ratio"))
sto.reverse()

solution = {
    "value_sum": 0,
    "power_sum": 0,
    "list": []
}
while True:
    if solution["power_sum"] + sto[0].power <= maximum_power:
        solution["value_sum"] += sto[0].armor
        solution["power_sum"] += sto[0].power
        solution["list"] += [sto[0].id]
        del sto[0]
    else:
        break


def progress_bar(value, max_value, width):
    value = int(value)
    max_value = int(max_value)
    width = int(width)
    bar = "-" * width
    bar_fill_width = int(value / max_value * width)
    bar = "#" * bar_fill_width + bar[bar_fill_width:]
    return bar


print("""
    EQUIPMENT PICK METHOD -------------------------------------
    ID = Misaka_0x447f's "rage" pick method
    ARMOR = """ + str(solution["value_sum"] + 1) + " / " + str(solution["value_sum"] + 1) + """ kN  100%
             """ + progress_bar(100, 100, 50) + """
    POWER LOAD = """ + str(solution["power_sum"]) + " / " + str(maximum_power) + """ MW  """ + str(
    int(solution["power_sum"] / maximum_power * 100)) + """%
             """ + progress_bar(solution["power_sum"], maximum_power, 50) + """
    *** EQUIPMENT LIST ***
    """ + str(solution["list"]) + """
    -----------------------------------------------------------
""")

print("Ex 5-2 Greedy solving MST")

parent = dict()
rank = dict()


def make_set(node):
    parent[node] = node
    rank[node] = 0


def find(node):
    if parent[node] != node:
        parent[node] = find(parent[node])
    return parent[node]


def union(node1, node2):
    root1 = find(node1)
    root2 = find(node2)
    if root1 != root2:
        if rank[root1] > rank[root2]:
            parent[root2] = root1
        else:
            parent[root1] = root2
            if rank[root1] == rank[root2]:
                rank[root2] += 1


def mst(net):
    for node in net["node"]:
        make_set(node)

    minimum_spanning_tree = set()
    edges = list(net['cable'])
    edges.sort()
    for edge in edges:
        weight, node1, node2 = edge
        if find(node1) != find(node2):
            union(node1, node2)
            minimum_spanning_tree.add(edge)
    return minimum_spanning_tree


net = {
    'node': ['A', 'B', 'C', 'D', 'E', 'F'],
    'cable': {(1, 'A', 'B'), (5, 'A', 'C'), (3, 'A', 'D'), (4, 'B', 'C'), (2, 'B', 'D'), (1, 'C', 'D')}
}
minimum_spanning_tree = {(1, 'A', 'B'), (2, 'B', 'D'), (1, 'C', 'D')}
result = mst(net)
assert result == minimum_spanning_tree

print(result)

print("Ex 5-3 Greedy solving dijkstr")

Edge = namedtuple('Edge', ['vertex', 'weight'])


class GraphUndirectedWeighted(object):
    def __init__(self, vertex_count):
        self.vertex_count = vertex_count
        self.adjacency_list = [[] for _ in range(vertex_count)]

    def add_edge(self, source, dest, weight):
        assert source < self.vertex_count
        assert dest < self.vertex_count
        self.adjacency_list[source].append(Edge(dest, weight))
        self.adjacency_list[dest].append(Edge(source, weight))

    def get_edge(self, vertex):
        for e in self.adjacency_list[vertex]:
            yield e

    def get_vertex(self):
        for v in range(self.vertex_count):
            yield v


def dijkstra(graph, source, dest):
    q = queue.PriorityQueue()
    parents = []
    distances = []
    start_weight = float("inf")

    for i in graph.get_vertex():
        weight = start_weight
        if source == i:
            weight = 0
        distances.append(weight)
        parents.append(None)

    q.put(([0, source]))

    while not q.empty():
        v_tuple = q.get()
        v = v_tuple[1]

        for e in graph.get_edge(v):
            candidate_distance = distances[v] + e.weight
            if distances[e.vertex] > candidate_distance:
                distances[e.vertex] = candidate_distance
                parents[e.vertex] = v
                # primitive but effective negative cycle detection
                if candidate_distance < -1000:
                    raise Exception("Negative cycle detected")
                q.put(([distances[e.vertex], e.vertex]))

    shortest_path = []
    end = dest
    while end is not None:
        shortest_path.append(end)
        end = parents[end]

    shortest_path.reverse()

    return shortest_path, distances[dest]


def main():
    g = GraphUndirectedWeighted(9)
    g.add_edge(0, 1, 4)
    g.add_edge(1, 7, 6)
    g.add_edge(1, 2, 1)
    g.add_edge(2, 3, 3)
    g.add_edge(3, 7, 1)
    g.add_edge(3, 4, 2)
    g.add_edge(3, 5, 1)
    g.add_edge(4, 5, 1)
    g.add_edge(5, 6, 1)
    g.add_edge(6, 7, 2)
    g.add_edge(6, 8, 2)
    g.add_edge(7, 8, 2)
    # for testing negative cycles
    # g.add_edge(1, 9, -5)
    # g.add_edge(9, 7, -4)

    # test points
    shortest_path, distance = dijkstra(g, 0, 1)
    assert shortest_path == [0, 1] and distance == 4

    shortest_path, distance = dijkstra(g, 0, 8)
    assert shortest_path == [0, 1, 2, 3, 7, 8] and distance == 11

    shortest_path, distance = dijkstra(g, 5, 0)
    assert shortest_path == [5, 3, 2, 1, 0] and distance == 9

    shortest_path, distance = dijkstra(g, 1, 1)
    assert shortest_path == [1] and distance == 0

main()

