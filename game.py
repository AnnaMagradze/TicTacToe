def print_field(board, num):
    print('-------')
    for i in range (9):
        if i % 3 == 0 :
            print('|', end="")
        print(board[i//3][i % 3], end='|')
        if i % 3 == 2:
            print()
            print('-' * 7)


board=[
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
    ]


print_field(board, False)