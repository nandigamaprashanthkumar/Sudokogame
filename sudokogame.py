import random
import copy

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - ")

        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(board[i][j])
            else:
                print(str(board[i][j]) + " ", end="")

def is_valid_move(board, row, col, num):
    # Check if the number is not in the same row or column
    if num in board[row] or num in [board[i][col] for i in range(9)]:
        return False

    # Check if the number is not in the 3x3 grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(start_row, start_row + 3):
        for j in range(start_col, start_col + 3):
            if board[i][j] == num:
                return False

    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid_move(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def generate_sudoku_board():
    board = [[0] * 9 for _ in range(9)]
    solve_sudoku(board)

    # Remove numbers to create the puzzle
    for _ in range(20):
        row, col = random.randint(0, 8), random.randint(0, 8)
        while board[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = 0

    return board

def is_board_full(board):
    return all(all(cell != 0 for cell in row) for row in board)

def main():
    sudoku_board = generate_sudoku_board()
    user_board = copy.deepcopy(sudoku_board)

    while not is_board_full(user_board):
        print_board(user_board)
        try:
            row = int(input("Enter row (1-9): ")) - 1
            col = int(input("Enter column (1-9): ")) - 1
            num = int(input("Enter number (1-9): "))
        except ValueError:
            print("Invalid input. Please enter valid values.")
            continue

        if 0 <= row < 9 and 0 <= col < 9 and 1 <= num <= 9:
            if user_board[row][col] == 0:
                if is_valid_move(sudoku_board, row, col, num):
                    user_board[row][col] = num
                else:
                    print("Invalid move. Try again.")
            else:
                print("Cell is already filled. Try again.")
        else:
            print("Invalid input. Please enter valid values.")

    print("Congratulations! You solved the Sudoku:")
    print_board(user_board)

if __name__ == "__main__":
    main()
