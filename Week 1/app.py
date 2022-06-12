"""
Author: Sebastian Gomez

Instructor: Brad Lythgoe

Tic-Tac-Toe is a game in which two players seek in alternate turns to complete a row, a column, or a diagonal with either three x's or three o's 
drawn in the spaces of a grid of nine squares.
"""

def create_numbers():
    table_numbers = [1,2,3,4,5,6,7,8,9]
    return table_numbers

def board(table_numbers):

    print()
    print(f"          {table_numbers[0]} | {table_numbers[1]} | {table_numbers[2]}")
    print("          ----------")
    print(f"          {table_numbers[3]} | {table_numbers[4]} | {table_numbers[5]}")
    print("          ----------")
    print(f"          {table_numbers[6]} | {table_numbers[7]} | {table_numbers[8]}")
    print()

def player_move(player, table_numbers):
    choice = int(input(f"Player {player}'s: Choose a square (1-9): "))
    if choice <= 0 or choice >= 10:
        print("Please select the correct square.")
    else:
        table_numbers[choice - 1] = player

def turn(player):
    if player == "" or player == "o":
        return "x"
    elif player == "x":
        return "o"

def winner(options):

    # Rows
    # 1-2-3
    if options[0] == "x" and options[1] == "x" and options[2] == "x" or options[0] == "o" and options[1] == "o" and options[2] == "o":
        return True
    # 4-5-6
    elif options[3] == "x" and options[4] == "x" and options[5] == "x" or options[3] == "o" and options[4] == "o" and options[5] == "o":
        return True
    # 7-8-9
    elif options[6] == "x" and options[7] == "x" and options[8] == "x" or options[6] == "o" and options[7] == "o" and options[8] == "o":
        return True

    # Columns
    # 1-4-7
    elif options[0] == "x" and options[3] == "x" and options[6] == "x" or options[0] == "o" and options[3] == "o" and options[6] == "o":
        return True
    # 2-5-8
    elif options[1] == "x" and options[4] == "x" and options[7] == "x" or options[1] == "o" and options[4] == "o" and options[7] == "o":
        return True
    # 3-6-9
    elif options[0] == "x" and options[7] == "x" and options[8] == "x" or options[2] == "o" and options[5] == "o" and options[8] == "o":
        return True

    # Diagonally
    # 1-5-9
    elif options[0] == "x" and options[4] == "x" and options[8] == "x" or options[0] == "o" and options[4] == "o" and options[8] == "o":
        return True
    # 3-5-7
    elif options[2] == "x" and options[4] == "x" and options[6] == "x" or options[2] == "o" and options[4] == "o" and options[6] == "o":
        return True

    else:
        return False

def draw(options):
    # When all the squares are full
    for i in range(9):
        if options[i] != "x" and options[i] != "o":
            return False
    return True
 
def main():

    player = turn("")
    complete_table = create_numbers()
    while winner(complete_table) == False and draw(complete_table) == False:
        board(complete_table)
        player_move(player, complete_table)
        player = turn(player)
    board(complete_table)
    print("GAME OVER")


if __name__ == '__main__':
    main()