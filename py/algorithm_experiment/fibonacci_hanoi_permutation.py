print("Ex 1-1 fibonacci in recursive")


def fib1(n):
    if n == 1 or n == 2:
        return 1
    return fib1(n-1) + fib1(n-2)


print(fib1(34))


print("Ex 1-2 fibonacci in recursive(enhanced)")


sto = [-1, 1, 1]


def fib2(n):
    global sto
    # extend sto
    if n >= len(sto):
        sto = sto + [-1] * (n - len(sto) + 1)

    if n <= 2:
        return 1
    if sto[n-1] == -1:
        sto[n - 1] = fib2(n - 1)
    if sto[n-2] == -1:
        sto[n - 2] = fib2(n - 2)
    sto[n] = sto[n - 1] + sto[n - 2]
    return sto[n]


print(fib2(34))
