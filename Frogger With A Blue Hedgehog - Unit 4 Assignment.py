#**********************************************************
# Program	:  Unit 4 Assignment - Game Assignment
# Author	:  Scott Reader
# Due Date	:  Friday May 4th 2018
# Description	:  Sonic the Hedgehog Frogger
#**********************************************************

import pygame
import sys
import random

from pygame.locals import *
pygame.init()

WINDOW = pygame.display.set_mode((738, 554))
pygame.display.set_caption("Frogger With A Blue Hedgehog")


#Put any colours you create here -- this code only needs to run once

RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

#Assorted variables
wincounter = 0
game = 3

whiteCE = 1
redCE = 1
orangeCE = 1
greenCE = 1
purpleCE = 1
blueCE = 1
lblueCE = 1

car1frame1 = -40
car1frame2 = -80
car1frame3 = 380
car1frame4 = 340

car2frame1 = -40
car2frame2 = -82
car2frame3 = 380
car2frame4 = 338

car3frame1 = 780
car3frame2 = 820
car3frame3 = 340
car3frame4 = 380

car4frame1 = 778
car4frame2 = 820
car4frame3 = 379
car4frame4 = 337

log1frame1 = -40
log1frame2 = -80
log1frame3 = 340
log1frame4 = 380

log2frame1 = 780
log2frame2 = 820
log2frame3 = 340
log2frame4 = 380

log3frame1 = -40
log3frame2 = -80
log3frame3 = 340
log3frame4 = 380

log4frame1 = 780
log4frame2 = 820
log4frame3 = 340
log4frame4 = 380

#Images
picture = pygame.image.load("Sonic.exe.png")
picture2 = pygame.image.load("Pointing Sonic.png")
picture3 = pygame.image.load("Pointing Sonic.png")
Player = pygame.image.load("Player Sonic.png")
log1 = pygame.image.load("Water Sonic Left.png")
log2 = pygame.image.load("Water Sonic Right.png")
log3 = pygame.image.load("Water Super Sonic Left.png")
log4 = pygame.image.load("Water Super Sonic Right.png")
car1 = pygame.image.load("Running Sonic.png")
car2 = pygame.image.load("Flying Super Sonic.png")
car3 = pygame.image.load("Rolling Sonic Right.png")
car4 = pygame.image.load("Rolling Super Sonic Right.png")
background = pygame.image.load("Frogger Background.gif")
img = pygame.image.load("Chaos Emeralds.gif")
img2 = pygame.image.load("Super Sonic.gif")

#Fonts
chiller = pygame.font.SysFont("Chiller", 90, False, False)
word = "Game Over"

ArialR = pygame.font.SysFont("Arial Rounded MT Bold", 40, False, False)
replay = "Play Again"
Quit = "Quit"
livecounter = "Lives: " + str(game)
CEtext = "Chaos Emeralds: " + str(wincounter)


Broadway = pygame.font.SysFont("Broadway", 40, False, False)
Win = "YOU WIN!"

text = chiller.render(word, True, RED) 
text2 = ArialR.render(replay, True, WHITE) 
text3 = ArialR.render(Quit, True, WHITE)
text4 = Broadway.render(Win, True, WHITE)
live = ArialR.render(livecounter, True, WHITE)
CEcounter = ArialR.render(CEtext, True, WHITE)

#Sprite Animation
frame = 0

#Sprite Movement
playerx = 354
playery = 468

#Location Variables
Px = 525
Py = 282
Px2 = 600
Py2 = 175


FPS = 60
fpsClock = pygame.time.Clock()

#Game Music
pygame.mixer.init()

pygame.mixer.music.load("Green Hill Zone Theme.mp3")

pygame.mixer.music.play(-1, 0)

while True:

   for event in pygame.event.get():

      if event.type == QUIT:
         pygame.quit()
         sys.exit()

      # Key Presses
      if game != 0 and wincounter!= 7:
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
               if playery <= 468 and playery >= 244 and playerx != 18:
                  playerx = playerx - 56
            if event.key == pygame.K_RIGHT:
               if playery <= 468 and playery >= 244 and playerx != 690:
                  playerx = playerx + 56
            if event.key == pygame.K_UP:
               if playery != 20:
                  playery = playery - 56
            if event.key == pygame.K_DOWN:
               if playery != 468:
                  playery = playery + 56

