n_dice_rolled = 0

p1_pos = 6
p2_pos = 9
p1_score = 0
p2_score = 0

dice_values = [1, 2, 3]

for i in range(1000):
    for value in dice_values:
        p1_pos += value
    if p1_pos % 10 == 0:
        p1_pos = 10
    else:
        p1_pos = p1_pos % 10
        # if p1_pos + value > 10 == 0:
        #     p1_pos = (p1_pos + value) % 10
    p1_score += p1_pos
    print(f"Player 1 rolls {dice_values[0]}+{dice_values[1]}+{dice_values[2]} moves to spaces {p1_pos} for a total score of {p1_score}")
    dice_values[0] += 3
    dice_values[1] += 3
    dice_values[2] += 3
    n_dice_rolled += 3
    if p1_score >=1000:
        print(f"Player 1 won. Game ended with a total of rolled dice: {n_dice_rolled}")
        print(f"The magic number is {n_dice_rolled * p2_score}")
        break
    for value in dice_values:
        p2_pos += value
        # if p2_pos + value > 10 == 0:
        #     p2_pos = (p2_pos + value) % 10
    if p2_pos % 10 == 0:
        p2_pos = 10
    else:
        p2_pos = p2_pos % 10
    # p2_pos = p2_pos % 10
    p2_score += p2_pos
    print(f"Player 2 rolls {dice_values[0]}+{dice_values[1]}+{dice_values[2]} moves to spaces {p2_pos} for a total score of {p2_score}")
    dice_values[0] += 3
    dice_values[1] += 3
    dice_values[2] += 3
    n_dice_rolled += 3
    if p2_score >=1000:
        print(f"Player 2 won. Game ended with a total of rolled dice: {n_dice_rolled}")
        print(f"The magic number is {n_dice_rolled * p1_score}")
        break
