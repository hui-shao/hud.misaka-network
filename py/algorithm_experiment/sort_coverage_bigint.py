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

print("before: ", repo)

qs(repo, 0, 18)

print("after: ", repo)

del repo

print("Ex 2-1-2 merge sort")


def merge_sort(seq):
    if len(seq) <= 1:
        return seq
    mid = int(len(seq) / 2)
    left = merge_sort(seq[:mid])
    right = merge_sort(seq[mid:])
    return merge(left, right)


def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result


repo = [x for x in range(1, 20)]
random.shuffle(repo)

print("before: ", repo)

repo = merge_sort(repo)

print("after: ", repo)

del repo
