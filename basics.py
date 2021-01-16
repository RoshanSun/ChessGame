# Simple pygame program

# Import and initialize the pygame library
import pygame
import chess_board as cb
import pieces as p
pygame.init()

# Constants
BOARD_SIDE = 800
NUM_SQUARES = 8
SQUARE_SIZE = BOARD_SIDE / NUM_SQUARES
LIGHT_BROWN = (185, 156, 107)
DARK_BROWN = (101, 67, 33)
RED = (255, 0, 0)

# Set up the drawing window
screen = pygame.display.set_mode([BOARD_SIDE, BOARD_SIDE])

height = 250
width = 250

def drawBoard():
  # draw light brown rectangles
  for x in range(0,8):
    for y in range(0,8):
      if (x+y)%2 == 1:
        pygame.draw.rect(screen, LIGHT_BROWN, (SQUARE_SIZE*x, SQUARE_SIZE*y, SQUARE_SIZE, SQUARE_SIZE))

def drawPieces(gameBoard):
  for x in range(len(gameBoard.board)):
    for y in range(len(gameBoard.board[x])):
      if(gameBoard.board[x][y] != '.'):
        screen.blit(gameBoard.board[x][y].image, (y*SQUARE_SIZE, x*SQUARE_SIZE))

def highlightSelectedPiece(mouseX, mouseY):
  # draw the square being highlighted
  if (mouseX != -1 and mouseY != -1 and gameBoard.board[mouseY][mouseX] != '.'):
    pygame.draw.rect(screen, RED, (mouseX*SQUARE_SIZE, mouseY*SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE), 2)
    #print(gameBoard.board[mouseY][mouseX].xPos, gameBoard.board[mouseY][mouseX].yPos)

def findMoves(mouseX, mouseY):
  moveList = []
  currentPiece = gameBoard.board[mouseY][mouseX]
  if currentPiece.team == 'W':
    enemyTeam = 'B'
  else:
    enemyTeam = 'W'
  if currentPiece == '.':
    return []

  # moves for pawns
  if currentPiece.symbol == 'P':
    if currentPiece.team == 'W':
      # not blocked infront
      if gameBoard.board[mouseY-1][mouseX] == '.':
        moveList.append((mouseY-1, mouseX))
        # starting pawn
        if currentPiece.xPos == 6 and gameBoard.board[mouseY-2][mouseX] == '.':
          moveList.append((mouseY-2, mouseX))
      # take piece moves
      if mouseX-1 >= 0 and gameBoard.board[mouseY-1][mouseX-1] != '.' and gameBoard.board[mouseY+1][mouseX-1].team == enemyTeam:
        moveList.append((mouseY-1, mouseX-1))
      if mouseX+1 <= 7 and gameBoard.board[mouseY-1][mouseX+1] != '.' and gameBoard.board[mouseY+1][mouseX-1].team == enemyTeam:
        moveList.append((mouseY-1, mouseX+1))
    elif currentPiece.team == 'B':
      if gameBoard.board[mouseY+1][mouseX] == '.':
        moveList.append((mouseY+1, mouseX))
        # starting pawn
        if currentPiece.xPos == 1 and gameBoard.board[mouseY+2][mouseX] == '.':
          moveList.append((mouseY+2, mouseX))
      # take piece moves
      if mouseX-1 >= 0 and gameBoard.board[mouseY+1][mouseX-1] != '.' and gameBoard.board[mouseY+1][mouseX-1].team == enemyTeam:
        moveList.append((mouseY+1, mouseX-1))
      if mouseX+1 <= 7 and gameBoard.board[mouseY+1][mouseX+1] != '.' and gameBoard.board[mouseY+1][mouseX-1].team == enemyTeam:
        moveList.append((mouseY+1, mouseX+1))
  elif currentPiece.symbol == 'Kn':
    # POSSIBLE KNIGHT MOVES
    # Y - 2, X + 1
    # Y - 2, X - 1
    # Y + 2, X + 1
    # Y + 2, X - 1
    # Y + 1, X - 2
    # Y - 1, X - 2
    # Y + 1, X + 2
    # Y - 1, X + 2

    if currentPiece.team == 'W':
      pass
    elif currentPiece == 'B':
      pass
  elif currentPiece.symbol == 'B':
    if currentPiece.team == 'W':
      pass
    elif currentPiece == 'B':
      pass
  elif currentPiece.symbol == 'R':
    if currentPiece.team == 'W':
      pass
    elif currentPiece == 'B':
      pass
  elif currentPiece.symbol == 'Q':
    if currentPiece.team == 'W':
      pass
    elif currentPiece == 'B':
      pass
  elif currentPiece.symbol == 'K':
    if currentPiece.team == 'W':
      pass
    elif currentPiece == 'B':
      pass
  
  return moveList

# Run until the user asks to quit
running = True
mouseX = mouseY = boardX = boardY = -1

while running:
    gameBoard = cb.ChessBoard()
    #gameBoard.displayBoard()

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with dark brown
    screen.fill(DARK_BROWN)
    
    drawBoard()
    drawPieces(gameBoard)

    # Draw a solid blue circle in the center
    #pygame.draw.circle(screen, (0, 0, 255), (width, height), 75)

    for event in pygame.event.get():
      if event.type == pygame.MOUSEBUTTONDOWN:
        mouseX, mouseY = pygame.mouse.get_pos()
        boardX = int(mouseX/SQUARE_SIZE)
        boardY = int(mouseY/SQUARE_SIZE)

    highlightSelectedPiece(boardX, boardY)
    moves = findMoves(boardX, boardY)
    if moves != []:
      print(moves)

    #     if event.key == pygame.K_LEFT:
    #       width -= 1
    #     if event.key == pygame.K_RIGHT:
    #       width += 1
    #     if event.key == pygame.K_UP:
    #       height -= 1
    #     if event.key == pygame.K_DOWN:
    #       height += 1

    # keys=pygame.key.get_pressed()
    # if keys[K_LEFT]:
    #   width -= 1
    # if keys[K_RIGHT]:
    #   width += 1
    # if keys[K_UP]:
    #   height -= 1
    # if keys[K_DOWN]:
    #   height += 1

    # Flip the display
    pygame.display.flip()

# Done! Time to quit.
pygame.quit()
print("done")