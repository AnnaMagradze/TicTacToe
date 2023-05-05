def print_field(board, num):
    print('-------')
    for i in range (9):
        if i % 3 == 0 :
            print('|', end="")
        if board[i//3][i%3]==' 'and num:
            print (i+1,end="|")
        else:
            print(board[i//3][i % 3], end='|')
        if i % 3 == 2:
            print()
            print('-' * 7)


def game_continue(board):
    for i in range(3):
        if board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] != ' ':
            return False
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] != ' ':
            return False
    if ((board[0][0] == board[1][1] == board[2][2]) or (board[2][0] == board[1][1] == board[0][2])) and board[1][1] != ' ':
        return False
    return True


def player(symdol):
    print_field(board,True)
    number =int(input(" введите номер ячейки: "))-1
    while number< 0 or number>8 or board[number//3][number % 3]!=" ":
        print('ошибка: нельзя записать в данную ячейку!')
        number = int(input(" введите номер ячейки: ")) - 1
    board[number // 3][number % 3] = symdol


board=[
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
    ]
symbols = ['x', 'o']
counter= 0
while game_continue(board):
    player(symbols[ counter% 2])
print_field(board, False)