#Win menu pointer
      if wincounter == 7:
         WINDOW.blit(picture3, (Px2,Py2))
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
               Px2 = 520
               Py2 = 225
            if event.key == pygame.K_UP:
               Px2 = 600
               Py2 = 175
            if event.key == pygame.K_RETURN:
               while Px2 == 520 and Py2 == 225:
                  pygame.quit()
                  sys.exit()
               while Px2 == 600 and Py2 == 175:
                  wincounter = 0
                  game = 3
                  whiteCE = 1
                  redCE = 1
                  orangeCE = 1
                  greenCE = 1
                  purpleCE = 1
                  blueCE = 1
                  lblueCE = 1
                  break
#Game Over Menu pointer
      if game <= 0:
         WINDOW.blit(picture3, (Px,Py))
         if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
               Px = 425
               Py = 332
            if event.key == pygame.K_UP:
               Px = 525
               Py = 282
            if event.key == pygame.K_RETURN:
               while Px == 425 and Py == 332:
                  pygame.quit()
                  sys.exit()
               while Px == 525 and Py == 282:
                  wincounter = 0
                  game = 3
                  whiteCE = 1
                  redCE = 1
                  orangeCE = 1
                  greenCE = 1
                  purpleCE = 1
                  blueCE = 1
                  lblueCE = 1
                  break


        #The shapes you draw go here
        #Note: make sure to will the screen first, otherwise you will fill over your other images

   WINDOW.fill(BLACK)

#Main game screen
   if game <= 3 and game > 0 and wincounter != 7:
      WINDOW.blit(background, (0,0))
      pygame.draw.line(WINDOW, WHITE, (0, 504), (738, 504), 3)
      if whiteCE == 1:
         WINDOW.blit(img, (10, 25), (260, 170, 50, 50))
      if purpleCE == 1:
         WINDOW.blit(img, (122, 25), (210, 170, 50, 50))   
      if greenCE == 1:
         WINDOW.blit(img, (234, 25), (160, 170, 50, 50))
      if orangeCE == 1:
         WINDOW.blit(img, (346, 25), (110, 170, 50, 50))   
      if blueCE == 1:
         WINDOW.blit(img, (458, 25), (60, 170, 50, 50))
      if redCE == 1:
         WINDOW.blit(img, (567, 25), (5, 170, 50, 50))
      if lblueCE == 1:
         WINDOW.blit(img, (675, 20), (260, 120, 50, 50))
      livecounter = "Lives: " + str(game)
      live = ArialR.render(livecounter, True, WHITE)
      WINDOW.blit(live, (20,515))
#Chaos Emerald Collision
      if playerx >= 10 and playerx <=60 and playery >=15 and playery <= 65 and whiteCE != 0: 
         wincounter = wincounter + 1
         playerx = 354
         playery = 468
         whiteCE = 0
      if playerx >= 122 and playerx <= 172 and playery >=15 and playery <= 65 and purpleCE != 0: 
         wincounter = wincounter + 1
         playerx = 354
         playery = 468
         purpleCE = 0
      if playerx >= 234 and playerx <= 284 and playery >=15 and playery <= 65 and greenCE != 0: 
         wincounter = wincounter + 1
         playerx = 354
         playery = 468
         greenCE = 0
      if playerx >= 346 and playerx <= 396 and playery >=15 and playery <= 65 and orangeCE != 0: 
         wincounter = wincounter + 1
         playerx = 354
         playery = 468
         orangeCE = 0
      if playerx >= 458 and playerx <= 508 and playery >=15 and playery <= 65 and blueCE != 0: 
         wincounter = wincounter + 1
         playerx = 354
         playery = 468
         blueCE = 0
      if playerx >= 567 and playerx <= 617 and playery >=15 and playery <= 65 and redCE != 0: 
         wincounter = wincounter + 1
         playerx = 354
         playery = 468
         redCE = 0
      if playerx >= 675 and playerx <= 725 and playery >=15 and playery <= 65 and lblueCE != 0: 
         wincounter = wincounter + 1
         playerx = 354
         playery = 468
         lblueCE = 0
      CEtext = "Chaos Emeralds: " + str(wincounter)
      CEcounter = ArialR.render(CEtext, True, WHITE)
      WINDOW.blit(CEcounter, (450,515))
      
# Normal Sonic Obstacles      
      if wincounter != 6:
