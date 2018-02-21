# Problem 0

print ("Go Rams Go!")

# Problem 1

name = input("What is your name?")
print("Hi {} let's start!".format(name)) # Will replace "{}" with name

# Problem 2

m = int(input("Value of mass?"))
v = int(input("value of velocity?"))

p = m * v

pstr = str(p)
print("The momentum of the spacecraft is " + pstr)

# Problem 3

st = 0.299792
time = int(input("Amount of time(picosecondss)?"))

distance = st * time
print("The claculated distance is  " + distance)

# Problem 4

miles = float(input("number of miles?"))
minutes = float(input("number of minutes?"))
average = miles / minutes
avstr = str(average)
print("The Average miles per hour is " + avstr)

# Program 5

Dragons = 914.8 / 168.2
ChartMonkeys = 1273.1 / 193.5
SolarWind = 1144.6 / 181.3

race = [Dragons, ChartMonkeys, SolarWind]
print(min(race))

# Problem 6

import numpy
x = [33,47,48,19,86,6]
xdiff = np.diff(x)
np.all(xdiff[0] == xdiff)

# Problem 7

import fileinput


# x[n+1] = C + (A * x[n] + M) / (B * x[n] + N)
def nextx(x, c, a, m, b, n):
    return c + (a * x + m) / (b * x + n)


def process(line):
    x, a, b, c, m, n, e = map(float, line.split())

    if e < 0:
        e = -e

    for i in xrange(0, 100):
        newx = nextx(x, c, a, m, b, n)
        diff = newx - x
        if -e < diff and diff < e:
            return "{:.6f}".format(newx)
        x = newx
    return "DIVERGES"


count = None
for line in fileinput.input():
    if not count:
        count = int(line)
        continue
    print process(line)
    count = count - 1
