import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame
import time
import random
from time import sleep
def up():
    pygame.display.update()
pygame.init()
grey = (245,245,245) 
red = (255,0,0)
blue = (0,0,255)
orange = (255,102,0)
purple = (201,71,245)
pink = (255,0,127)
green = (57,255,20)
mango = (218,160,61)
moss = (97,98,71)
colorlist = [red,blue,orange,pink,green,mango,purple,moss]
colorx = random.choice(colorlist)
if colorx == red:
    coloro = blue
elif colorx == blue:
    coloro = red
elif colorx == pink:
    coloro = green
elif colorx == green:
    coloro = pink
elif colorx == purple:
    coloro = orange
elif colorx == orange:
    coloro = purple
elif colorx == moss:
    coloro = mango
elif colorx == mango:
    coloro = moss
myfont = pygame.font.SysFont("Arial", 150) 
myfont2 = pygame.font.SysFont("Arial", 48)
textsurface = myfont.render("X", True, (colorx))
textsurface2 = myfont.render("O", True, (coloro))
screen = pygame.display.set_mode((900, 660)) 
image = pygame.image.load("tictactoe.jpg")
pygame.display.set_caption("Tic Tac Toe")
screen.blit(image, (0,0))
# Buttons
input_rect = pygame.Rect(150,455,200,195) # rect in the form (x,y,width,height)
input_rect2 = pygame.Rect(170,265,175,160)
input_rect3 = pygame.Rect(150,63,190,170)
input_rect4 = pygame.Rect(375,40,152,195)
input_rect5 = pygame.Rect(560,40,180,195)
input_rect6 = pygame.Rect(560,265,180,158)
input_rect7 = pygame.Rect(560,455,180,178)
input_rect8 = pygame.Rect(373,265,155,160)
input_rect9 = pygame.Rect(374,457,155,170)
# Display buttons
pygame.draw.rect(screen,grey,input_rect)
pygame.draw.rect(screen,grey,input_rect2)
pygame.draw.rect(screen,grey,input_rect3)
pygame.draw.rect(screen,grey,input_rect4)
pygame.draw.rect(screen,grey,input_rect5)
pygame.draw.rect(screen,grey,input_rect6)
pygame.draw.rect(screen,grey,input_rect7)
pygame.draw.rect(screen,grey,input_rect8)
pygame.draw.rect(screen,grey,input_rect9)
up()
p1 = []
p2=[]
# Crosses
def cross(a):
    while True:
        if a == 1:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos) and 7 not in p1 and 7 not in p2:
                    screen.blit(textsurface, (203,470))
                    a = 1
                    p1.append(7)
                    break
                elif input_rect2.collidepoint(event.pos) and 4 not in p1 and 4 not in p2:
                    screen.blit(textsurface,(203,265))
                    a = 1
                    p1.append(4)
                    break
                elif input_rect3.collidepoint(event.pos) and 1 not in p1 and 1 not in p2:
                    screen.blit(textsurface,(203,75))
                    a=1
                    p1.append(1)
                    break
                elif input_rect4.collidepoint(event.pos) and 2 not in p1 and 2 not in p2:
                    screen.blit(textsurface,(394,75))
                    a=1
                    p1.append(2)
                    break
                elif input_rect5.collidepoint(event.pos) and 3 not in p1 and 3 not in p2:
                    screen.blit(textsurface,(590,75))
                    p1.append(3)
                    a=1
                    break
                elif input_rect6.collidepoint(event.pos) and 6 not in p1 and 6 not in p2:
                    screen.blit(textsurface,(590,270))
                    a=1
                    p1.append(6)
                    break
                elif input_rect7.collidepoint(event.pos) and 9 not in p1 and 9 not in p2:
                    screen.blit(textsurface,(590,470))
                    p1.append(9)
                    a=1
                    break
                elif input_rect8.collidepoint(event.pos) and 5 not in p1 and 5 not in p2:
                    screen.blit(textsurface,(398,265))
                    a=1
                    p1.append(5)
                    break
                elif input_rect9.collidepoint(event.pos) and 8 not in p1 and 8 not in p2:
                    screen.blit(textsurface,(399,470))
                    p1.append(8)
                    a=1
                    break
                else:
                    continue
