# credits for the solution to:
# https://github.com/jonathanpaulson/AdventOfCode/blob/master/2021/15.py
import sys
import heapq

infile = sys.argv[1] if len(sys.argv) > 1 else "15.in"

risk_map = []
for line in open(infile):
    risk_map.append([int(x) for x in line.rstrip()])

n_rows = len(risk_map)
n_cols = len(risk_map[0])


# Neighbour Points for Dijkstra Exploration
# (row, column) + neighbour = up, right, down, left
# neighbours = [(0, 1), (1, 0)]  # works for only for test
# neighbours = [(0, 1), (1, 0), (0, -1)] # works for test and part 1
neighbours = [(-1, 0), (0, 1), (1, 0), (0, -1)]

# We implement Dijkstra algorithm
def solve(n_tiles):
    # Dijkstra map contains the values of cummulative risks
    DijkstraMap = [[None for _ in range(n_tiles * n_cols)] for _ in range(n_tiles * n_rows)]
    root_node = (0, 0, 0) # Top left node value (risk=0, i=0, j=0)
    HeapQueue = [root_node]
    while HeapQueue:
        (risk, i, j) = heapq.heappop(HeapQueue)  # the highest (parent node is popped)
        # we check for values less than zero because we explore in all four possible directions
        if i < 0 or i >= n_tiles * n_rows or j < 0 or j >= n_tiles * n_cols:
            continue

        # Begin lines Relevant for part two only
        new_risk = risk_map[i % n_rows][j % n_cols] + (i // n_rows) + (j // n_cols)
        if new_risk > 9:
            new_risk -= 9
        # End lines relevant for part two only

        # Begin line relevant for part one only
        # new_risk = risk_map[i][j]
        # End line relevant for part one only

        ij_risk = risk + new_risk

        # If we have not visited Dijkstra map before or the risk_value is lower
        # than the cummulative risk at the Dijkstra map then:
        # this conditions establish that we built a min Heap (parent node is less than its children)
        if DijkstraMap[i][j] is None or ij_risk < DijkstraMap[i][j]:  
            DijkstraMap[i][j] = ij_risk
        else:  # we have visited Dijkstra map or the risk value is higher
            continue

        if i == n_tiles * n_rows - 1 and j == n_tiles * n_cols - 1:
            break

        # We append those four nodes to the HeapQueue
        for point in neighbours:
            new_i, new_j = i + point[0], j + point[1] 
            heapq.heappush(HeapQueue,(DijkstraMap[i][j], new_i, new_j))
    # End of while Q, either we reach the end node or we have no more nodes in the HeapQueue

    return DijkstraMap[n_tiles * n_rows - 1][n_tiles * n_cols - 1] - risk_map[0][0]

print(solve(1))
print(solve(5))
# solution part 1 is: 696
# solution part 1 is: 2952
