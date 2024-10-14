def new_board(n):
    board = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n - 1):
        board[i][0] = 1
    for j in range(1, n):
        board[n - 1][j] = 2
    return board


def display_board(board, n):
    print("Joueur 1 = x", "Joueur 2 = o")
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


def select_pawn(board, n, directions, player):
    return int(input("Choisir la ligne d'un pion : ")) - 1, int(input("Choisir la colonne d'un pion : ")) - 1


def ask_for_direction():
    return int(input("Choisir la direction du mouvement (1 pour Nord, 2 pour Est, 3 pour Sud et 4 pour Ouest) : ")) - 1


def select_move(board, n, directions, player, i, j):
    m = ask_for_direction()
    while True:
        if len(directions) >= m >= 0:
            if player == 1 and m != 3:  # 4 - 1 (ouest)
                break
            if player == 2 and m != 2:  # 3 - 1 (sud)
                break
        m = ask_for_direction()
    return m


def possible_move(board, n, directions, player, i, j, m):
    if board[i][j] != player:
        return False
    x, y = directions[m]
    i += x
    j += y
    if i >= n or j >= n or j < 0 or i < 0:
        return True
    return board[i][j] == 0


def move(board, n, directions, player, i, j, m):
    x, y = directions[m]
    board[i][j] = 0
    i += x
    j += y
    if i >= n or j >= n or j < 0 or i < 0:
        return
    board[i][j] = player


def get_other_player(player):
    return 1 if player == 2 else 2


def win(board, n, directions, player):
    nothing_left = True
    for i in range(n):
        for j in range(n):
            if board[i][j] == player:
                nothing_left = False
                for m in range(4):
                    if player == 1 and m == 4:
                        continue
                    if player == 2 and m == 3:
                        continue
                    if possible_move(board, n, directions, player, i, j, m):
                        return False
    return nothing_left


def dodgem(n):
    directions = ((-1, 0), (0, 1), (1, 0), (0, -1))
    board = new_board(n)
    display_board(board, n)
    current_player = 1

    while not win(board, n, directions, current_player):
        print("Au joueur", current_player, "de jouer")

        i, j = select_pawn(board, n, directions, current_player)
        m = select_move(board, n, directions, current_player, i, j)
        while not possible_move(board, n, directions, current_player, i, j, m):
            i, j = select_pawn(board, n, directions, current_player)
            m = select_move(board, n, directions, current_player, i, j)

        move(board, n, directions, current_player, i, j, m)
        display_board(board, n)

        if win(board, n, directions, current_player):
            current_player = get_other_player(current_player)
            break

        current_player = get_other_player(current_player)

    current_player = get_other_player(current_player)
    print("Le gagnant est le joueur", current_player)


dodgem(3)