# Noughts
def noughts(a):
    while True:
        if a == 1:
            break
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos) and 7 not in p1 and 7 not in p2:
                    screen.blit(textsurface2, (203,470))
                    a = 1
                    p2.append(7)
                    break
                elif input_rect2.collidepoint(event.pos) and 4 not in p1 and 4 not in p2:
                    screen.blit(textsurface2,(203,265))
                    a=1
                    p2.append(4)
                    break
                elif input_rect3.collidepoint(event.pos)and 1 not in p1 and 1 not in p2:
                    screen.blit(textsurface2,(203,75))
                    a = 1
                    p2.append(1)
                    break
                elif input_rect4.collidepoint(event.pos) and 2 not in p1 and 2 not in p2:
                    screen.blit(textsurface2,(394,75))
                    a=1
                    p2.append(2)
                    break
                elif input_rect5.collidepoint(event.pos) and 3 not in p1 and 3 not in p2:
                    screen.blit(textsurface2,(590,75))
                    a=1
                    p2.append(3)
                    break
                elif input_rect6.collidepoint(event.pos) and 6 not in p1 and 6 not in p2:
                    screen.blit(textsurface2,(590,270))
                    a=1
                    p2.append(6)
                    break
                elif input_rect7.collidepoint(event.pos) and 9 not in p1 and 9 not in p2:
                    screen.blit(textsurface2,(590,470))
                    a=1
                    p2.append(9)
                    break
                elif input_rect8.collidepoint(event.pos) and 5 not in p1 and 5 not in p2:
                    screen.blit(textsurface2,(393,265))
                    a=1
                    p2.append(5)
                    break
                elif input_rect9.collidepoint(event.pos) and 8 not in p1 and 8 not in p2:
                    screen.blit(textsurface2,(399,470))
                    a=1
                    p2.append(8)
                    break
                else:
                    continue
b=2
# Display text if their is a winner
def winX():
    playerx = myfont2.render("X WINS", True, (colorx))
    screen.blit(playerx,(720,16))
    up()
    sleep(3)
def winO():
    playero = myfont2.render("O WINS", True,(coloro))
    screen.blit(playero,(720,16))
    up()
    sleep(3)
def checkers(b): # Check for winner
    if 1 in p1 and 2 in p1 and 3 in p1:
        winX()
        b+=1
        up()
        exit()
    elif 1 in p2 and 2 in p2 and 3 in p2:
        winO()
        b+=1
        up()
        exit()
    elif 4 in p1 and 5 in p1 and 6 in p1:
        winX()
        b+=1
        up()
        exit()
    elif 4 in p2 and 5 in p2 and 6 in p2:
        winO()
        b+=1
        up()
        exit()
    elif 7 in p1 and 8 in p1 and 9 in p1:
        winX()
        b+=1
        up()
        exit()
    elif 7 in p2 and 8 in p2 and 9 in p2:
        winO()
        b+=1
        up()
        exit()
    elif 1 in p1 and 4 in p1 and 7 in p1:
        winX()
        b+=1
        up()
        exit()
    elif 1 in p2 and 4 in p2 and 7 in p2:
        winO()
        b+=1
        up()
        exit()
    elif 2 in p1 and 5 in p1 and 8 in p1:
        winX()
        b+=1
        up()
        exit()
    elif 2 in p2 and 5 in p2 and 8 in p2:
        winO()
        b+=1
        up()
        exit()
    elif 3 in p1 and 6 in p1 and 9 in p1:
        winX()
        b+=1
        up()
        exit()
    elif 3 in p2 and 6 in p2 and 9 in p2:
        winO()
        b+=1
        up()
        exit()
    elif 3 in p1 and 5 in p1 and 7 in p1:
        winX()
        b+=1
        up()
        exit()
    elif 3 in p2 and 5 in p2 and 7 in p2:
        winO()
        b+=1
        up()
        exit()
    elif 1 in p1 and 5 in p1 and 9 in p1:
        winX()
        b+=1
        up()
        exit()
    elif 1 in p2 and 5 in p2 and 9 in p2:
        winO()
        b+=1
        up()
        exit()
    else:
        pass
        b = 2
cross(2)
up()
noughts(2)
up()
cross(2)
up()
noughts(2)
up()
cross(2)
checkers(2)
up()
noughts(2)
checkers(2)
up()
cross(2)
checkers(2)
up()
noughts(2)
checkers(2)
up()
cross(2)
checkers(2)
up()
if b == 2:
    tie = myfont2.render("TIE", True, (0,0,0))
    screen.blit(tie,(730,16))
    up()
    sleep(2)