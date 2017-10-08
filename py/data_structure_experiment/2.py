import math


print("Ex 2-1 ---------------------------------------------")


def is_prime(n):
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


def num(m, k, xx):
    m += 1
    while True:
        if is_prime(m):
            xx += [m]
            k -= 1
        if k == 0:
            break
        m += 1
    # deep copy was not applied here.
    return xx


print("This program is to get k prime numbers which are larger than m.")
m = input(">> Please input two integers to m and k : ")
m = m.split(" ")
m, k = m[0], m[1]
print(">> The " + k + " prime numbers which are larger than " + m + " are:")
print(num(int(m), int(k), []))


print("Ex 2-2 ---------------------------------------------")


print("""****************************************************************
*     This program is to solve Problem of Three Color Ball.    *
* The Problem is as follows: There are 12 balls in the pocket. *
* Amony them, 3 balls are red,3 balls are white and 6 balls    *
* are black. Now take out any 8 balls from the pocket,how      *
* many color combinations are there?                           *
****************************************************************
 >> The solutions are:
  No.     RED BALL  WHITE BALL   BLACK BALL
-----------------------------------------------------""")

r, w, b = 0, 0, 0
counter = 1

for i in range(0, 4):
    for j in range(0, 4):
        for k in range(0, 7):
            if i + j + k == 8:
                print((2 - int(math.log(counter, 10))) * " ", counter,
                      "    |     ", str(i), "     |    ", str(j),
                      "    |     ", str(k))
                counter += 1


del b

print("Ex 2-3 ---------------------------------------------")
n = int(input("how many students are in your class?"))
print("please input a student three scores:")
sto = []
for i in range(0, n):
    sto += [input("the no." + str(i + 1) + ":  ")]

summary = 0
print(" num        a    b    c     av")
for i in range(0, n):
    curr = sto[i].split(",")
    summary += (int(curr[0]) + int(curr[1]) + int(curr[2])) / 3
    print(" " + str(i) + " " * 10 + curr[0] + " " * 3 + curr[1] +
          " " * 3 + curr[2] + " " * 5 + str((int(curr[0]) + int(curr[1]) + int(curr[2])) / 3))

print("average of the class=" + str(summary / n))
