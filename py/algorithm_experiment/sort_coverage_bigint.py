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


def board(sto, x, y, size):
    global step

    if step == 0:
        location = index_in_matrix(sto, -1)
    else:
        location = index_not_zero_in_matrix(sto, x, y, size)

    CONST_LOCATION_LEFT_TOP = 495855600
    CONST_LOCATION_RIGHT_TOP = 495855601
    CONST_LOCATION_LEFT_BOTTOM = 495855602
    CONST_LOCATION_RIGHT_BOTTOM = 495855603

    splitter = int(size / 2 - 1)

    '''
                   y
        +---------->
        |
        |
        |
        |
      x ↓

    '''

    if location[0] <= splitter + x:
        if location[1] <= splitter + y:
            location = CONST_LOCATION_LEFT_TOP
        else:
            location = CONST_LOCATION_RIGHT_TOP
    else:
        if location[1] <= splitter + y:
            location = CONST_LOCATION_LEFT_BOTTOM
        else:
            location = CONST_LOCATION_RIGHT_BOTTOM

    location_map = [[1, 1], [1, 1]]

    if location == CONST_LOCATION_LEFT_TOP:
        location_map[0][0] = 0
    elif location == CONST_LOCATION_RIGHT_TOP:
        location_map[0][1] = 0
    elif location == CONST_LOCATION_LEFT_BOTTOM:
        location_map[1][0] = 0
    elif location == CONST_LOCATION_RIGHT_BOTTOM:
        location_map[1][1] = 0
    else:
        return False

    step += 1

    for i in range(2):
        for j in range(2):
            if location_map[i][j] == 1:
                sto[splitter + i + x][splitter + j + y] = step

    size = int(size / 2)
    if size <= 1:
        return 0

    board(sto, x, y, size)
    board(sto, x + splitter + 1, y, size)
    board(sto, x, y + splitter + 1, size)
    board(sto, x + splitter + 1, y + splitter + 1, size)


def my_base64(number):
    li = "·ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_"
    return li[number]


def index_in_matrix(matrix, value):
    for i in range(len(matrix)):
        if value in matrix[i]:
            return [i, matrix[i].index(value)]
    return False


def index_not_zero_in_matrix(matrix, x, y, size):
    for i in range(x, x + size):
        for j in range(y, y + size):
            if matrix[i][j] != 0:
                return [i, j]
    return False


size = 2 ** 3
print("problem size: ", size)

board_sto = []
for i in range(size):
    board_sto += [[0] * size]

bad_sector = random.sample(range(size), 2)
print("bad sector is located at ", bad_sector)
board_sto[bad_sector[0]][bad_sector[1]] = -1
step = 0

show_board(board_sto)

board(board_sto, 0, 0, size)

show_board(board_sto)
