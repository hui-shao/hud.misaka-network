import random

print("Ex 3-1 DFS")
# Target: Search for maximum value in this image && print progress.

# Generate test data
repo = [x for x in range(0, 20)]
random.shuffle(repo)

# 0 = valid, 1 = invalid, 5 = default
net = [[5] * 20 for x in range(0, 20)]

for i in range(0, 20):
    for j in range(i + 1, 20):
        net[i][j] = random.randint(0, 1)

visited = [0] * 20

sto = -1 # store maximum value in this image.

def dfs(repo, net, visited):
    somecode = 1
    # TODO: complete this function

print("Ex 3-4 100 item with 100 coin")

for a in range(0, 20):
    for b in range(0, 33):
        if a * 5 + b * 3 + (100 - a - b) == 100:
            print("a=" + str(a) + ", b=" + str(b) + ", c=" + str(100 - a - b))
