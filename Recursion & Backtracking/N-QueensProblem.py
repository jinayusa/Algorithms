# Solving the N-Queens problem using Backtracking
def solve_n_queens(n):
    """
    Solves the N-Queens problem and returns all valid board configurations.
    
    Time Complexity: O(N!) (Worst case, as we check all placements)
    Space Complexity: O(N) (Tracking columns and diagonals)
    """
    results = []  # Store all valid board configurations
    board = [-1] * n  # 1D array to store column placements for each row
    cols = set()  # To track occupied columns
    diagonals_pos = set()  # (row + col) for `\` diagonals
    diagonals_neg = set()  # (row - col) for `/` diagonals

    def backtrack(row):
        """Recursive function to place queens row by row."""
        if row == n:
            # Convert board to a visual representation
            results.append(generate_board(board, n))
            return
        
        for col in range(n):
            # Check if the column and diagonals are free
            if col in cols or (row + col) in diagonals_pos or (row - col) in diagonals_neg:
                continue  # Skip invalid positions

            # Place the queen
            board[row] = col
            cols.add(col)
            diagonals_pos.add(row + col)
            diagonals_neg.add(row - col)

            # Recur for next row
            backtrack(row + 1)

            # Backtrack: Remove queen and try next column
            board[row] = -1
            cols.remove(col)
            diagonals_pos.remove(row + col)
            diagonals_neg.remove(row - col)

    def generate_board(board, n):
        """Generates the board representation from column placements."""
        return ["".join("Q" if col == board[row] else "." for col in range(n)) for row in range(n)]

    # Start backtracking from the first row
    backtrack(0)

    return results

# Example Usage
n = 4
solutions = solve_n_queens(n)

print(f"Total solutions for {n}-Queens: {len(solutions)}")
for board in solutions:
    print("\n".join(board))
    print()
