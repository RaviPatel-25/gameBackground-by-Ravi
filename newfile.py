import pygame
from pygame.locals import *
 
pygame.init()
window = pygame.display.set_mode((600, 600))

image_sprite = []

for i in range(24):
	image_sprite.append(pygame.image.load("/storage/emulated/0/gif_to_png/Img/Convert"+str(i)+".png"))
	image_sprite[i] = pygame.transform.scale(image_sprite[i], (1080,2129))

clock = pygame.time.Clock()
value = 0

run = True
while run:
    clock.tick(60)
    
    if value >= len(image_sprite):
        value = 0
  
    image = image_sprite[value]
    window.blit(image, (0,0))
    pygame.display.update()
    window.fill((0, 0, 0))

    value += 1