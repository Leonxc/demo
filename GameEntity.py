#!/usr/bin/env python
# -*-coding: utf-8 -*-

import pygame
from gameobjects.vector2 import Vector2

class GameEntity():
	def __init__(self, name):
		self.name = name
		self.image = pygame.image
		self.speed = 0.
		self.location = Vector2(0, 0)
		self.destination = Vector2(0, 0)
		
	def render(self):
		
