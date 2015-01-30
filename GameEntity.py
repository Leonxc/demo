#!/usr/bin/env python
# -*-coding: utf-8 -*-
# filename:GameEntity.py

import pygame
from gameobjects.vector2 import Vector2

class GameEntity():
	#游戏的实体单位，其中共有的基本属性和功能
	def __init__(self, name):
		self.name = name
		self.image = pygame.image
		self.speed = 0.
		self.location = Vector2(0, 0)
		self.destination = Vector2(0, 0)
		self.brain = StateMachine()
		self.eye = World()
		self.id = 0
		
	def render(self, surface):
		#将实体画到屏幕上
		x, y = self.location
		w, h = self.image.get_size()
		surface.blit(self.image, (x-w/2, y-h/2))
		
	def process(self, time_passed):
		#计算实体的移动方向、距离，返回新的location
		self.brain.think() #获取新状态
		if self.location != self.destination and speed != 0:
			location_to_destination = self.destination - self.location
			distance = location_to_destination.get_length()
			head = location_to_destination.normalise()
			road = min(distance, time_passed * self.speed)
			self.location += head * road
			
class Ant(GameEntity):
	#蚂蚁
	def __init__(self,"ant"):
		
