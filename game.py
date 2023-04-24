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
player("x")