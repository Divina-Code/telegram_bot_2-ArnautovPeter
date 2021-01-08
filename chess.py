import pygame

gamedisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Snowmans")


def draw_chess(x, y, startX = 100, startY = 100, size = 30):

    pygame.draw.rect(gamedisplay, BROWN, ( nowx,now), 25 )


BLACK = (0,0,0)
WHITE = (255, 255, 255)
BROWN = (150, 75, 0)
RED = (255, 0, 0)

game = True
while game:

    for e in pygame.event.get():

        if e.type == pygame.QUIT:
            game = False


    draw_chess(8,8)

    pygame.display.update()
pygame.quit()
