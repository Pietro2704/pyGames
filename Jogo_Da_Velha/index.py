def manual():
    print('Bem-vindo ao jogo da velha!')
    print('O jogo é jogado em um tabuleiro 3x3.')
    print('Você é X e seu adversário é O.')
    print('O primeiro jogador a obter 3 em uma linha ganha.')
    print('A tabuleiro é numerado da seguinte forma:')
    print('0, 0 | 0, 1 | 0, 2')
    print('-----+------+-----')
    print('1, 0 | 1, 1 | 1, 2')
    print('-----+------+-----')
    print('2, 0 | 2, 1 | 2, 2')
    print('Para fazer um movimento, insira a linha e a coluna separadas por uma vírgula.')
    print('Por exemplo, para fazer sua jogada no canto superior esquerdo, digite 0, 0.')
    print('Bom jogo!')
    main()
    
def make_tac_toe():
    board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]
    return board
  
def make_move(board, player, position):
    if player == 'X':
        board[position[0]][position[1]] = 'X'
    else:
        board[position[0]][position[1]] = 'O'
    return board
  
def print_board(board):
    for row in board:
        print(row)
        
def check_win(board, player):
  
    for row in board:
        if row[0] == row[1] == row[2] == player:
            return True
          
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] == player:
            return True
          
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
      
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
      
    return False
  
def main():
  
    board = make_tac_toe()
    print_board(board)
    
    while True:
        player = 'X'
        position = input('Enter the position: ').split(',')
        position = [int(position[0]), int(position[1])]
        
        if board[position[0]][position[1]] != ' ':
            print('Invalid position')
            continue
          
        board = make_move(board, player, position)
        print_board(board)
        
        if check_win(board, player):
            print('Player {} wins!'.format(player))
            break
          
        player = 'O'
        position = input('Enter the position: ').split(',')
        position = [int(position[0]), int(position[1])]
        
        if board[position[0]][position[1]] != ' ':
            print('Invalid position')
            continue
          
        board = make_move(board, player, position)
        print_board(board)
        
        if check_win(board, player):
            print('Player {} wins!'.format(player))
            break

manual()