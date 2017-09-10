import copy
print("Ex 1-1-1 fibonacci in recursive")


def fib1(n):
    if n == 1 or n == 2:
        return 1
    return fib1(n-1) + fib1(n-2)


#print(fib1(34))


print("Ex 1-1-2 fibonacci in recursive(enhanced)")


sto = [-1, 1, 1]


def fib2(n):
    global sto
    # extend sto
    if n >= len(sto):
        sto = sto + [-1] * (n - len(sto) + 1)

    if n <= 2:
        return 1
    if sto[n-1] == -1:
        sto[n-1] = fib2(n-1)
    if sto[n-2] == -1:
        sto[n-2] = fib2(n-2)
    sto[n] = sto[n-1] + sto[n-2]
    return sto[n]


print(fib2(34))


print("Ex 1-2 hanoi puzzle")


def hanoi(count, post):
    # our goal is move it from source to target(a to b)
    if count >= 1:
        hanoi(count - 1, post[0] + post[2] + post[1])
        print(post[0], "->", post[1])
        hanoi(count - 1, post[2] + post[1] + post[0])


posts = ["a", "b", "c"]
hanoi(3, posts)


print("Ex 1-3 permutation puzzle")


def perm(list):
    for i in range(len(list)):
        perm_sto = copy.deepcopy(list[i])
        for j in range(len(list[i])):
            perm_sto2 = [perm_sto[i]]
            del perm_sto[i]
            if len(list[i]) == 1:
                print(list[i])
                d = list[i]
                return list[i]
            elif len(list[i]) > 1:
                list_sto = []
                for j in range(len(list[i])):
                    perm_output = perm(perm_sto) + perm_sto2
                    print(perm_output)
                    list_sto += perm_output
                return list_sto
            else:
                return -1


perm([[1, 2, 3, 4]])