#Middle row of river
         WINDOW.blit(log1, (log1frame1, 132),(0,0,47.5,26))
         log1frame1 = log1frame1 + 2
         if log1frame1 == 760:
            log1frame1 = -50
         WINDOW.blit(log1, (log1frame2, 132),(0,0,47.5,26))
         log1frame2 = log1frame2 + 2
         if log1frame2 == 760:
            log1frame2 = -50
         WINDOW.blit(log1, (log1frame4, 132),(0,0,47.5,26))
         log1frame4 = log1frame4 + 2
         if log1frame4 == 760:
            log1frame4 = -50
         WINDOW.blit(log1, (log1frame3, 132),(0,0,47.5,26))
         log1frame3 = log1frame3 + 2
         if log1frame3 == 760:
            log1frame3 = -50
#Top row of river
         WINDOW.blit(log2, (log2frame1, 76),(0,0,47.5,26))
         log2frame1 = log2frame1 - 2
         if log2frame1 == -40:
            log2frame1 = 780
         WINDOW.blit(log2, (log2frame2, 76),(0,0,47.5,26))
         log2frame2 = log2frame2 - 2
         if log2frame2 == -40:
            log2frame2 = 780
         WINDOW.blit(log2, (log2frame3, 76),(0,0,47.5,26))
         log2frame3 = log2frame3 - 2
         if log2frame3 == -40:
            log2frame3 = 780
         WINDOW.blit(log2, (log2frame4, 76),(0,0,47.5,26))
         log2frame4 = log2frame4 - 2
         if log2frame4 == -40:
            log2frame4 = 780
#Bottom row of river
         WINDOW.blit(log2, (log2frame1, 188),(0,0,47.5,26))
         log2frame1 = log2frame1 - 2
         if log2frame1 == -40:
            log2frame1 = 780
         WINDOW.blit(log2, (log2frame2, 188),(0,0,47.5,26))
         log2frame2 = log2frame2 - 2
         if log2frame2 == -40:
            log2frame2 = 780
         WINDOW.blit(log2, (log2frame3, 188),(0,0,47.5,26))
         log2frame3 = log2frame3 - 2
         if log2frame3 == -40:
            log2frame3 = 780
         WINDOW.blit(log2, (log2frame4, 188),(0,0,47.5,26))
         log2frame4 = log2frame4 - 2
         if log2frame4 == -40:
            log2frame4 = 780

#Road objects
#Top row of road
         WINDOW.blit(car1, (car1frame1, 300),(0,0,31.5,36))
         car1frame1 = car1frame1 + 5
         if car1frame1 == 790:
            car1frame1 = -40
         WINDOW.blit(car1, (car1frame2, 300),(0,0,31.5,36))
         car1frame2 = car1frame2 + 5
         if car1frame2 == 790:
            car1frame2 = -40
         WINDOW.blit(car1, (car1frame3, 300),(0,0,31.5,36))
         car1frame3 = car1frame3 + 5
         if car1frame3 == 790:
            car1frame3 = -40
         WINDOW.blit(car1, (car1frame4, 300),(0,0,31.5,36))
         car1frame4 = car1frame4 + 5
         if car1frame4 == 790:
            car1frame4 = -40
#Bottom row of road
         WINDOW.blit(car1, (car1frame1, 412),(0,0,31.5,36))
         car1frame1 = car1frame1 + 5
         if car1frame1 == 790:
            car1frame1 = -40
         WINDOW.blit(car1, (car1frame2, 412),(0,0,31.5,36))
         car1frame2 = car1frame2 + 5
         if car1frame2 == 790:
            car1frame2 = -40
         WINDOW.blit(car1, (car1frame3, 412),(0,0,31.5,36))
         car1frame3 = car1frame3 + 5
         if car1frame3 == 790:
            car1frame3 = -40
         WINDOW.blit(car1, (car1frame4, 412),(0,0,31.5,36))
         car1frame4 = car1frame4 + 5
         if car1frame4 == 790:
            car1frame4 = -40
#Middle row of road
         WINDOW.blit(car3, (car3frame1, 356),(0,0,31.5,36))
         car3frame1 = car3frame1 - 5
         if car3frame1 == -40:
            car3frame1 = 780
         WINDOW.blit(car3, (car3frame2, 356),(0,0,31.5,36))
         car3frame2 = car3frame2 - 5
         if car3frame2 == -40:
            car3frame2 = 780
         WINDOW.blit(car3, (car3frame3, 356),(0,0,31.5,36))
         car3frame3 = car3frame3 - 5
         if car3frame3 == -40:
            car3frame3 = 780
         WINDOW.blit(car3, (car3frame4, 356),(0,0,31.5,36))
         car3frame4 = car3frame4 - 5
         if car3frame4 == -40:
            car3frame4 = 780

