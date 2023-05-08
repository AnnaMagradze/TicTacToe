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


def win(board):
    for i in range(3):
        if board[0][i] == board[1][i] and board[0][i] == board[2][i] and board[0][i] != ' ':
            return board[1][i]
        if board[i][0] == board[i][1] and board[i][0] == board[i][2] and board[i][0] != ' ':
            return board[i][1]
    if ((board[0][0] == board[1][1] == board[2][2]) or (board[2][0] == board[1][1] == board[0][2])) and board[1][1] != ' ':
        return board[1][1]
    for stroke in board:
        for cell in stroke:
            if cell==" ":
                return ""
    return "Ничья"



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
while win(board)=='':
    player(symbols[ counter% 2])
    counter+= 1
print_field(board, False)
if win(board)=="Ничья":
    print('e dfc у вас ничья!')
else:
     print("поздрашиляем! вы выиграли:",win(board))
