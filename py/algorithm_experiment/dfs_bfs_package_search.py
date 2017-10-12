import random
import copy

print("Ex 3-1 DFS")
# Target: Search for the most easy way from random origin to random destination.
SCALE_OF_DATA = 20

# Generate test data
origin = random.randint(0, SCALE_OF_DATA - 1)
destination = random.randint(0, SCALE_OF_DATA - 1)

repo = [x for x in range(0, SCALE_OF_DATA)]
random.shuffle(repo)

# 0 = link down, 1 = link up, 5 = default
net = [[5] * SCALE_OF_DATA for x in range(0, SCALE_OF_DATA)]

for i in range(0, SCALE_OF_DATA):
    for j in range(i + 1, SCALE_OF_DATA):
        net[i][j] = random.randint(0, 1)

visited = [0] * SCALE_OF_DATA


def search(method):
    print("Auto pilot start")
    print("You are on:", origin)
    print("Destination:", destination)
    path = []
    if method == "dfs":
        path = dfs_explore(origin, path)
    elif method == "bfs":
        path = bfs_explore()
    else:
        return False

    if path is False:
        print("Auto pilot stop: navigation mark was not reachable")
        return False

    print(path)
    print("Auto pilot stop: navigation mark was arrived")
    return True


def dfs_explore(location, prev_path):
    visited[location] = 1
    path = copy.deepcopy(prev_path) + [location]
    if location == destination:
        return path
    for i in range(0, SCALE_OF_DATA):
        if net[i][location] == 1 and visited[i] == 0:
            return dfs_explore(i, path)
        if net[location][i] == 1 and visited[i] == 0:
            return dfs_explore(i, path)
    return False


search("dfs")

print("Ex 3-2 BFS")

# Generate part located in DFS part
del visited
visited = [0] * SCALE_OF_DATA

tasks = [[origin]]


def bfs_explore():
    global tasks
    while True:
        if len(tasks) > 0:
            for i in tasks:
                if i[-1] == destination:
                    return i
                else:
                    # in case of not reached, search for next step
                    for j in range(0, SCALE_OF_DATA):
                        if net[j][i[-1]] == 1 and visited[j] == 0:
                            new_task = copy.deepcopy(i)
                            new_task += [j]
                            tasks += [new_task]
                        if net[i[-1]][j] == 1 and visited[j] == 0:
                            new_task = copy.deepcopy(i)
                            new_task += [j]
                            tasks += [new_task]
        else:
            return False


search("bfs")

print("Ex 3-4 100 item with 100 coin")

for a in range(0, 20):
    for b in range(0, 33):
        if a * 5 + b * 3 + (100 - a - b) == 100:
            print("a=" + str(a) + ", b=" + str(b) + ", c=" + str(100 - a - b))