#Collisions with road objects
         if playery == 412 and playerx >= car1frame1 and playerx <= car1frame1 + 31.5 or playery == 300 and playerx >= car1frame1 and playerx <= car1frame1 + 31.5:
            game = game - 1
            playerx = 354
            playery = 468
         if playery == 412 and playerx >= car1frame2 and playerx <= car1frame2 + 31.5 or playery == 300 and playerx >= car1frame2 and playerx <= car1frame2 + 31.5:
            game = game - 1
            playerx = 354
            playery = 468
         if playery == 412 and playerx >= car1frame3 and playerx <= car1frame3 + 31.5 or playery == 300 and playerx >= car1frame3 and playerx <= car1frame3 + 31.5:
            game = game - 1
            playerx = 354
            playery = 468
         if playery == 412 and playerx >= car1frame4 and playerx <= car1frame4 + 31.5 or playery == 300 and playerx >= car1frame4 and playerx <= car1frame4 + 31.5:
            game = game - 1
            playerx = 354
            playery = 468
         if playery == 356 and playerx >= car3frame1 and playerx <= car3frame1 + 31.5:
            game = game - 1
            playerx = 354
            playery = 468
         if playery == 356 and playerx >= car3frame2 and playerx <= car3frame2 + 31.5:
            game = game - 1
            playerx = 354
            playery = 468
         if playery == 356 and playerx >= car3frame3 and playerx <= car3frame3 + 31.5:
            game = game - 1
            playerx = 354
            playery = 468
         if playery == 356 and playerx >= car3frame4 and playerx <= car3frame4 + 31.5:
            game = game - 1
            playerx = 354
            playery = 468
# Water & Log Collision
         if playery == 76 and playerx >= log2frame1 and playerx <= log2frame1 + 47.5 and playerx > -30 and playerx < 730 or playery == 188 and playerx >= log2frame1 and playerx <= log2frame1 + 47.5 and playerx > -30 and playerx < 730:
            playerx = playerx - 4
         elif playery == 76 and playerx >= log2frame2 and playerx <= log2frame2 + 47.5 and playerx > -30 and playerx < 730 or playery == 188 and playerx >= log2frame2 and playerx <= log2frame2 + 47.5 and playerx > -30 and playerx < 730:
            playerx = playerx - 4
         elif playery == 76 and playerx >= log2frame3 and playerx <= log2frame3 + 47.5 and playerx > -30 and playerx < 730 or playery == 188 and playerx >= log2frame3 and playerx <= log2frame3 + 47.5 and playerx > -30 and playerx < 730:
            playerx = playerx - 4
         elif playery == 76 and playerx >= log2frame4 and playerx <= log2frame4 + 47.5 and playerx > -30 and playerx < 730 or playery == 188 and playerx >= log2frame4 and playerx <= log2frame4 + 47.5 and playerx > -30 and playerx < 730:
            playerx = playerx - 4
         elif playery == 132 and playerx >= log1frame1 and playerx <= log1frame1 + 47.5 and playerx > -30 and playerx < 730:
            playerx = playerx + 2
         elif playery == 132 and playerx >= log1frame2 and playerx <= log1frame2 + 47.5 and playerx > -30 and playerx < 730:
            playerx = playerx + 2
         elif playery == 132 and playerx >= log1frame3 and playerx <= log1frame3 + 47.5 and playerx > -30 and playerx < 730:
            playerx = playerx + 2
         elif playery == 132 and playerx >= log1frame4 and playerx <= log1frame4 + 47.5 and playerx > -30 and playerx < 730:
            playerx = playerx + 2
         elif playerx >= -30 and playerx <= 730 and playery <= 188 and playery >= 76:
            game = game - 1
            playerx = 354
            playery = 468

#Super Sonic Obstacles
      if wincounter == 6:
#Middle row of river
         WINDOW.blit(log3, (log3frame1, 132),(0,0,49,26.5))
         log3frame1 = log3frame1 + 5
         if log3frame1 == 790:
            log3frame1 = -40
         WINDOW.blit(log3, (log3frame2, 132),(0,0,49,26.5))
         log3frame2 = log3frame2 + 5
         if log3frame2 == 790:
            log3frame2 = -40
         WINDOW.blit(log3, (log3frame4, 132),(0,0,49,26.5))
         log3frame4 = log3frame4 + 5
         if log3frame4 == 790:
            log3frame4 = -40
         WINDOW.blit(log3, (log3frame3, 132),(0,0,49,26.5))
         log3frame3 = log3frame3 + 5
         if log3frame3 == 790:
            log3frame3 = -40
