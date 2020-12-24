import pieces as p

class ChessBoard:
  def __init__(self):
    self.board = self.createBoard()

  def createBoard(self):
    board = [['.']*8 for _ in range(8)]

    board[0][0] = p.Rook(0, 0, 'B')
    board[0][1] = p.Knight(0, 1, 'B')
    board[0][2] = p.Bishop(0, 2, 'B')
    board[0][3] = p.Queen(0, 3, 'B')
    board[0][4] = p.King(0, 4, 'B')
    board[0][5] = p.Bishop(0, 5, 'B')
    board[0][6] = p.Knight(0, 6, 'B')
    board[0][7] = p.Rook(0, 7, 'B')

    for i in range(0,8):
      board[1][i] = p.Pawn(1, i, 'B')

    board[7][0] = p.Rook(7, 0, 'W')
    board[7][1] = p.Knight(7, 1, 'W')
    board[7][2] = p.Bishop(7, 2, 'W')
    board[7][3] = p.Queen(7, 3, 'W')
    board[7][4] = p.King(7, 4, 'W')
    board[7][5] = p.Bishop(7, 5, 'W')
    board[7][6] = p.Knight(7, 6, 'W')
    board[7][7] = p.Rook(7, 7, 'W')

    for i in range(0,8):
      board[6][i] = p.Pawn(6, i, 'W')

    return board
  
  def displayBoard(self):
    for i in range(8):
      for j in range(8):
        if (self.board[i][j] != '.'):
          print(self.board[i][j].symbol, end=' ')
        else:
          print('.', end=' ')
      print()

if __name__ == '__main__':
  gameBoard = ChessBoard()
  gameBoard.displayBoard()