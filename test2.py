import pygame
from pygame.locals import *
import math
import time

pygame.init()
F1image = pygame.image.load("F1image.png")
sportsimage = pygame.image.load("sportsimage.png")
bikeimage = pygame.image.load("bikeimage.png")
muscleimage = pygame.image.load("muscleimage.png")
truckimage = pygame.image.load("truckimage.png")
screen = pygame.display.set_mode((1280,720))
xpos = 280
xpos_2 = 280
ypos = 50
ypos_2 = 85
keys = [False, False, False, False]
keys_2 = [False, False, False, False]
direction = 0
direction_2 = 0
forward = 0
forward_2 = 0

class Background(pygame.sprite.Sprite):
    def __init__(self, image_file, location):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image_file)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location

BackGround = Background('track.png', [0,0])

class Vehicle:
    'Base class for all vehicles (Cars and Motorbikes) in the game'
    vehicleCount = 0

    def __init__(self, max_speed, acceleration, turning_radius, image):
        pygame.sprite.Sprite.__init__(self)
        self.max_speed = max_speed
        self.acceleration = acceleration
        self.turning_radius = turning_radius
        self.image = image
        self.rect = self.image.get_rect()
        Vehicle.vehicleCount  = Vehicle.vehicleCount + 1


    def displayAmount():
        print ("Total number of Vehicle enteries: ", Vehicle.vehicleCount)

    def displayVehicle(self):
        print ("max speed: ", self.max_speed, "acceleration: ", self.acceleration, "turning radius: ", self.turning_radius)

    def checkCollision(self, sprite1, sprite2):
        col = pygame.sprite.collide_rect(sprite1, sprite2)
        if col == True:
            print ("True")

F1 = Vehicle(5.0, 0.1, 2.84, F1image)
sportscar = Vehicle(4.5, 0.2, 2.01, sportsimage)
bike = Vehicle(4.0, 0.15, 2.64, bikeimage)
musclecar = Vehicle(3.5, 0.25, 1.76, muscleimage)
truck = Vehicle(3.0, 0.3, 1.20, truckimage)

print (F1.max_speed)

player1choice = input("Input player 1 choice").lower()
player2choice = input("Input player 2 choice").lower()

if player1choice == ("f1"):
    choice1 = F1
elif player1choice == ("sports"):
    choice1 = sportscar
elif player1choice == ("muscle"):
    choice1 = musclecar
elif player1choice == ("truck"):
    choice1 = truck
else:
    choice1 = bike

if player2choice == ("f1"):
    choice2 = F1
elif player2choice == ("sports"):
    choice2 = sportscar
elif player2choice == ("muscle"):
    choice2 = musclecar
elif player2choice == ("truck"):
    choice2 = truck
else:
    choice2 = bike

running = True
while running:
    pygame.display.set_caption("Speed Wars")
    WHITE = (255, 255, 255)
    screen.fill(WHITE)
    screen.blit(BackGround.image, BackGround.rect)

    #Vehicle 1
    if keys[0] == True:
        direction += (choice1).turning_radius
    if keys[1] == True:
        direction -= (choice1).turning_radius
    if keys[2] == True and forward <= (choice1).max_speed:
        forward += (choice1).acceleration
    if keys[3] == True and forward >= 0:
        forward -= (choice1).acceleration

    #Vehicle 2
    if keys_2[0] == True:
        direction_2 += (choice2).turning_radius
    if keys_2[1] == True:
        direction_2 -= (choice2).turning_radius
    if keys_2[2] == True and forward_2 <= (choice2).max_speed:
        forward_2 += (choice2).acceleration
    if keys_2[3] == True and forward_2 >= 0:
        forward_2 -= (choice2).acceleration

    movex = math.cos(direction / 57.29) * forward
    movey = math.sin(direction / 57.29) * forward
    xpos += movex
    ypos -= movey

    movex_2 = math.cos(direction_2 / 57.29) * forward_2
    movey_2 = math.sin(direction_2 / 57.29) * forward_2
    xpos_2 += movex_2
    ypos_2 -= movey_2

    rotation = pygame.transform.rotate((choice1).image, direction)
    rotation_2 = pygame.transform.rotate((choice2).image, direction_2)
    screen.blit(rotation, (xpos, ypos))
    screen.blit(rotation_2, (xpos_2, ypos_2))
    pygame.display.flip()
    time.sleep(0.01)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit(0)

        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                keys[0] = True
            elif event.key == K_RIGHT:
                keys[1] = True
            elif event.key == K_UP:
                keys[2] = True
            elif event.key == K_DOWN:
                keys[3] = True

            if event.key == K_a:
                keys_2[0] = True
            elif event.key == K_d:
                keys_2[1] = True
            elif event.key == K_w:
                keys_2[2] = True
            elif event.key == K_s:
                keys_2[3] = True

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                keys[0] = False
            elif event.key == pygame.K_RIGHT:
                keys[1] = False
            elif event.key == pygame.K_UP:
                keys[2] = False
            elif event.key == pygame.K_DOWN:
                keys[3] = False

            if event.key == pygame.K_a:
                keys_2[0] = False
            elif event.key == pygame.K_d:
                keys_2[1] = False
            elif event.key == pygame.K_w:
                keys_2[2] = False
            elif event.key == pygame.K_s:
                keys_2[3] = False

        #Collision detection
        (choice1).checkCollision((choice2).image, (choice1).image)