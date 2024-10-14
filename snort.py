def new_board(n):
    return [[0 for _ in range(n)] for _ in range(n)]


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
    print()


def possible_square(board, n, player, i, j):
    if i > n or i < 0 or j > n or j < 0:
        return False
    other_player = get_other_player(player)
    if n > i - 1 > 0 and board[i - 1][j] == other_player:
        return False
    if n > i + 1 > 0 and board[i + 1][j] == other_player:
        return False
    if n > j - 1 > 0 and board[i][j - 1] == other_player:
        return False
    if n > j + 1 > 0 and board[i][j + 1] == other_player:
        return False
    if board[i][j] != 0:
        return False
    return True


def select_square(board, n, player):
    return int(input("Choisir un numéro de ligne : ")) - 1, int(input("Choisir un numéro de colonne : ")) - 1


def update_board(board, player, i, j):
    board[i][j] = player


def get_other_player(player):
    return 1 if player == 2 else 2


def again(board, n, player):
    for i in range(n):
        for j in range(n):
            if possible_square(board, n, player, i, j):
                return True
    return False


def snort(n):
    board = new_board(n)
    display_board(board, n)
    current_player = 1

    while again(board, n, current_player):
        print("Au joueur", current_player, "de jouer")

        i, j = select_square(board, n, current_player)
        while not possible_square(board, n, current_player, i, j):
            i, j = select_square(board, n, current_player)

        update_board(board, current_player, i, j)
        display_board(board, n)

        if not again(board, n, current_player):
            break

        current_player = get_other_player(current_player)

    current_player = get_other_player(current_player)
    print("Le gagnant est le joueur", current_player)


snort(3)
