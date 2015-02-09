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
				x, y = event.pos
				world.create_ant((x, y))
				
		time_passed = clock.tick(30)
		if randint(1, 10) == 1:
			world.create_leaf()
			
		for ant in world.entities:
			if isinstance(ant, Ant):
				for leaf in world.entities:
					if isinstance(leaf, Leaf):
						distance = (ant.location - leaf.location).get_length()
						distance_to_nest = (ant.location - world.nest_location).get_length()
						if distance > ant.senseRange and (ant.state == "explore" or ant.state == "drop_stuff"):
							ant.explore()
							print 1
						elif 10 < distance < ant.senseRange and (ant.state == "explore" or ant.state == "seeking") :
							ant.seeking(leaf)
							print 2
						elif distance_to_nest >world.nest_r and distance < 10 and ant.state == "seeking":
							ant.carry_stuff(leaf)
							leaf.carry_by_ant(ant)
							print 3
						elif distance_to_nest < world.nest_r and ant.state == "carry_stuff":
							ant.drop_stuff()
							leaf.speed = 0
							print 4
			
		world.process(time_passed)
		world.render(screen)
	
		pygame.display.update()
	
if __name__ == "__main__":
	run()
			
