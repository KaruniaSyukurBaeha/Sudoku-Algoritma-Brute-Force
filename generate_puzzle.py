import random

def generate_empty_board():
    return [[0 for _ in range(9)] for _ in range(9)]

def is_valid(board, num, row, col):
    # Check row
    if num in board[row]:
        return False
    # Check column
    if num in [board[r][col] for r in range(9)]:
        return False
    # Check 3x3 box
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False
    return True

def find_empty(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None

def solve(board):
    empty = find_empty(board)
    if not empty:
        return True
    row, col = empty
    nums = list(range(1, 10))
    random.shuffle(nums)
    for num in nums:
        if is_valid(board, num, row, col):
            board[row][col] = num
            if solve(board):
                return True
            board[row][col] = 0
    return False

def generate_puzzle():
    board = generate_empty_board()
    solve(board)
    for _ in range(random.randint(20, 40)): 
        row, col = random.randint(0, 8), random.randint(0, 8)
        while board[row][col] == 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = 0
    return board

def save_puzzle(board, filename="data/example_puzzles.txt"):
    with open(filename, 'w') as file:
        for row in board:
            file.write(' '.join(map(str, row)) + '\n')

def main():
    random.seed()  # Remove this line if you want more variation each time
    puzzle = generate_puzzle()
    save_puzzle(puzzle)
    print("Puzzle Sudoku telah dibuat dan disimpan ke 'data/example_puzzles.txt'.")

if __name__ == "__main__":
    main()
