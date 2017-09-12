print("Ex 1-1 ---------------------------------------------")

n = int(input("Input N: "))
sum = 0
for i in range(1, n+1):
    sum += i * (n + 1 - i)
print(sum)

print("Ex 1-2 ---------------------------------------------")

n = int(input("Input N: "))
a = 0
b = 1
print(1)
for i in range(n - 1):
    a, b = b, a + b
    print(b)


print("Ex 1-3 ---------------------------------------------")

n = int(input("Input N: "))
counter = 0
while True:
    if n % 2 == 0:
        n = n / 2
    elif n % 2 == 1:
        n = n * 3 + 1
    if n == 1:
        print("n is 1 after", counter, "time(s) calculate")
        break
    else:
        counter = counter + 1
