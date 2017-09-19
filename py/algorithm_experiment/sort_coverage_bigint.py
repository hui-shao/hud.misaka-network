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

print("Ex 2-2 coverage")


def show_board(board):
    print("board status:")
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == -1:
                print("#", end=' ')
            else:
                print(my_base64(board[i][j]), end=' ')
        print("")


def my_base64(number):
    li = "·ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_"
    return li[number]


def index_in_matrix(matrix, value):
    for i in range(len(matrix)):
        if value in matrix[i]:
            return [i, matrix[i].index(value)]
    return False


size = 2**3
print("problem size: ", size)

board = []
for i in range(size-1):
    board += [[0] * size]

bad_sector = random.sample(range(0, size-1), 2)
print("bad sector is located at ", bad_sector)
board[bad_sector[0]][bad_sector[1]] = -1
show_board(board)

step = 0


def board(x, y, size):
    global step
    if size == 1:
        return 0
    step += 1
    size = int(size / 2)

