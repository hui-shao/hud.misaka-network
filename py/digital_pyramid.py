print("Integer required:")
n = int(input())

for i in range(1, n + 1):
    padding = " " * (i - 1)
    print(padding + str(i % 10) * ((n + 1 - i) * 2 - 1) + padding)
