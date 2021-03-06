﻿#!/usr/bin/env python
# -*-coding: utf-8 -*-
#filename:GameRun.py

import pygame
from sys import exit
from pygame.locals import *
from GameEntity import *
from World import *
from StateMachine import *
from gameobjects.vector2 import Vector2
# import thread

def run():
	pygame.init()
	screen = pygame.display.set_mode((640, 480), 0, 32)
	world = World()
	clock = pygame.time.Clock()
	stateMachine = StateMachine(world)
	x, y = (0, 0)
	time = 0
	#pygame.display.update()
	while True:
		for event in pygame.event.get():
			if event.type == QUIT:
				return
			if event.type == MOUSEBUTTONDOWN:
				x, y = event.pos
				world.create_ant((x, y))
				
		time_passed = clock.tick(30)
		if randint(1, 10) == 1:
			world.create_leaf()
			
		if time == 50:
			world.create_spider()
			time = 0
		else:
			time += 1
		print time 
		
		stateMachine.analyze_entities()
		stateMachine.ant_state()
		stateMachine.leaf_state()
		stateMachine.spider_state()
			
		world.process(time_passed)
		world.render(screen)
	
		pygame.display.update()
	
if __name__ == "__main__":
	run()
			
