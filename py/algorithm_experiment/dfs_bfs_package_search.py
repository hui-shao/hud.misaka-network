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


print("Ex 3-3 DFS searching 0-1 package problem")
# Hey, we got a hatchling destroyer and some shield equipment here.
# Different equipment needs different power and give different shield.
# We only have fixed power so we must find a way to give her the most shield.

# Generate data
power = [x for x in range(0, SCALE_OF_DATA)]
shield = [x for x in range(0, SCALE_OF_DATA)]
random.shuffle(power)
random.shuffle(shield)
maximum_power = random.randint(0, SCALE_OF_DATA * 2)


solution = [0,          0,         []]
#          [shield_sum, power_sum, [method of pick up]]


def package_dfs():
    package_dfs_explore(0, solution)

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
        ID = Misaka_0x447f hatchling destroyer's pick method
        SHIELD = """ + str(solution[0] + 1) + " / " + str(solution[0] + 1) + """ kRes.  100%
                 """ + progress_bar(100, 100, 50) + """
        POWER LOAD = """ + str(solution[1]) + " / " + str(maximum_power) + """ MW  """ + str(int(solution[1] / maximum_power * 100)) + """%
                 """ + progress_bar(solution[1], maximum_power, 50) + """
        *** EQUIPMENT LIST ***
        """ + str(solution[2]) + """
        -----------------------------------------------------------
    """)


def package_dfs_explore(location, prev_solution):
    global solution
    if prev_solution[1] >= maximum_power or location > SCALE_OF_DATA - 1:
        return False
    if prev_solution[0] > solution[0]:
        solution = prev_solution
    # in case of pick this...
    pick_this = copy.deepcopy(prev_solution)
    pick_this[0] += shield[location]
    pick_this[1] += power[location]
    pick_this[2] += [location]
    package_dfs_explore(location + 1, pick_this)
    # in case of not pick this...
    not_pick_this = copy.deepcopy(prev_solution)
    package_dfs_explore(location + 1, not_pick_this)


package_dfs()


print("Ex 3-4 100 item with 100 coin")


for a in range(0, 20):
    for b in range(0, 33):
        if a * 5 + b * 3 + (100 - a - b) == 100:
            print("a=" + str(a) + ", b=" + str(b) + ", c=" + str(100 - a - b))
