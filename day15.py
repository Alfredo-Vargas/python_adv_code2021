import sys
import heapq
import itertools
from collections import defaultdict, Counter, deque

sys.setrecursionlimit(int(1e6))

infile = sys.argv[1] if len(sys.argv)>1 else '15.in'

G = []
for line in open(infile):
    G.append([int(x) for x in line.strip()])
R = len(G)
C = len(G[0])
DR = [-1,0,1,0]
DC = [0,1,0,-1]

def solve(n_tiles):
    D = [[None for _ in range(n_tiles*C)] for _ in range(n_tiles*R)]
    Q = [(0,0,0)]
    while Q:
        (dist,r,c) = heapq.heappop(Q)
        if r<0 or r>=n_tiles*R or c<0 or c>=n_tiles*C:
            continue

        val = G[r%R][c%C] + (r//R) + (c//C)
        while val > 9:
            val -= 9
        rc_cost = dist + val

        if D[r][c] is None or rc_cost < D[r][c]:
            D[r][c] = rc_cost
        else:
            continue
        if r==n_tiles*R-1 and c==n_tiles*C-1:
            break

        for d in range(4):
            rr = r+DR[d]
            cc = c+DC[d]
            heapq.heappush(Q, (D[r][c],rr,cc))
    return D[n_tiles*R-1][n_tiles*C-1] - G[0][0]

print(solve(1))
print(solve(5))
# Advent of Code 2021

# Day 15 part 1 and 2
# import sys
# import numpy as np
# from collections import deque
#
# file = sys.argv[1] if len(sys.argv) > 1 else 'please input the 15 day data'
#
# # read contents
# pre_map = []
# for line in open(file):
#     pre_map.append([int(x) for x in line.rstrip()])
#
# risk_map = {}
# def add_risks(i, j):
#     if (i, j) in risk_map:
#         return risk_map[(i, j)]
#     if i < 0 or i >= len(pre_map) or j < 0 or j >= len(pre_map[i]):
#         return 1e9
#     if i == len(pre_map) - 1 and j == len(pre_map[i]) - 1:
#         return pre_map[i][j]
#     risk = pre_map[i][j] + min(add_risks(i + 1, j), add_risks(i, j + 1))
#     risk_map[(i, j)] = risk
#     return risk
#
# print(add_risks(0, 0) - pre_map[0][0])

# # store the contents on a 2x2 matrix
# risk_map = np.zeros((len(pre_map), len(pre_map[0])), dtype=int)
# for i in range(len(pre_map)):
#     risk_map[i, :] = pre_map[i]
#
# n_rows = len(risk_map[:, 0])
# n_cols = len(risk_map[0, :])
#
# # INSIGHT: Calculate the risk map first !!!
# # This risk_map will point the minimum value at each location
# # the borders of the risk_map are contributed only by one position
#
# risk_map[0, 0] = 0  # we do not count how the initial position
# for i in range(1, n_cols, 1):
#     risk_map[0, i] = risk_map[0, i - 1]+ risk_map[0, i]
# for i in range(1, n_cols, 1):
#     risk_map[i, 0] = risk_map[i - 1, 0] + risk_map[i, 0] 
#
# for i in range(1, n_rows, 1):
#     for j in range(1, n_cols, 1):
#         risk_map[i, j] = risk_map[i, j] + min(risk_map[i - 1, j], risk_map[i, j - 1])
#
# print("Answer part 1:")
# print(risk_map[n_rows - 1, n_cols - 1])
#
# # Wrong answers:
# # 697
# # 700
# # 701
# # 702  # Too high
# # 704  # Too high
# # 810  # Too high
#
# # Prepare the input data for part 2
# big_risk_map = np.zeros((len(pre_map) * 5, len(pre_map[0]) * 5), dtype=int) 
#
# # print(big_risk_map.shape)
# n_rows_bg = len(big_risk_map[:, 0])
# n_cols_bg = len(big_risk_map[0, :])
# # for i in range(n_rows_bg):
# #     for j in range(n_cols_bg):
#
