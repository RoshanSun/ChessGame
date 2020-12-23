class ChessBoard:
  def __init__(self):
    self.board = self.createBoard()

  def createBoard(self):
    board = [['.']*8 for _ in range(8)]

    board[0][0] = 'BR1'
    board[0][1] = 'BKn1'
    board[0][2] = 'BB1'
    board[0][3] = 'BQ'
    board[0][4] = 'BK'
    board[0][5] = 'BB2'
    board[0][6] = 'BKn2'
    board[0][7] = 'BR2'

    for i in range(0,8):
      board[1][i] = 'BP' + str(i+1)

    board[7][0] = 'WR1'
    board[7][1] = 'WKn1'
    board[7][2] = 'WB1'
    board[7][3] = 'WQ'
    board[7][4] = 'WK'
    board[7][5] = 'WB2'
    board[7][6] = 'WKn2'
    board[7][7] = 'WR2'

    for i in range(0,8):
      board[6][i] = 'WP' + str(i+1)

    return board
  
  def displayBoard(self):
    for i in range(8):
      for j in range(8):
        print(self.board[i][j], end=' ')
      print()

if __name__ == '__main__':
  gameBoard = ChessBoard()
  gameBoard.displayBoard()