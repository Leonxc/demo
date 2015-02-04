﻿#!/usr/bin/env python
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
		
	def render(self, surface):
		x, y = self.location
		w, h = self.image.get_size()
		surface.blit(self.image, (x-w/2, y-h/2))#将图片中心作为显示坐标
		
	def process(self, time_passed):#移动
		if self.location != self.destination:
			location_to_destination = self.destination - self.location
			distance = location_to_destination.get_length()
			head = location_to_destination.normalize()
			self.location = min(distance, time_passed * self.speed * head)
			#TODO 图片旋转
	
	def attack_spider(self, spider):
		self.destination = spider.location - randint(-10, 10)
		distance = (self.location - self.destination).get_length()
		if distance < 10:
			self.speed = 60
		else:
			self.speed = 100
			
	def explore(self):
		w, h = (self.world.width, self.world.high)
		self.destination = (randint(0, w), randint(0, h))
		for entity in self.world.entities:
			if isinstance(entity, Leaf):
				self.seeking()
			
	def seeking(self):
		
			
	def carry_stuff(self):
		self.destination = world.nest_location
		distance = (self.location - self.destination).get_length()
		if distance < self.world.nest_r:
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
		ox, oy = self.world.nest_location
		r = self.world.nest.r
		for ox-r < x < ox+r and oy-r < y < oy+r:
			x, y = (randint(0, w), randint(0, y))
		self.location = (x, y)
			
	def render(self, surface):
		x, y = self.location
		w, h = self.image.get_size()
		surface.blit(self.image, (x-w/2, y-h/2))
		
	def process(self, time_passed):#移动
		if self.location != self.destination:
			location_to_destination = self.destination - self.location
			distance = location_to_destination.get_length()
			head = location_to_destination.normalize()
			self.location = min(distance, time_passed * self.speed * head)
		
	def carry_by_ant(self, ant):
		self.location = ant.location
		"""
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
		self.destination = world.nest_location
		
	def render(self, surface):
		x, y = self.location
		w, h = self.image.get_size()
		surface.blit(self.image, (x-w/2, y-h/2))
		
	def process(self, time_passed):#移动
		if self.location != self.destination:
			location_to_destination = self.destination - self.location
			distance = location_to_destination.get_length()
			head = location_to_destination.normalize()
			self.location = min(distance, time_passed * self.speed * head)
	
	def create(self):
		if self.world.spider_num < 0:
			return
		w, h = (self.world.width, self.world.high)
		if randint(0, 100) == 1:
			self.location = (0, randint(0, h))
		elif randint(0, 100) == 2:
			self.location = (w, randint(0, h))
		elif randint(0, 100) == 3:
			self.location = (randint(0, w), 0)
		elif randint(0, 100) == 4:
			self.location = (randint(0, w), h)
			
	def dead(self):
		self.speed = 0
		#TODO 图片旋转
		
	def carry_by_ant(self, ant):
		self.location = ant.location
		"""
