import random

print("Ex 2-1-1 quick sort")


def qs(repo, left, right):
    if right > left:
        pin = int((left + right) / 2)
        pin = partition(repo, left, right, pin)
        qs(repo, left, pin - 1)
        qs(repo, pin + 1, right)


def partition(repo, left, right, pin):
    pinned_value = repo[pin]
    repo[pin], repo[right] = repo[right], repo[pin]
    for i in range(left, right):
        if repo[i] <= pinned_value:
            repo[left], repo[i] = repo[i], repo[left]
            left += 1
    repo[right], repo[left] = repo[left], repo[right]
    return left


repo = [x for x in range(1, 20)]
random.shuffle(repo)

qs(repo, 0, 18)

print(repo)

del repo

print("Ex 2-1-2 merge sort")


def merge_sort(repo):
    i = 0
    while True:
        if i >= len(repo):
            break
        # Step 1: separate
        sub_repo = []
        j = 0
        while True:
            sub_repo += [repo[j:j+2**i]]
            j += 2**i
            if j >= len(repo):
                break
        repo = []
        # Step 2: merge
        for j in range(0, len(sub_repo) - 2):
            while True:
                pin1, pin2 = 0, 0
                if pin1 >= len(sub_repo[j]):
                    # Some end process here
                    break
                if pin2 >= len(sub_repo[j + 1]):
                    # Some end process here
                    break
                if sub_repo[j][pin1] >= sub_repo[j+1][pin2]
