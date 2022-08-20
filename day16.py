import sys

infile = sys.argv[1] if len(sys.argv) > 1 else "16.in"

risk_map = []
for line in open(infile):
    risk_map.append([int(x) for x in line.rstrip()])