#Top row of river
         WINDOW.blit(log4, (log4frame1, 76),(0,0,48,26.5))
         log4frame1 = log4frame1 - 5
         if log4frame1 == -40:
            log4frame1 = 780
         WINDOW.blit(log4, (log4frame2, 76),(0,0,48,26.5))
         log4frame2 = log4frame2 - 5
         if log4frame2 == -40:
            log4frame2 = 780
         WINDOW.blit(log4, (log4frame3, 76),(0,0,48,26.5))
         log4frame3 = log4frame3 - 5
         if log4frame3 == -40:
            log4frame3 = 780
         WINDOW.blit(log4, (log4frame4, 76),(0,0,48,26.5))
         log4frame4 = log4frame4 - 5
         if log4frame4 == -40:
            log4frame4 = 780
#Bottom row of river
         WINDOW.blit(log4, (log4frame1, 188),(0,0,48,26.5))
         log4frame1 = log4frame1 - 5
         if log4frame1 == -40:
            log4frame1 = 780
         WINDOW.blit(log4, (log4frame2, 188),(0,0,48,26.5))
         log4frame2 = log4frame2 - 5
         if log4frame2 == -40:
            log4frame2 = 780
         WINDOW.blit(log4, (log4frame3, 188),(0,0,48,26.5))
         log4frame3 = log4frame3 - 5
         if log4frame3 == -40:
            log4frame3 = 780
         WINDOW.blit(log4, (log4frame4, 188),(0,0,48,26.5))
         log4frame4 = log4frame4 - 5
         if log4frame4 == -40:
            log4frame4 = 780

#Road objects
#Top row of road
         WINDOW.blit(car2, (car2frame1, 300),(0,0,38.5,35))
         car2frame1 = car2frame1 + 7
         if car2frame1 == 793:
            car2frame1 = -40
         WINDOW.blit(car2, (car2frame2, 300),(0,0,38.5,35))
         car2frame2 = car2frame2 + 7
         if car2frame2 == 793:
            car2frame2 = -40
         WINDOW.blit(car2, (car2frame3, 300),(0,0,38.5,35))
         car2frame3 = car2frame3 + 7
         if car2frame3 == 793:
            car2frame3 = -40
         WINDOW.blit(car2, (car2frame4, 300),(0,0,38.5,35))
         car2frame4 = car2frame4 + 7
         if car2frame4 == 793:
            car2frame4 = -40
#Bottom row of road
         WINDOW.blit(car2, (car2frame1, 412),(0,0,38.5,35))
         car2frame1 = car2frame1 + 7
         if car2frame1 == 793:
            car2frame1 = -40
         WINDOW.blit(car2, (car2frame2, 412),(0,0,38.5,35))
         car2frame2 = car2frame2 + 7
         if car2frame2 == 793:
            car2frame2 = -40
         WINDOW.blit(car2, (car2frame3, 412),(0,0,38.5,35))
         car2frame3 = car2frame3 + 7
         if car2frame3 == 793:
            car2frame3 = -40
         WINDOW.blit(car2, (car2frame4, 412),(0,0,38.5,35))
         car2frame4 = car2frame4 + 7
         if car2frame4 == 793:
            car2frame4 = -40
#Middle row of road
         WINDOW.blit(car4, (car4frame1, 356),(0,0,31.25,36))
         car4frame1 = car4frame1 - 7
         if car4frame1 == -41:
            car4frame1 = 778
         WINDOW.blit(car4, (car4frame2, 356),(0,0,31.25,36))
         car4frame2 = car4frame2 - 7
         if car4frame2 == -41:
            car4frame2 = 778
         WINDOW.blit(car4, (car4frame3, 356),(0,0,31.25,36))
         car4frame3 = car4frame3 - 7
         if car4frame3 == -41:
            car4frame3 = 778
         WINDOW.blit(car4, (car4frame4, 356),(0,0,31.25,36))
         car4frame4 = car4frame4 - 7
         if car4frame4 == -41:
            car4frame4 = 778

