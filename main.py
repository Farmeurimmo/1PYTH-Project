def new_board(n):
    return [[0] * n] * n


def display_board(board, n):
    max_length = 0
    for i in range(n):
        text = str(i+1) + (len(str(n)) - len(str(i+1))) * " " + " | "
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
        print(i+1, end=" " + " " * (len(str(n)) - len(str(i+1))))




n = 120
board = new_board(n)

display_board(board, n)