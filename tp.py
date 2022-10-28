def the_sequence(n):
    """Return the n firsts number of the sequence
        :param n (int): the number of terms that we want to return
        :return res (list) the list of the n firts term of the sequence"""
    res = ["1"]
    for i in range(n):
        res.append(next_term(res[i]))
    return res


def is_valid_sudoku(board):
    """Return if the sudoku board is good or Not
        :param board (list) the list containing the sudoku board
        :return res (bool) if the board is good or not"""
    for i in range(9):
        # verify the columns
        col = [board[k][i] for k in range(9)]
        for j in range(9):
            # verify the lines
            if board[i].count(j) > 1 or col.count(j) > 1:
                return False


def next_term(a):
    temp = 0
    count = 0
    res = []
    a = [i for i in str(a)]
    a = list(map(int, a))
    for i in a:
        if i == temp:
            count = count + 1
        else:
            if temp and count != 0:
                res.append(count)
                res.append(temp)
            temp = i
            count = 1
    res.append(count)
    res.append(temp)
    return int("".join(list(map(str, res))))


def is_valid_tictactoe(board):
    """Return if the tictactoe board is good or not
        :param board (list) the list containing the tictactoe board
        :return res (bool) if the board is good or not"""


print(the_sequence(6))
