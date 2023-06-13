def tic_tac_toe(board):
    # Check rows
    for row in board:
        if row.count('X') == 3:
            return 'X'
        elif row.count('O') == 3:
            return 'O'

    # Check columns
    for col in range(3):
        column = [board[row][col] for row in range(3)]
        if column.count('X') == 3:
            return 'X'
        elif column.count('O') == 3:
            return 'O'

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2]:
        if board[0][0] == 'X':
            return 'X'
        elif board[0][0] == 'O':
            return 'O'

    if board[0][2] == board[1][1] == board[2][0]:
        if board[0][2] == 'X':
            return 'X'
        elif board[0][2] == 'O':
            return 'O'

    # No winner
    return 'No one'

board = [['X', 'O', 'O'],
         ['X', 'X', 'O'],
         ['O', 'X', 'X']]

winner = tic_tac_toe(board)
print(f"The winner is: {winner}")
