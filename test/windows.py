#!/usr/bin/env python
import pygame
if ( __name__ == "__main__" ):
	pygame.init()
	windows_size = windows_width, windows_heigth = 640, 480 
	windows = pygame.display.set_mode( windows_size, pygame.RESIZABLE )
	print pygame.display.get_caption()
	pygame.display.set_caption( " ser_caption(-----)") 
	running = True 
	while( running ):
		for event in pygame.event.get():
			if ( event.type == pygame.QUIT ) :
				running = False
	pygame.quit()
