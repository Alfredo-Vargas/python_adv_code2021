import sys
import math

infile = sys.argv[1] if len(sys.argv) > 1 else "17.in"
xraw, yraw = open(infile).read().strip()[13:].split(",")  # .split(":")
pxmin, pxmax = xraw.strip()[2:].split("..")
pymin, pymax = yraw.strip()[2:].split("..")
xmin, xmax = int(pxmin), int(pxmax)
ymin, ymax = int(pymin), int(pymax)

print(xmin, xmax)
print(ymin, ymax)


#  we guess a reasonable time interval where that should happen
t_range = [i for i in range(1, 2000)]

# we guess a reasonable vx0 velocity to be evaluated
vx0_range = [vx0 for vx0 in range(0, 2000)]
# we guess a reasonable vy0 velocity to be evaluated
vy0_range = [vy0 for vy0 in range(0, 2000)]

initial_x = []
initial_y = []


def hit_target(pos, r):
    if r == "x":
        if pos >= xmin and pos <= xmax:
            return True
    elif r == "y":
        if pos >= ymin and pos <= ymax:
            return True
    else:
        print("Direction not specified. Please give either \"x\" or \"y\".")
    return False


for vx0 in vx0_range:
    xpos, ypos, v0 = 0, 0, vx0
    for t in t_range:
        xpos += v0
        v0 = v0 - 1 if v0 > 0 else 0
        if hit_target(xpos, "x"):
            initial_x.append((t, vx0))


for vy0 in vy0_range:
    xpos, ypos, v0 = 0, 0, vy0
    for t in t_range:
        ypos += v0
        v0 = v0 - 1
        if hit_target(ypos, "y"):
            initial_y.append((t, vy0))

selected = []
for yvalues in initial_y:
    for xvalues in initial_x:
        if yvalues[0] == xvalues[0]:
            selected.append((xvalues[1], yvalues[1]))

vy0 = 0
for v in selected:
    if v[1] > vy0:
        vy0 = v[1]

filtered = []
for v in selected:
    if v[1] == vy0:
        filtered.append(v)


vx0 = 9999
for v in filtered:
    if v[0] < vx0:
        vx0 = v[0]

v0 = []
for v in filtered:
    if v[0] == vx0:
        v0.append(v)

# print(v0[0][1])
# height = (v0[0][1] ** 2) / 2
# print(height)

x0, y0, vz = 0, 0, v0[0][1]
for t in t_range:
    y0 += vz
    vz = vz - 1
    if vz == 0:
        print(y0)
        break

