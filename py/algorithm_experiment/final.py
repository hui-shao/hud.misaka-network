import random

print("Ex 8 Maximum summary of sub-array")

SCALE_OF_DATA = 200

sto = [0] * SCALE_OF_DATA
negative_counter = 0
for i in range(0, len(sto)):
    value = random.randint(random.randint(-SCALE_OF_DATA, 0), random.randint(0, int(SCALE_OF_DATA/2)))
    sto[i] = value
    if value < 0:
        negative_counter += 1

print("***************** Data-set *****************")
for i in range(0, len(sto), 10):
    print(sto[i:i+10])

print("Generated an array with", SCALE_OF_DATA - negative_counter, "positive integer(including zero) and",
      negative_counter, "negative integer.")

best_solution = []
best_solution_sum = 0

for i in range(0, len(sto)):
    for j in range(i, len(sto)):
        curr_value = 0
        for k in range(i, j + 1):
            curr_value += sto[k]
        if curr_value > best_solution_sum:
            best_solution_sum = curr_value
            best_solution = sto[i:j]

print("Solution: the following array is the best sub-array for the current problem with largest summary value:",
      best_solution_sum)
print(best_solution)
