# Advent of Code 2021
import numpy as np

# Day 4 part 1

# Sequence
sequence = []

# List of Bingo Cards and Bingo Cards State
bingo_cards = []
bingo_cards_state = []

# Bingo was obtained
bingo = False
indices_of_winners = []
last_winner_number = 0
last_winner_index = 0
last_winner_state = np.zeros((5, 5))

# We load the bingo cards and card states
with open("./data/day4.txt", "r") as file:
    lines = file.read().splitlines()
    sequence = np.array([int(p) for p in lines[0].split(",")])
    bingo_lines = lines[1:]
    counter = 0
    for line in bingo_lines:
        if (line == ""):
            temp_bingo_card = np.zeros((5, 5))
            temp_bingo_card_state = np.zeros((5, 5))
            counter = 0
            continue
        row = np.array([int(p) for p in line.split()])
        temp_bingo_card[counter][:] = row
        counter += 1
        if counter == 4:
            bingo_cards.append(temp_bingo_card)
            bingo_cards_state.append(temp_bingo_card_state)


# Function to detect bingo and append winner index to indices_of_winners
def is_there_bingo(number):
    global bingo  # to modify the global variable within the function scope
    global indices_of_winners  # to be aware of the global list of winners
    global last_winner_number
    global last_winner_index
    global last_winner_state
    row_of_ones = np.ones(5)
    column_of_ones = np.transpose(row_of_ones)
    stop_index = 0
    for bingo_state in bingo_cards_state:
        # Check if bingo card already won
        if stop_index not in indices_of_winners:
            # check for bingo on the rows of bingo_state
            for i in range(len(bingo_state)):
                if (np.dot(bingo_state[i, :],  column_of_ones) == 5):
                    bingo = True
                    if len(indices_of_winners) == 99:
                        last_winner_number = number
                        last_winner_index = stop_index
                        print("The state of last winner:")
                        last_winner_state = bingo_cards_state[stop_index]
                        print(last_winner_state)
                    indices_of_winners.append(stop_index)
        # Check if bingo card already won
        if stop_index not in indices_of_winners:
            # check for bingo on the columns of bingo_state
            for i in range(len(bingo_state)):
                if (np.dot(row_of_ones, bingo_state[:, i]) == 5):
                    bingo = True
                    if len(indices_of_winners) == 99:
                        last_winner_number = number
                        last_winner_index = stop_index
                        print("The state of last winner:")
                        last_winner_state = bingo_cards_state[stop_index]
                        print(last_winner_state)
                    indices_of_winners.append(stop_index)
        stop_index += 1
    return bingo


# Function to mark all the bingo cards which have the chosen random number
def mark_all_bingo_cards(chosen_number):
    for i in range(len(bingo_cards)):
        if chosen_number in bingo_cards[i]:
            index_i, index_j = np.where(bingo_cards[i] == chosen_number)
            bingo_cards_state[i][index_i[0]][index_j[0]] = 1


def prompt_first_winner(number):
    print(f"The taken number for first winner is: {number}")
    wi = indices_of_winners[0]  # one winner index
    print("The winner indices are:")
    print(indices_of_winners)
    print("The first winner card(s) and state is/are:")
    for index in indices_of_winners:
        print(bingo_cards[index])
        print(bingo_cards_state[index])
    bingo_cards_state[wi][bingo_cards_state[wi] == 0] = 2
    bingo_cards_state[wi][bingo_cards_state[wi] == 1] = 0
    bingo_cards_state[wi][bingo_cards_state[wi] == 2] = 1
    # We calculate the unmarked matrix
    um = np.multiply(bingo_cards_state[wi], bingo_cards[wi])
    print("The first winner card with unmarked only:")
    print(um)
    print(f"The total score is: {um.sum() * number}")


def prompt_last_winner_number(number, index):
    print(f"The taken number for last winner is: {number}")
    print("The winner index is:")
    print(index)
    print("The last winner card is:")
    print(bingo_cards[index])
    print("The last winner state is:")
    print(last_winner_state)
    bingo_cards_state[index][bingo_cards_state[index] == 0] = 2
    bingo_cards_state[index][bingo_cards_state[index] == 1] = 0
    bingo_cards_state[index][bingo_cards_state[index] == 2] = 1
    # We calculate the unmarked matrix
    um = np.multiply(bingo_cards_state[index], bingo_cards[index])
    print("The last winner card with unmarked only:")
    print(um)
    print(f"The total score is: {um.sum() * number}")


for number in sequence:
    # to stop marking after last winners has won
    if (len(indices_of_winners) == 100):
        break
    mark_all_bingo_cards(number)
    is_there_bingo(number)

    if bingo and len(indices_of_winners) == 1:
        prompt_first_winner(number)
        # break


# Day 4 part 2
prompt_last_winner_number(last_winner_number, last_winner_index)
