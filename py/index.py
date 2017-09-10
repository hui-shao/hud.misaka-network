print("""
    hello world
""")
# single line comment
"""
multi-line comments
"""
var1 = 2
var2 = 8
print("the value is", var1 + var2, ",", var1 ** var2, ",", var2 // var1)
var3 = "str"
var4 = "ing"
var3 += var4
print(var3[0:5])
var5 = ["a", "b", "c"]
var5[0:1] = ["d", "e"]
print("count of e:", var5.count("e"), ",", len(var5), var5)
a, b = 0, 1
while b < 100:
    print(b, end=",")
    a, b = b, a + b


def func_sgn(arg1):
    if arg1 > 0:
        return 1
    if arg1 == 0:
        return 0
    if arg1 < 0:
        return -1


# x = int(input("Some number required: "))
x = 42
# spaceship operator? not exist.
if func_sgn(x - 42) == 0:
    print("true")
print("false")

for i in range(5, 10):
    print(i)
