def board(game_board):
    for _ in range(0, 9, 3):
        print('+' + '-' * 7 + '+' + '-' * 7 + '+' + '-' * 7 + '+')
        print('|\t|\t|\t|')
        print(f'|{game_board[_]:>4}\t|{game_board[_+1]:>4}\t|{game_board[_+2]:>4}\t|')
        print('|\t|\t|\t|')
        print('+' + '-' * 7 + '+' + '-' * 7 + '+' + '-' * 7 + '+')

movimiento = 0
game = list(range(1,10)) # 1 - 9
while True:
    board(game)
    movimiento = int(input('Ingresa tu movimiento: '))
    if movimiento in game:
        print('existe')
        game[movimiento-1] = "x" 
    elif 0 < movimiento < 10:
        print('Casilla ocupada')
