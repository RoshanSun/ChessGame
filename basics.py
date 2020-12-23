# Simple pygame program

# Import and initialize the pygame library
import pygame
import chess_board as cb
pygame.init()

screenHeight = 640
screenWidth = 640

# Set up the drawing window
screen = pygame.display.set_mode([screenHeight, screenWidth])

height = 250
width = 250

def drawBoard():
  # draw light brown rectangles
  for x in range(0,8):
    for y in range(0,8):
      if (x+y)%2 == 1:
        pygame.draw.rect(screen, (185,156,107), (screenWidth/8*x, screenHeight/8*y, screenWidth/8, screenHeight/8))

def drawPieces():
  # draw circles for the pieces for now
  for x in range(1,9):
    for y in [1,2,7,8]:
      colour = (255,0,0)
      if(y==1 or y==8):
        colour = (0,255,0)

      pygame.draw.circle(screen, colour, (int(screenWidth/8*(x-0.5)), int(screenHeight/8*(y-0.5))), 30)


# Run until the user asks to quit
running = True
while running:
    gameBoard = cb.ChessBoard()
    gameBoard.displayBoard()

    # Did the user click the window close button?
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Fill the background with dark brown
    screen.fill((101,67,33))
    
    drawBoard()
    drawPieces()

    # Draw a solid blue circle in the center
    #pygame.draw.circle(screen, (0, 0, 255), (width, height), 75)

    # for event in pygame.event.get():

    #   if event.type == pygame.KEYDOWN:
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