def the_sequence(n):
    """Return the n firsts number of the sequence
        :param n (int): the number of terms that we want to return
        :return res (list) the list of the n firts term of the sequence"""
    res = ["1"]
    for i in range(n-1):
        res.append(next_term(res[i]))
    return res


def is_valid_sudoku(board):
    """Return if the sudoku board is good or not
        :param board (list) the list containing the sudoku board
        :return res (bool) if the board is good or not"""
    for i in range(9):
        # col = regroup the i^th colomn
        # box = regroup the i^th 3 x 3 sub-boxe
        col = [board[k][i] for k in range(9)]
        box = [board[(k%3)+3*(i//3)][(k//3)+3*(i%3)] for k in range(9)]
        for j in range(9):
            # verify there is no tuples
            if board[i].count(str(j)) > 1 or col.count(str(j)) > 1 or box.count(str(j)) > 1:
                return False
    return True


def next_term(a):
    """auxiliary function who compute the next term of the sequence"""
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
    return "".join(list(map(str, res)))


def is_valid_tictactoe(board):
    """Return if the tictactoe board is good or not
        :param board (list) the list containing the tictactoe board
        :return res (bool) if the board is good or not"""
    X = 0
    O = 0
    for line in board:
        X = X + line.count("X")
        O = O + line.count("O")
    return X >= O and X - O <= 1




def test():
    valid_board = [
                  ["5", "3", ".", ".", "7", ".", ".", ".", "."]
                , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    invalid_board_col = [
                  ["5", "3", ".", ".", "7", ".", ".", ".", "."]
                , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                , ["6", ".", ".", ".", "6", ".", ".", ".", "3"]
                , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    invalid_board_line = [
                  ["5", "3", ".", ".", "7", ".", ".", ".", "."]
                , ["6", ".", ".", "1", "6", "5", ".", ".", "."]
                , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                , ["5", ".", ".", ".", "6", ".", ".", ".", "3"]
                , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                , [".", "6", ".", ".", ".", ".", "2", "8", "."]
                , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    invalid_board_box = [
                  ["5", "3", ".", ".", "7", ".", ".", ".", "."]
                , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
                , [".", "9", "8", ".", ".", ".", ".", "6", "."]
                , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
                , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
                , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
                , [".", "6", ".", ".", ".", ".", "2", "8", "7"]
                , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
                , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]


    tictactoe_valid = ["XO ", " X ", " "]
    tictactoe_not_valid = ["XOX", " X ", " "]
    tictactoe_invalid = ["XOO", " X ", " "]

    print (is_valid_sudoku (valid_board))
    print (is_valid_sudoku (invalid_board_col))
    print (is_valid_sudoku (invalid_board_line))
    print (is_valid_sudoku (invalid_board_box))
    print(is_valid_tictactoe(["XO ", " X ", " "]))
    print(the_sequence(1))
test()

