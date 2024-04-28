def initialize_board(num_rows,num_cols):
    board = []
    for row in range(num_rows):
        row = []
        for cols in range(num_cols):
            row.append('-')
        board.append(row)
    return board

def print_board(board):
    for row in reversed(board):  # Starting from last row
        for item in row:
            print(item, end=" ")
        print()

def insert_chip(board, col, chip_type):
    for row in range(len(board)):
        if board[row][col] == '-':  # Check if spot is used
            board[row][col] = chip_type  # Place chip
            return row

def check_if_winner(board, col, row, chip_type):
    # Check rows
    count = 0
    for i in range(len(board[0])):  # Iterate over each column in this row
        if board[row][i] == chip_type:
            count += 1
            if count == 4:  # Check if count is enough to win
                return True
        else:
            count = 0

    # Check columns
    count = 0
    for i in range(len(board)):  # Iterate over each row in this column
        if board[i][col] == chip_type:
            count += 1
            if count == 4:
                return True
        else:
            count = 0

    return False

def board_full(board):
    for row in board:
        if '-' in row:
            return False
    return True



def main():
    num_rows = int(input("What would you like the height of the board to be? "))
    num_cols = int(input("What would you like the length of the board to be? "))
    print()
    board = initialize_board(num_rows,num_cols)
    print_board(board)
    print("\nPlayer 1: x\nPlayer 2: o\n")

    player = 1
    chip = "x"

    while True:
        print(f"Player {player}:", end = " ")
        column = int(input("Which column would you like to choose? "))
        row = insert_chip(board, column, chip)  # Get the row where the chip was placed
        if check_if_winner(board, column, row, chip):
            print_board(board)
            print()
            print(f"Player {player} won the game!")
            break
        elif board_full(board):
            print_board(board)
            print("Draw. Nobody wins.")
            break
        if chip == 'x':
            chip = 'o' # Switch chip type
        else:
            chip = 'x'
        if player == 1:
            player = 2   # Switch player
        else:
            player = 1
        print_board(board)
        print()



if __name__ == "__main__":
    main()