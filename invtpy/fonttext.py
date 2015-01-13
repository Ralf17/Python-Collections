import pygame, sys, pdb
from pygame.locals import *

pygame.init()
pdb.set_trace()
DISPLAYSURF = pygame.display.set_mode((100, 50))
pygame.display.set_caption('Hello World!')

WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
BLUE = (0, 0, 128)

fontObj = pygame.font.Font('freesansbold.ttf', 32)
textSurfaceObj = fontObj.render('Check', True, GREEN, BLUE)
textRectObj = textSurfaceObj.get_rect()
textRectObj.center = (50, 25)

while True: # main game loop
	DISPLAYSURF.fill(WHITE)
	DISPLAYSURF.blit(textSurfaceObj, textRectObj)
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit()
	pygame.display.update()
