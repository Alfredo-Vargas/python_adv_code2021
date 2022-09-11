import sys
import math

infile = sys.argv[1] if len(sys.argv) > 1 else "17.in"
xraw, yraw = open(infile).read().strip()[13:].split(",")
pxmin, pxmax = xraw.strip()[2:].split("..")
pymin, pymax = yraw.strip()[2:].split("..")
xmin, xmax = int(pxmin), int(pxmax)
ymin, ymax = int(pymin), int(pymax)


# v0xmin is given by the "n" consecutive numbers n(n+1)/2 = xmin
v0xmin = int((-1 + math.sqrt(1 + 2 * xmin)) / 2)
# vx0 = xmax + 1 misses the target after one time step therefore is the max
vx0_range = [vx0 for vx0 in range(v0xmin, xmax + 1)]

# vy0 = ymin - 1 misses the target after one time step therefore is the min
# vy0 = -ymin + 1 misses the target after one time step therefore is the max
vy0_range = [vy0 for vy0 in range(ymin - 1, -ymin + 1)]

# We guess a reasonable high time interval (not problem dependent ... sigh)
trange = [i for i in range(1, 1000)]

xrange, yrange = [], []


def hit_target(pos, r):
    if r == "x":
        if pos >= xmin and pos <= xmax:
            return True
    elif r == "y":
        if pos >= ymin and pos <= ymax:
            return True
    else:
        print(f"Direction unknown: {r}. Please give either \"x\" or \"y\".")
    return False


# xmotion we save points (time, vx0) that hit the target
for vx0 in vx0_range:
    xpos, v0 = 0, vx0
    for t in trange:
        xpos += v0
        v0 = v0 - 1 if v0 > 0 else 0
        if hit_target(xpos, "x"):
            xrange.append((t, vx0))

# ymotion we save points (time, vy0) that hit the target
for vy0 in vy0_range:
    ypos, v0 = 0, vy0
    for t in trange:
        ypos += v0
        v0 = v0 - 1
        if hit_target(ypos, "y"):
            yrange.append((t, vy0))

# velocities v0x and v0y that hit the target at the same time
v0x, v0y = [], []
for yvalues in yrange:
    for xvalues in xrange:
        if yvalues[0] == xvalues[0]:
            v0x.append(xvalues[1])
            v0y.append(yvalues[1])

v0ymax = max(v0y)

# We calculate the maximum height
y, vy = 0, v0ymax
for t in trange:
    y += vy
    vy = vy - 1
    if vy == 0:
        print("\nPart 1, solution:")
        print(f"The maximum height is: {y}.")
        break


# The total velocities pairs that hit target (included repeated)
v0_pairs = list(zip(v0x, v0y))
print("\npart 2, solution:")
print(f"Number of velocities which hit the target: {len(set(v0_pairs))}.")
