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
BLUE = (0, 0, 255)

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
  if currentPiece == '.':
    return []

  if currentPiece.team == 'W':
    enemyTeam = 'B'
  else:
    enemyTeam = 'W'

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
    if mouseY-2 >= 0 and mouseX-1 >= 0 and (gameBoard.board[mouseY-2][mouseX-1] == '.' or (gameBoard.board[mouseY-2][mouseX-1] != '.' and gameBoard.board[mouseY-2][mouseX-1].team == enemyTeam)):
      moveList.append((mouseY-2, mouseX-1))
    if mouseY-2 >= 0 and mouseX+1 <= 7 and (gameBoard.board[mouseY-2][mouseX+1] == '.' or (gameBoard.board[mouseY-2][mouseX+1] != '.' and gameBoard.board[mouseY-2][mouseX+1].team == enemyTeam)):
      moveList.append((mouseY-2, mouseX+1))
    if mouseY+2 <= 7 and mouseX-1 >= 0 and (gameBoard.board[mouseY+2][mouseX-1] == '.' or (gameBoard.board[mouseY+2][mouseX-1] != '.' and gameBoard.board[mouseY+2][mouseX-1].team == enemyTeam)):
      moveList.append((mouseY+2, mouseX-1))
    if mouseY+2 <= 7 and mouseX+1 <= 7 and (gameBoard.board[mouseY+2][mouseX+1] == '.' or (gameBoard.board[mouseY+2][mouseX+1] != '.' and gameBoard.board[mouseY+2][mouseX+1].team == enemyTeam)):
      moveList.append((mouseY+2, mouseX+1))
    if mouseY-1 >= 0 and mouseX-2 >= 0 and (gameBoard.board[mouseY-1][mouseX-2] == '.' or (gameBoard.board[mouseY-1][mouseX-2] != '.' and gameBoard.board[mouseY-1][mouseX-2].team == enemyTeam)):
      moveList.append((mouseY-1, mouseX-2))
    if mouseY+1 <= 7 and mouseX-2 >= 0 and (gameBoard.board[mouseY+1][mouseX-2] == '.' or (gameBoard.board[mouseY+1][mouseX-2] != '.' and gameBoard.board[mouseY+1][mouseX-2].team == enemyTeam)):
      moveList.append((mouseY+1, mouseX-2))
    if mouseY-1 >= 0 and mouseX+2 <= 7 and (gameBoard.board[mouseY-1][mouseX+2] == '.' or (gameBoard.board[mouseY-1][mouseX+2] != '.' and gameBoard.board[mouseY-1][mouseX+2].team == enemyTeam)):
      moveList.append((mouseY-1, mouseX+2))
    if mouseY+1 <= 7 and mouseX+2 <= 7 and (gameBoard.board[mouseY+1][mouseX+2] == '.' or (gameBoard.board[mouseY+1][mouseX+2] != '.' and gameBoard.board[mouseY+1][mouseX+2].team == enemyTeam)):
      moveList.append((mouseY+1, mouseX+2))
  elif currentPiece.symbol == 'B':
    # up to the left direction
    for i in range(1, 8):
      newY = mouseY - i
      newX = mouseX - i
      if newY < 0 or newX < 0:
        break
      elif newY >= 0 and newX >= 0:
        if gameBoard.board[newY][newX] == '.':
          moveList.append((newY, newX))
        elif gameBoard.board[newY][newX] != '.':
          if gameBoard.board[newY][newX].team == enemyTeam:
            moveList.append((newY, newX))
          break
    # up to the right
    for i in range(1, 8):
      newY = mouseY - i
      newX = mouseX + i
      if newY < 0 or newX < 0:
        break
      elif newY >= 0 and newX >= 0:
        if gameBoard.board[newY][newX] == '.':
          moveList.append((newY, newX))
        elif gameBoard.board[newY][newX] != '.':
          if gameBoard.board[newY][newX].team == enemyTeam:
            moveList.append((newY, newX))
          break
    # down to the left
    for i in range(1, 8):
      newY = mouseY + i
      newX = mouseX - i
      if newY < 0 or newX < 0:
        break
      elif newY >= 0 and newX >= 0:
        if gameBoard.board[newY][newX] == '.':
          moveList.append((newY, newX))
        elif gameBoard.board[newY][newX] != '.':
          if gameBoard.board[newY][newX].team == enemyTeam:
            moveList.append((newY, newX))
          break
    # down to the right
    for i in range(1, 8):
      newY = mouseY + i
      newX = mouseX + i
      if newY < 0 or newX < 0:
        break
      elif newY >= 0 and newX >= 0:
        if gameBoard.board[newY][newX] == '.':
          moveList.append((newY, newX))
        elif gameBoard.board[newY][newX] != '.':
          if gameBoard.board[newY][newX].team == enemyTeam:
            moveList.append((newY, newX))
          break
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

def drawPossibleMoves(moveList):
  for (moveX, moveY) in moveList:
    pygame.draw.circle(screen, BLUE, (int(moveY*SQUARE_SIZE + SQUARE_SIZE/2), int(moveX*SQUARE_SIZE + SQUARE_SIZE/2)), 5)
 
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
      #print(moves)
      drawPossibleMoves(moves)

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