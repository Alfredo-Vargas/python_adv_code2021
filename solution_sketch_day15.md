### Assumptions:
1. We navigate from top left towards bottom right
2. Every step is either to the right or down
- Consequence of this is that the total number of steps is equal to:
$$steps = n\_rows + n\_cols - 2$$
- The number 2 takes into account the fact the already start at the top left and we have already one step down and right into the risk map (input data)

### Methodology
1. We will create a function that takes the previous cumulative risk and position and wil returns two new risk values given by the outcome of whether one steps to the right or to down. Given that $i$ represents the row index and $j$ the column index, then:
```dot
digraph G {
    rankdir="LR";
    "S0, (i,j)" -> "S1, (i+1, j)" [label = "down"];
    "S0, (i,j)" -> "S2, (i, j+1)" [label = "right"];
    "S1, (i+1, j)" -> "S3, (i+2, j)" [label = "down"];
    "S1, (i+1, j)" -> "S4, (i+1, j+1)" [label = "right"];
    "S2, (i, j+1)" -> "S5, (i+1, j+1)" [label = "down"];
    "S2, (i, j+1)" -> "S6, (i, j+2)" [label = "right"];
    "S3, (i+2, j)" -> "S7, (i+3, j)" [label = "down"];
    "S3, (i+2, j)" -> "S8, (i+2, j+1)" [label = "right"];
    "S4, (i+1, j+1)" -> "S9, (i+2, j+1)" [label = "down"];
    "S4, (i+1, j+1)" -> "S10, (i+1, j+2)" [label = "right"];
    "S5, (i+1, j+1)" -> "S11, (i+2, j+1)" [label = "down"];
    "S5, (i+1, j+1)" -> "S12, (i+1, j+2)" [label = "right"];
    "S6, (i, j+2)" -> "S13, (i+1, j+2)" [label = "down"];
    "S6, (i, j+2)" -> "S13, (i, j+3)" [label = "right"];
  }
```
- The above function should contemplate the edge cases that occur whenever we reach $i=n\_cols$ and/or $j=n\_rows$.
#### Challenges
- Exploring all the possible paths under assumptions \#1 and \#2, means that the whole tree will have $2^{steps}$.
  - For example for $steps=18$ example given on has a total of paths: $262144$
  - For part 1 one has $steps=198$ with total of paths: $401734511064747568885490523085290650630550748445698208825344$
- So _we need to keep track of the cumulative sums but not keep track of the whole binary tree values_.

2. From the above challenge will then need to adjust the recursive function such we explore "enough further ahead".
- Taking only three steps ahead, we will have 8 possible paths
```python
def next_sum(i, j, current_sum, steps):
  if steps == 0:
  right_sum = current_sum + map(i, j+1)
  left_sum = current_sum + map(i+1, j)
  return (right_sum, down_sum)
```

# Review of previous approach and final solution
## Review
- The above approach is inconvenient/wrong for the following reasons:
  1. It assumes that the only possible moves involve, right or down. What if we would like to explore from bottom right towards top left? (This is inconvenient)
  2. Moreover, one could have particular geometries were the shortest path (or path with the least risk) is includes movements other moves such going up or left. The only restriction should be the boundary. (This was wrongly omitted, although for the Day 15 of Advent of Code sometimes there are no need to include the other movements, test and part 1 worked perfectly with just exploring only the neighbour to the right or to the bottom. Nevertheless for part two one must include the other types of exploration: up and left.
  3. Third the above approach demanded to much memory allocations as it must store the total amount of nodes which at every step doubles (if we include top and left moves, it quadruples!)

## Solution, applying the Dijkstra Algorithm (finding the shortest path)
