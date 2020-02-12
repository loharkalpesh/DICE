import pygame
import sys
import random
import os

x,y = 200,200

pygame.init()
pygame.display.init()

pygame.display.set_caption("DICE made by KALPESH LOHAR")
wd = pygame.display.set_mode((x,y))

clock = pygame.time.Clock()

wd.fill((255,255,255))

d1 = pygame.image.load("data\\assets\\1.png")
d2 = pygame.image.load("data\\assets\\2.png")
d3 = pygame.image.load("data\\assets\\3.png")
d4 = pygame.image.load("data\\assets\\4.png")
d5 = pygame.image.load("data\\assets\\5.png")
d6 = pygame.image.load("data\\assets\\6.png")

wel = pygame.image.load("data\\assets\\welcome.png")
wel = pygame.transform.scale(wel, (x,y)).convert_alpha()

ge = False
font = pygame.font.SysFont(None, 40)

wd.blit(wel, (0, 0))

def dices ():
    dice = random.randint(1, 6)
    if dice == 1:
        dice_s = d1
    elif dice == 2:
        dice_s = d2
    elif dice == 3:
        dice_s = d3
    elif dice == 4:
        dice_s = d4
    elif dice == 5:
        dice_s = d5
    elif dice == 6:
        dice_s = d6
    wd.blit(dice_s,(x/3,y/3))
    print(dice)
    text("You Have = " + str(dice), (118,8,229) , 16 , 150)
    pygame.display.update()
    clock.tick(30)

def text (tfont,color,x,y):
    stext = font.render(tfont, True, color)
    wd.blit(stext, [x, y])

while not False:
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            ge = True
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == (pygame.K_q or pygame.K_ESCAPE):
                ge = True
                sys.exit()
            if event.key == pygame.K_KP_ENTER:
                wd.fill((255, 255, 255))
                dices()
