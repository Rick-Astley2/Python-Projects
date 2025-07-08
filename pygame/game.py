import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800,400))
clock = pygame.time.Clock()
pygame.display.set_caption("game")

sky = pygame.image.load('pygame/graphics/sky.png')
pygame.transform.scale(sky, (800,400))
test_suface = pygame.image.load('pygame/graphics/sky.png')

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(test_suface,(0,0))       

    pygame.display.update()
    clock.tick(60)