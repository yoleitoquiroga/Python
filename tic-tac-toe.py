# Function to print the Tic-Tac-Toe board
def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 10)

# Function to check for a win
def check_win(board, player):
    # Check rows, columns, and diagonals
    for row in board:
        if all([cell == player for cell in row]):
            return True
    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True
    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

# Function to check for a draw
def check_draw(board):
    return all([cell != " " for row in board for cell in row])

# Function to get player input and update the board
def make_move(board, player):
    while True:
        try:
            row, col = map(int, input(f"Player {player}, enter your move (row and column): ").split())
            if board[row][col] == " ":
                board[row][col] = player
                break
            else:
                print("Cell is already taken. Try again.")
        except (ValueError, IndexError):
            print("Invalid input. Please enter row and column as two numbers between 0 and 2.")

# Main game loop
def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    while True:
        print_board(board)
        make_move(board, current_player)
        if check_win(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        if check_draw(board):
            print_board(board)
            print("The game is a draw!")
            break
        current_player = "O" if current_player == "X" else "X"

if __name__ == "__main__":
    main()
