# n_dice_rolled = 0

# p1_pos = 6
# p2_pos = 9
# p1_score = 0
# p2_score = 0

# dice_values = [1, 2, 3]

# for i in range(1000):
#     for value in dice_values:
#         p1_pos += value
#     if p1_pos % 10 == 0:
#         p1_pos = 10
#     else:
#         p1_pos = p1_pos % 10
#         # if p1_pos + value > 10 == 0:
#         #     p1_pos = (p1_pos + value) % 10
#     p1_score += p1_pos
#     print(
#         f"Player 1 rolls {dice_values[0]}+{dice_values[1]}+{dice_values[2]} moves to spaces {p1_pos} for a total score of {p1_score}"
#     )
#     dice_values[0] += 3
#     dice_values[1] += 3
#     dice_values[2] += 3
#     n_dice_rolled += 3
#     if p1_score >= 1000:
#         print(f"Player 1 won. Game ended with a total of rolled dice: {n_dice_rolled}")
#         print(f"The magic number is {n_dice_rolled * p2_score}")
#         break
#     for value in dice_values:
#         p2_pos += value
#         # if p2_pos + value > 10 == 0:
#         #     p2_pos = (p2_pos + value) % 10
#     if p2_pos % 10 == 0:
#         p2_pos = 10
#     else:
#         p2_pos = p2_pos % 10
#     # p2_pos = p2_pos % 10
#     p2_score += p2_pos
#     print(
#         f"Player 2 rolls {dice_values[0]}+{dice_values[1]}+{dice_values[2]} moves to spaces {p2_pos} for a total score of {p2_score}"
#     )
#     dice_values[0] += 3
#     dice_values[1] += 3
#     dice_values[2] += 3
#     n_dice_rolled += 3
#     if p2_score >= 1000:
#         print(f"Player 2 won. Game ended with a total of rolled dice: {n_dice_rolled}")
#         print(f"The magic number is {n_dice_rolled * p1_score}")
#         break

# Part 2
# Solution taken from:
# https://github.com/jonathanpaulson/AdventOfCode/blob/master/2021/21.py

p1_pos = 6 - 1
p2_pos = 9 - 1

game_states = {}


# Solve the problem by recursion will be impossible with only brute force,
# however given the initial states of every round is limited, then one can introduce memoization together with recursion!
def count_wins(p1, p2, s1, s2):
    if s1 >= 21:
        return (1, 0)
    if s2 >= 21:
        return (0, 1)
    if (p1, p2, s1, s2) in game_states:
        return game_states[(p1, p2, s1, s2)]
    ans = (0, 0)
    for d1 in [1, 2, 3]:
        for d2 in [1, 2, 3]:
            for d3 in [1, 2, 3]:
                new_p1 = (p1 + d1 + d2 + d3) % 10
                # makes the correction because we start from the given position -1
                new_s1 = s1 + new_p1 + 1
                x1, y1 = count_wins(p2, new_p1, s2, new_s1)
                ans = (ans[0] + y1, ans[1] + x1)
    game_states[(p1, p2, s1, s2)] = ans
    return ans


print(max(count_wins(p1_pos, p2_pos, 0, 0)))
