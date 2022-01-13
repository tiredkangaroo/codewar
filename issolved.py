def is_solved(board):
    zeros = False
    for s in board:
        if s[0] == s[1] == s[2]: #if one way is the same, horizantal win
            return s[0]
        if s[0] == 0:
            zeros = True
    if board[0][0] == board[1][0] == board[2][0]: #vertical win (for the left)
        return board[0][0]
    elif board[0][1] == board[1][1] == board[2][1]: #vertical win (for the middle)
        return board[0][1]
    elif board[0][2] == board[0][2] == board[2][2]: #vertical win (for the end)
        return board[0][2]
    elif board[0][0] == board[1][1] == board[2][2]: #diagnal win
        return board[0][0]
    elif zeros:
        return -1
    else:
        return 0
print(is_solved([[0, 0, 1], [0, 1, 2], [2, 1, 0]]))
print(is_solved([[1, 1, 1], [0, 2, 2], [0, 0, 0]]))
board = [[2, 1, 2], [2, 1, 1], [1, 1, 2]]