import pygame
from random import randint
from time import sleep

pygame.init()
gamedisplay = pygame.display.set_mode((800, 600))
gamedisplay.fill((255, 255, 255))
radius = 10
color_red = 0
color_green = 0
color_blue = 0
color = (color_red, color_red, color_blue)

game = True

print(color)
while(game == True):
    color = (color_red, color_red, color_blue)
    events = pygame.event.get()

    for e in events:
        print(e)
        if e.type == pygame.QUIT:
            game = False

        if e.type == pygame.MOUSEBUTTONDOWN:

            if e.button == 4:
                radius += 1
            if e.button == 5:
                radius -= 1

            if e.button == 2:   #рандомный цвет на колесико
                color_red = randint(0, 255)
                color_green = randint(0, 255)
                color_blue = randint(0, 255)

    if pygame.mouse.get_pressed()[0]:
        mousepose = pygame.mouse.get_pos()
        pygame.draw.circle(gamedisplay, color, mousepose, radius)
        
    elif pygame.mouse.get_pressed()[2]: #ластик на правую кнопку
        mousepose = pygame.mouse.get_pos()
        pygame.draw.circle(gamedisplay, (255, 255, 255), mousepose, radius)

    pygame.display.update()

pygame.quit()
