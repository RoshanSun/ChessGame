import pygame

class Piece(pygame.sprite.Sprite):
  def __init__(self, x, y, team):
    super().__init__()
    self.image = None

    self.xPos = x
    self.yPos = y
    self.team = team
    self.symbol = None

  def printPiece(self):
    print("The symbol of this piece is: " + self.symbol)

class Pawn(Piece):
  def __init__(self, x, y, team):
    Piece.__init__(self, x , y, team)
    self.symbol = 'P'
    if self.team == 'W':
      self.image = pygame.image.load('pieceSprites/whitePawn.png')
    else:
      self.image = pygame.image.load('pieceSprites/blackPawn.png')

class Knight(Piece):
  def __init__(self, x, y, team):
    Piece.__init__(self, x , y, team)
    self.symbol = 'Kn'
    if self.team == 'W':
      self.image = pygame.image.load('pieceSprites/whiteKnight.png')
    else:
      self.image = pygame.image.load('pieceSprites/blackKnight.png')

class Bishop(Piece):
  def __init__(self, x, y, team):
    Piece.__init__(self, x , y, team)
    self.symbol = 'B'
    if self.team == 'W':
      self.image = pygame.image.load('pieceSprites/whiteBishop.png')
    else:
      self.image = pygame.image.load('pieceSprites/blackBishop.png')

class Rook(Piece):
  def __init__(self, x, y, team):
    Piece.__init__(self, x , y, team)
    self.symbol = 'R'
    if self.team == 'W':
      self.image = pygame.image.load('pieceSprites/whiteRook.png')
    else:
      self.image = pygame.image.load('pieceSprites/blackRook.png')

class Queen(Piece):
  def __init__(self, x, y, team):
    Piece.__init__(self, x , y, team)
    self.symbol = 'Q'
    if self.team == 'W':
      self.image = pygame.image.load('pieceSprites/whiteQueen.png')
    else:
      self.image = pygame.image.load('pieceSprites/blackQueen.png')

class King(Piece):
  def __init__(self, x, y, team):
    Piece.__init__(self, x , y, team)
    self.symbol = 'K'
    if self.team == 'W':
      self.image = pygame.image.load('pieceSprites/whiteKing.png')
    else:
      self.image = pygame.image.load('pieceSprites/blackKing.png')

if __name__ == '__main__':
  pygame.init()
  screen = pygame.display.set_mode([800, 800])
  running = True

  whitePawn = Pawn(0, 0, 'W')
  whiteRook = Rook(0, 0, 'W')
  whiteKnight = Knight(0, 0, 'W')
  whiteBishop = Bishop(0, 0, 'W')
  whiteQueen = Queen(0, 0, 'W')
  whiteKing = King(0, 0, 'W')

  blackPawn = Pawn(400, 400, 'B')
  blackRook = Rook(0, 0, 'B')
  blackKnight = Knight(0, 0, 'B')
  blackBishop = Bishop(0, 0, 'B')
  blackQueen = Queen(0, 0, 'B')
  blackKing = King(0, 0, 'B')

  print(whitePawn.image.get_rect().width)
  print(whitePawn.image.get_rect().height)

  print(blackPawn.image.get_rect().width)
  print(blackPawn.image.get_rect().height)

  while running:
    screen.fill((101,67,33))

    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        running = False
    
    for i in range(8):
      screen.blit(whitePawn.image, (i*100+5, 600))
      screen.blit(blackPawn.image, (i*100+5, 100))

    screen.blit(blackRook.image, (0, 0))
    screen.blit(blackRook.image, (700, 0))
    screen.blit(blackKnight.image, (600, 0))
    screen.blit(blackKnight.image, (100, 0))
    screen.blit(blackBishop.image, (500, 0))
    screen.blit(blackBishop.image, (200, 0))
    screen.blit(blackQueen.image, (300, 0))
    screen.blit(blackKing.image, (400, 0))

    screen.blit(whiteRook.image, (0, 700))
    screen.blit(whiteRook.image, (700, 700))
    screen.blit(whiteKnight.image, (600, 700))
    screen.blit(whiteKnight.image, (100, 700))
    screen.blit(whiteBishop.image, (500, 700))
    screen.blit(whiteBishop.image, (200, 700))
    screen.blit(whiteQueen.image, (300, 700))
    screen.blit(whiteKing.image, (400, 700))

    pygame.display.flip()
    
  pygame.quit()