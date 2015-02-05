#!/usr/bin/env python
# -*-coding: utf-8 -*-
#filename:GameRun.py

import pygame
from sys import exit
from pygame.locals import *
from GameEntity import *
from World import *
from gameobjects.vector2 import Vector2

def run():
	pygame.init()
	screen = pygame.display.set_mode((640, 480), 0, 32)
	world = World()
	clock = pygame.time.Clock()
	x, y = (0, 0)
	#pygame.display.update()
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
		for ant in world.entities:
			if isinstance(ant, Ant):
				while True:
					if ant.explore():
						break
				while True:
					if ant.seeking():
						break

		world.process(time_passed)
		world.render(screen)
	
		pygame.display.update()
	
if __name__ == "__main__":
	run()
			
