# Tic-Tac-Toe Game with AI Opponent with minimax algoritm

# Function to print the game board
def print_board(board):
    print("-------------")
    for i in range(3):
        print("|", end=" ")
        for j in range(3):
            print(board[i][j], end=" | ")
        print("\n-------------")

# Function to check for a win
def check_win(board, player):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True
    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == player:
            return True
    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    return False

# Function to check for a draw
def check_draw(board):
    return all(board[i][j] != " " for i in range(3) for j in range(3))

# Function to evaluate the board for the minimax algorithm
def evaluate(board):
    if check_win(board, "X"):
        return 1
    if check_win(board, "O"):
        return -1
    return 0

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_win(board, "X"):
        return 1
    if check_win(board, "O"):
        return -1
    if check_draw(board):
        return 0

    if is_maximizing:
        max_eval = float("-inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "X"
                    eval = minimax(board, depth + 1, False)
                    board[i][j] = " "
                    max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float("inf")
        for i in range(3):
            for j in range(3):
                if board[i][j] == " ":
                    board[i][j] = "O"
                    eval = minimax(board, depth + 1, True)
                    board[i][j] = " "
                    min_eval = min(min_eval, eval)
        return min_eval

# Function to make the AI's move using the minimax algorithm
def make_ai_move(board):
    best_eval = float("-inf")
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == " ":
                board[i][j] = "X"
                eval = minimax(board, 0, False)
                board[i][j] = " "
                if eval > best_eval:
                    best_eval = eval
                    best_move = (i, j)

    board[best_move[0]][best_move[1]] = "X"

# Function to play the game
def play_game():
    # Initialize the game board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "O"

    # Main game loop
    while True:
        print_board(board)

        if current_player == "O":
            row = int(input("Enter the row number (0-2): "))
            col = int(input("Enter the column number (0-2): "))
            if board[row][col] != " ":
                print("Invalid move. Try again.")
                continue
            board[row][col] = "O"
        else:
            make_ai_move(board)

        # Check for a win
        if check_win(board, current_player):
            print_board(board)
            print("Player", current_player, "wins!")
            break

        # Check for a draw
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # Switch players
        current_player = "X" if current_player == "O" else "O"

# Start the game
play_game()