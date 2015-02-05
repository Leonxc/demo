#!/usr/bin/env python
# -*-coding: utf-8 -*-
#filename:GameRun.py

import pygame
from pygame.locals import *
from GameEntitys import *
from World import *
from gameobjects.vector2 import Vector2

def run():
	pygame.init()
	world = World()
	screen = pygame.display.set_mode((world.width, world.high), 0, 32)
	clock = pygame.time.Clock()
	action[] = {}
		
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				return
			if event.type == MOUSEBUTTONDOWN:
				x, y = event.MOUSEBUTTONDOWN[0]
				world.create_ant()
				
		time_passed = clock.tick(30)
		
		if randint(1, 10) == 1:
			world.create_leaf()

			
	world.process(time_passed)
	world.render(screen)
	
	pygame.display.update()
	
if __name__ == "__main__":
	run()
			
