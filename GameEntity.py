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
		self.location = Vector2(location)
		self.destination = Vector2(randint(0, world.width), randint(0, world.high))
		self.speed = 120
		self.senseRange = 60
		self.state = "explore"
		
	def render(self, surface):
		x, y = self.location
		surface.blit(self.image, (x, y))
		
	def process(self, time_passed):#移动
		while self.location == self.destination:
			self.explore()
		if self.location != self.destination and self.speed > 0:
			location_to_destination = self.destination - self.location
			distance = location_to_destination.get_length()
			head = location_to_destination.get_normalized()
			road = min(distance, time_passed * self.speed / 1000)
			self.location += head * road
			#TODO 图片旋转
	"""
	def attack_spider(self, spider):
		self.destination = spider.location - randint(-10, 10)
		distance = (self.location - self.destination).get_length()
		if distance < 10:
			self.speed = 60
		else:
			self.speed = 100
			"""
	def explore(self):
		w, h = (self.world.width, self.world.high)
		if randint(1, 300) == 1:
			self.destination = (randint(0, w), randint(0, h))
			self.state = "explore"
			
	def seeking(self, leaf):
		self.destination = leaf.location
		self.state = "seeking"
		
	def carry_stuff(self):
		self.destination = self.world.nest_location + (randint(-20, 20), randint(-20, 20)) - Vector2(self.image.get_size())/2
		self.speed = 60
		self.state = "carry_stuff"
			
	def drop_stuff(self):
		self.speed = 120
		self.state = "drop_stuff"
		
	def dead():
		self.state = "dead"
		self.destination = self.location
		
		
class Leaf():
	def __init__(self, id, image, world):
		self.name = "leaf"
		self.id = id
		self.image = image
		self.world = world
		self.location = Vector2(0, 0)
		self.destination = Vector2(0, 0)
		self.speed = 0
		self.state = ""
		self.target = None
		
	def create(self):
		w, h = (self.world.width, self.world.high)
		x, y = (randint(0, w-10), randint(0, h-10))
		ox, oy = self.world.nest_location
		r = self.world.nest_r
		while True:
			if ox-r < x < ox+r and oy-r < y < oy+r:
				x, y = (randint(0, w-10), randint(0, y-10))
			else:
				self.location = Vector2(x, y)
				self.destination = self.location
				break
				
	def render(self, surface):
		#print self.location
		surface.blit(self.image, self.location)
		
	def process(self, time_passed):#移动
		if self.location != self.destination:
			location_to_destination = self.destination - self.location
			distance = location_to_destination.get_length()
			head = location_to_destination.get_normalized()
			road = min(distance, time_passed * self.speed / 1000)
			self.location += road * head

	def carry_by_ant(self):
		if self.target != None:
			self.speed = self.target.speed
			self.destination = self.target.location
		
	def drop_by_ant(self):
		self.speed = 0
		self.target = None
		self.destination = self.location
		
class Spider():
	def __init__(self, id, image, world):
		self.name = "spider"
		self.id = id
		self.image = image
		self.world = world
		self.health = 25
		self.speed = 80
		self.state = "explore"
		self.location = Vector2(0, 0)
		self.destination = Vector2(0, 0)
		self.target = None
		
	def render(self, surface):
		surface.blit(self.image, self.location)
		
	def process(self, time_passed):#移动
		if self.location != self.destination:
			location_to_destination = self.destination - self.location
			distance = location_to_destination.get_length()
			head = location_to_destination.get_normalize()
			road = min(distance, time_passed * self.speed / 1000)
			self.location += road * head
	
	def create(self):
		w, h = (self.world.width, self.world.high)
		if randint(0, 100) == 1:
			self.location = Vector2(0, randint(0, h))
		elif randint(0, 100) == 2:
			self.location = Vector2(w, randint(0, h))
		elif randint(0, 100) == 3:
			self.location = Vector2(randint(0, w), 0)
		elif randint(0, 100) == 4:
			self.location = Vector2(randint(0, w), h)
		else:
			return
			
	def explore(self):
		w, h = (self.world.width, self.world.high)
		if randint(1, 300) == 1:
			self.destination = (randint(0, w), randint(0, h))
			self.state = "explore"
			
	def seeking(self, ant):
		self.destination = ant.location
		self.state = "seeking"
		self.target = ant
		
	def eat_ant(self, ant):
		ant.dead()
		
	def dead(self):
		# self.speed = 0
		self.destination = self.location
		self.state = "dead"
		
	def carry_by_ant(self, ant):
		self.speed = ant.speed
		self.destination = ant.location
		self.state = "carry_by_ant"
		
	def drop_by_ant(self):
		self.speed = 0
		self.target = None
		self.destination = self.location
