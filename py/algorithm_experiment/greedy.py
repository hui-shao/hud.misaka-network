import random
import math
from operator import attrgetter

SCALE_OF_DATA = 40

print("Ex 5-1 Solving package problem with greedy method")

# Hey, we got a "rage" and some armor equipment here.
# Different equipment needs different power and give different armor.
# We only have fixed power so we must find a way to give her the most armor.
# We have no time yet. Equipment must be completed as soon as possible

# Generate data
class Equipment:
    def __init__(self, power, armor):
        self.power = power
        self.armor = armor
        self.id = id(self) % 10000

        if power == 0:
            self.ratio = math.inf
        else:
            self.ratio = armor / power


sto = []
for i in range(0, 20):
    sto += [Equipment(random.randint(0, SCALE_OF_DATA), random.randint(0, SCALE_OF_DATA))]

maximum_power = random.randint(0, SCALE_OF_DATA * 3)

# Sort data
sto = sorted(sto, key=attrgetter("ratio"))
sto.reverse()

solution = {
    "value_sum": 0,
    "power_sum": 0,
    "list": []
}
while True:
    if solution["power_sum"] + sto[0].power <= maximum_power:
        solution["value_sum"] += sto[0].armor
        solution["power_sum"] += sto[0].power
        solution["list"] += [sto[0].id]
        del sto[0]
    else:
        break

def progress_bar(value, max_value, width):
    value = int(value)
    max_value = int(max_value)
    width = int(width)
    bar = "-" * width
    bar_fill_width = int(value / max_value * width)
    bar = "#" * bar_fill_width + bar[bar_fill_width:]
    return bar

print("""
    EQUIPMENT PICK METHOD -------------------------------------
    ID = Misaka_0x447f's "rage" pick method
    ARMOR = """ + str(solution["value_sum"] + 1) + " / " + str(solution["value_sum"] + 1) + """ kN  100%
             """ + progress_bar(100, 100, 50) + """
    POWER LOAD = """ + str(solution["power_sum"]) + " / " + str(maximum_power) + """ MW  """ + str(int(solution["power_sum"] / maximum_power * 100)) + """%
             """ + progress_bar(solution["power_sum"], maximum_power, 50) + """
    *** EQUIPMENT LIST ***
    """ + str(solution["list"]) + """
    -----------------------------------------------------------
""")
