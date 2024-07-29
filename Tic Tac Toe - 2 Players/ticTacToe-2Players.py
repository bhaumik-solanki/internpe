def displayBoard(board):
    print("\n", end="")
    for i, row in enumerate(board):
        print('|'.join(row))
        if i < len(board) - 1:
            print('-' * 5)

def checkWin(board, user):
    for row in board:
        if all(cell == user for cell in row):
            return True
    for col in range(3):
        if all(board[row][col] == user for row in range(3)):
            return True
    if all(board[i][i] == user for i in range(3)) or all(board[i][2 - i] == user for i in range(3)):
        return True
    return False

def isDraw(board):
    return all(cell != ' ' for row in board for cell in row)

def userMove(board):
    while True:
        try:
            row = int(input("Enter row (0, 1, 2): "))
            col = int(input("Enter column (0, 1, 2): "))
            if 0 <= row <= 2 and 0 <= col <= 2 and board[row][col] == ' ':
                return row, col
            else:
                print("Invalid move, Try again!")
        except ValueError:
            print("Invalid input, enter numbers between 0 and 2 only.")

board = [[' ' for _ in range(3)] for _ in range(3)]
user1Turn = True
user2Turn = False
while True:
    displayBoard(board)
    if user1Turn:
        print("\n")
        print("User-1's turn:")
        row, col = userMove(board)
        board[row][col] = 'X'
    else:
        print("\n")
        print("User-2's turn:")
        row, col = userMove(board)
        board[row][col] = 'O'
    if checkWin(board, 'X'):
        displayBoard(board)
        print("\nUser-1 wins!")
        break
    elif checkWin(board, 'O'):
        displayBoard(board)
        print("\nUser-2 wins!")
        break
    elif isDraw(board):
        displayBoard(board)
        print("\nIt's a draw!")
        break
    user1Turn = not user1Turn
    user2Turn = not user2Turn