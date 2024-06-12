import time

def is_valid(board, num, row, col):
    # Check row
    if num in board[row]:
        return False
    # Check column
    for r in range(9):
        if board[r][col] == num:
            return False
    # Check 3x3 subgrid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == num:
                return False
    return True

def find_empty_cell(board):
    for r in range(9):
        for c in range(9):
            if board[r][c] == 0:
                return r, c
    return None

def solve_sudoku(board):
    empty = find_empty_cell(board)
    if not empty:
        return True
    row, col = empty
    for num in range(1, 10):
        if is_valid(board, num, row, col):
            board[row][col] = num
            if solve_sudoku(board):
                return True
            board[row][col] = 0
    return False

def print_board(board):
    for i in range(9):
        if i % 3 == 0 and i != 0:
            print("-" * 21)
        for j in range(9):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            else:
                print(board[i][j], end=" ")

def read_puzzle_from_file(filename):
    with open(filename, 'r') as f:
        board = []
        for line in f:
            board.append([int(num) for num in line.split()])
    return board

def main():
    board = read_puzzle_from_file("data/example_puzzles.txt")
    print("Puzzle Sudoku awal:")
    print_board(board)
    
    start_time = time.time()  # Mulai menghitung waktu
    if solve_sudoku(board):
        end_time = time.time()  # Berhenti menghitung waktu
        print("\nSudoku berhasil dipecahkan:")
        print_board(board)
        elapsed_time = end_time - start_time
        print(f"\nWaktu yang dibutuhkan: {elapsed_time:.4f} detik")
    else:
        print("\nTidak ada solusi yang ditemukan.")

if __name__ == "__main__":
    main()