#Collisions with road objects
         if playery == 412 and playerx >= car2frame1 and playerx <= car2frame1 + 38.5 or playery == 300 and playerx >= car2frame1 and playerx <= car2frame1 + 38.5:
            game = game - 1
            playerx = 354
            playery = 468
         if playery == 412 and playerx >= car2frame2 and playerx <= car2frame2 + 38.5 or playery == 300 and playerx >= car2frame2 and playerx <= car2frame2 + 38.5:
            game = game - 1
            playerx = 354
            playery = 468
         if playery == 412 and playerx >= car2frame3 and playerx <= car2frame3 + 38.5 or playery == 300 and playerx >= car2frame3 and playerx <= car2frame3 + 38.5:
            game = game - 1
            playerx = 354
            playery = 468
         if playery == 412 and playerx >= car2frame4 and playerx <= car2frame4 + 38.5 or playery == 300 and playerx >= car2frame4 and playerx <= car2frame4 + 38.5:
            game = game - 1
            playerx = 354
            playery = 468
         if playery == 356 and playerx >= car4frame1 and playerx <= car4frame1 + 31.25:
            game = game - 1
            playerx = 354
            playery = 468
         if playery == 356 and playerx >= car4frame2 and playerx <= car4frame2 + 31.25:
            game = game - 1
            playerx = 354
            playery = 468
         if playery == 356 and playerx >= car4frame3 and playerx <= car4frame3 + 31.25:
            game = game - 1
            playerx = 354
            playery = 468
         if playery == 356 and playerx >= car4frame4 and playerx <= car4frame4 + 31.25:
            game = game - 1
            playerx = 354
            playery = 468
# Water & Log Collision
         if playery == 76 and playerx >= log4frame1 and playerx <= log4frame1 + 48 and playerx > -30 and playerx < 730 or playery == 188 and playerx >= log4frame1 and playerx <= log4frame1 + 48 and playerx > -30 and playerx < 730:
            playerx = playerx - 10
         elif playery == 76 and playerx >= log4frame2 and playerx <= log4frame2 + 48 and playerx > -30 and playerx < 692 or playery == 188 and playerx >= log4frame2 and playerx <= log4frame2 + 48 and playerx > -30 and playerx < 730:
            playerx = playerx - 10
         elif playery == 76 and playerx >= log4frame3 and playerx <= log4frame3 + 48 and playerx > -30 and playerx < 692 or playery == 188 and playerx >= log4frame3 and playerx <= log4frame3 + 48 and playerx > -30 and playerx < 730:
            playerx = playerx - 10
         elif playery == 76 and playerx >= log4frame4 and playerx <= log4frame4 + 48 and playerx > -30 and playerx < 730 or playery == 188 and playerx >= log4frame4 and playerx <= log4frame4 + 48 and playerx > -30 and playerx < 730:
            playerx = playerx - 10
         elif playery == 132 and playerx >= log3frame1 and playerx <= log3frame1 + 49 and playerx > -30 and playerx < 730:
            playerx = playerx + 5
         elif playery == 132 and playerx >= log3frame2 and playerx <= log3frame2 + 49 and playerx > -30 and playerx < 730:
            playerx = playerx + 5
         elif playery == 132 and playerx >= log3frame3 and playerx <= log3frame3 + 49 and playerx > -30 and playerx < 730:
            playerx = playerx + 5
         elif playery == 132 and playerx >= log3frame4 and playerx <= log3frame4 + 49 and playerx > -30 and playerx < 730:
            playerx = playerx + 5
         elif playerx >= -30 and playerx <= 730 and playery <= 188 and playery >= 76:
            game = game - 1
            playerx = 354
            playery = 468

# Sprite Movement
      WINDOW.blit(Player, (playerx,playery), (frame , 0, 30, 37))

# grass collsion
   if playery == 20 and playerx > 60 and playerx < 122:
      playery = playery + 56
   if playery == 20 and playerx > 172 and playerx < 234:
      playery = playery + 56
   if playery == 20 and playerx > 284 and playerx < 346:
      playery = playery + 56
   if playery == 20 and playerx > 396 and playerx < 458:
      playery = playery + 56
   if playery == 20 and playerx > 508 and playerx < 567:
      playery = playery + 56
   if playery == 20 and playerx > 617 and playerx < 675:
      playery = playery + 56


# Win Menu
   if wincounter == 7:
      WINDOW.blit(img2, (0,0))
      WINDOW.blit(text4, (425, 100))
      WINDOW.blit(text2, (450,175))
      WINDOW.blit(text3, (450,225))
      WINDOW.blit(picture3, (Px2,Py2))
      
# Game Over Menu
   if game == 0:
      WINDOW.blit(text, (309,182))
      WINDOW.blit(picture, (0,0))
      WINDOW.blit(text2, (349,282))
      WINDOW.blit(text3, (349,332))
      WINDOW.blit(picture2, (Px,Py))


        #This line of code updates the display and draws the images

   pygame.display.update()

   fpsClock.tick(FPS)
