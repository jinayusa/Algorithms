# Sudoku Solver using Backtracking

def solve_sudoku(board):
    """
    Solves the given 9x9 Sudoku board in-place using backtracking.

    Time Complexity: O(9^N), where N is the number of empty cells.
    Space Complexity: O(N) due to recursion stack depth.
    """
    
    def is_valid(board, row, col, num):
        """
        Checks if placing `num` at board[row][col] is valid.
        """
        # Check if num is in the same row
        for x in range(9):
            if board[row][x] == num:
                return False
        
        # Check if num is in the same column
        for x in range(9):
            if board[x][col] == num:
                return False
        
        # Check if num is in the 3x3 subgrid
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if board[start_row + i][start_col + j] == num:
                    return False
        
        return True  # No conflicts, it's a valid placement

    def backtrack():
        """
        Backtracking function to fill the board.
        """
        for row in range(9):
            for col in range(9):
                if board[row][col] == '.':  # Find an empty cell
                    for num in map(str, range(1, 10)):  # Try numbers '1' to '9'
                        if is_valid(board, row, col, num):  # Check if the move is valid
                            board[row][col] = num  # Place the number
                            
                            if backtrack():  # Recursively solve the rest of the board
                                return True
                            
                            board[row][col] = '.'  # Backtrack (undo the move)
                    
                    return False  # No valid numbers found, return False
        return True  # If no empty cells left, the board is solved
    
    backtrack()  # Start solving

# Example Usage
sudoku_board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]

print("Original Sudoku Board:")
for row in sudoku_board:
    print(row)

solve_sudoku(sudoku_board)

print("\nSolved Sudoku Board:")
for row in sudoku_board:
    print(row)
