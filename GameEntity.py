#!/usr/bin/env python
# -*-coding: utf-8 -*-
# filename:GameEntity.py

import pygame
from gameobjects.vector2 import Vector2
from random import randint

class Ant():
	def __init__(self, id, image, world, location):
		self.name = "ant"
		self.id = id
		self.image = image
		self.world = world
		self.location = location
		self.destination = Vector2(0, 0)
		self.speed = 60.
		self.senseRange = 30
		self.brain = StateMachine()
		
	def render(self):
		x, y = self.location
		w, h = self.image.get_size()
		pygame.blit(self.image, (x-w/2, y-h/2))#将图片中心作为显示坐标
		
	def process(self, time_passed):#移动
		if self.location != self.destination:
			location_to_destination = self.destination - self.location
			distance = location_to_destination.get_length()
			head = location_to_destination.normalize()
			self.location = min(distance, time_passed * self.speed * head)
		
	def create(self):
		x, y = self.world.mouse_pos
		if self.world.nest.location
		#TODO
	
	def attack_spider(self, spider):
		self.destination = spider.location - randint(-10, 10)
		distance = (self.location - self.destination).get_length()
		if distance < 10:
			self.speed = 60
		else:
			self.speed = 100
			
	def carry_stuff(self):
		self.destination = world.NestPosition
		distance = (self.location - self.destination).get_length()
		if distance < self.world.nest.r:
			self.speed = 40.
			
	def drop_stuff(self):
		self.speed = 60
		
class Leaf():
	def __init__(self, id, image, world):
		self.name = "leaf"
		self.id = id
		self.image = image
		self.world = world
		self.location = Vector2(0, 0)
		self.destination = Vector2(0, 0)
		
	def create(self):
		x, y = self.location
		w, h = (self.world.width, self.world.high)
		ox, oy = self.world.nest.loaction
		r = self.world.nest.r
		for ox-r < x < ox+r and oy-r < y < oy+r:
			x, y = (randint(0, w), randint(0, y))
		self.location = (x, y)
			
	def render(self):
		x, y = self.location
		w, h = self.image.get_size()
		pygame.blit(self.image, (x-w/2, y-h/2))
		
	def process(self, time_passed):#移动
		if self.location != self.destination:
			location_to_destination = self.destination - self.location
			distance = location_to_destination.get_length()
			head = location_to_destination.normalize()
			self.location = min(distance, time_passed * self.speed * head)
		
	def carry_by_ant(self, ant):
		self.location = ant.location
		
class Spider():
	def __init__(self, id, image, world):
		self.name = "spider"
		self.id = id
		self.image = image
		self.world = world
		self.health = 25
		self.speed = 40
		#self.brain
		self.location = Vector2(0, 0)
		self.destination = Vector2(0, 0)
		
	def render(self):
		x, y = self.location
		w, h = self.image.get_size()
		pygame.blit(self.image, (x-w/2, y-h/2))
		
	def process(self, time_passed):#移动
		if self.location != self.destination:
			location_to_destination = self.destination - self.location
			distance = location_to_destination.get_length()
			head = location_to_destination.normalize()
			self.location = min(distance, time_passed * self.speed * head)
	
	def #TODO
