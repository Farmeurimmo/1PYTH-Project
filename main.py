def new_board(n):
    return [[0] * n] * n


def display_board(board, n):
    max_length = 0
    for i in range(n):
        text = str(i + 1) + (len(str(n)) - len(str(i + 1))) * " " + " | "
        for j in range(n):
            text += ("." if board[i][j] == 0 else ("x" if board[i][j] == 1 else "o")) + " " * len(str(n))
        print(text)
        if max_length < len(text):
            max_length = len(text)

    print(" " * (len(str(n)) + 1), end="")
    for i in range(max_length - 3):
        print("-", end="")
    print()

    print(len(str(n)) * " " + 3 * " ", end="")

    for i in range(n):
        print(i + 1, end=" " + " " * (len(str(n)) - len(str(i + 1))))


def possible_square(board, n, player, i, j):
    if i - 1 > 0 and board[i - 1][j] != player:
        return False
    if i + 1 < n and board[i + 1][j] != player:
        return False
    if j - 1 > 0 and board[i][j - 1] != player:
        return False
    if j + 1 < n and board[i][j + 1] != player:
        return False
    if board[i][j]:
        return False


def select_square(board, n, player):
    return int(input("Choisir un numéro de ligne : ")), int(input("Choisir un numéro de colonne : "))


def update_board(board, player, i, j):
    board[i][j] = player


def again(board, n, player):
    for i in range(n):
        for j in range(n):
            if not possible_square(board, n, player, i, j):
                return False
    return True


n = 12
board = new_board(n)

display_board(board, n)
