#!/usr/bin/env python
# -*-coding: utf-8 -*-
# filename:GameEntitys.py


import pygame
from pygame.locals import *
from gameobjects.vector2 import Vector2
from random import randint
from EntityState import *

class GameEntity():
	#游戏的实体单位，其中共有的基本属性和功能
	def __init__(self, world, name, image):
		self.name = name
		self.image = image
		self.speed = 0.
		self.location = Vector2(0, 0)
		self.destination = Vector2(0, 0)
		self.brain = StateMachine()
		self.world = World
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
		GameEntity.__init__(self, world, "ant", image)
		exploring_state = AntstateExploring(self)
		seeking_state = AntstateSeeking(self)
		delivering_state = AntStateDelivering(self)
		hunting_state = AntStateHunting(self)
		self.brain.add_state(exploring_state)
		self.brain.add_state(seeking_state)
		self.brain.add_state(delivering_state)
		self.brain.add_state(hunting_state)
		self.carry_image = None
		
	def carry(self, image):
		#携带杀死后的蜘蛛或者是树叶
		self.carry_image = image
		
	def drop(self, surface):
		#将携带的实体丢下
		if self.carry_image:
			x, y = self.location
			w, h = self.carry_image.get_size()
			surface.blit(self.carry_image, (x-w, y-h/2))
			self.carry_image = None
			
	def render(self, surface):
		#当蚂蚁携带物体时，会带着物体一起移动
		GameEntity.render(self, surface)
		if self.carry_image:
			x, y = self.location
			w, h = self.carry_image.get_size()
			surface.blit(self.carry_image, (x-w,y-h/2))
			
class Leaf(GameEntity):
	#叶子，没有特殊属性
	def __init__(self, world, image):
		GameEntity.__init__(self, world, "leaf", image)
		
class Spider(GameEntity):
	#蜘蛛
	def __init__(self, world, image):
		GameEntity.__init__(self, world, "Spider", image)
		self.dead_image = pygame.transfom.flip(image, 0, 1)
		self.health = 25
		self.speed = 50. + randint(-20,20)
		
	def bitten(self)
	#被蚂蚁hunting时
		self.health -= 1
		if self.health <= 0:
			self.speed = 0.
			self.image = self.dead_image
		self.speed = 140.
		
	def render(self, surface):
		GameEntity.render(self, surface)
		x, y = self.location
		if x > SCREEN_SIZE[0] + 2 :
			self.world.remove_entity(self)
			return
		GameEntity.process(self, time_passed)