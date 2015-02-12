#!/usr/bin/env python
# -*- coding: utf-8 -*-
# filename:World.py

import pygame
from GameEntity import *

class World():
	def __init__(self):
		self.width = 640
		self.high = 480
		self.nest_location = Vector2(self.width/2, self.high/2)
		self.nest_r = 50
		self.entities = []
		self.entities_id = 0
		
		self.ant_num = 20
		self.ant_id = 0
		self.ant_image = 'ant.png'
		
		self.spider_num = 1
		self.spider_id = 0
		self.spider_image = 'spider.png'
		
		self.leaf_num = 20
		self.leaf_id = 0
		self.leaf_image = 'leaf.png'
		
		self.background = pygame.surface.Surface((self.width, self.high)).convert()
		self.background.fill((255, 255, 255))
		pygame.draw.circle(self.background, (200, 255, 200), (self.width/2, self.high/2), self.nest_r)
		
	def render(self, surface):
		surface.blit(self.background, (0, 0))
		for entity in self.entities:
			entity.render(surface)
			
	def process(self, time_passed):
		for entity in self.entities:
			entity.process(time_passed)
		
	def create_ant(self, mouse_down_pos):
		x, y = mouse_down_pos
		if self.ant_num > 0 and 0 < x < self.width and 0 < y < self.high:
			ant = Ant(self.ant_id, pygame.image.load(self.ant_image).convert_alpha(), self, Vector2(x, y))
			self.entities.append(ant)
			self.entities_id += 1
			self.ant_num -= 1
			self.ant_id += 1
			
	def create_leaf(self):
		if self.leaf_num <= 0:
			return
		w, h = (self.width, self.high)
		x, y = (randint(0, w-10), randint(0, h-10))
		ox, oy = self.nest_location
		r = self.nest_r
		while True:
			if ox-r < x < ox+r and oy-r < y < oy+r:
				x, y = (randint(0, w-10), randint(0, y-10))
			else:
				break
		leaf = Leaf(self.leaf_id, pygame.image.load(self.leaf_image).convert_alpha(), self)
		leaf.location = Vector2(x, y)
		# leaf.destination = leaf.location
		self.entities.append(leaf)
		self.entities_id += 1
		self.leaf_num -= 1
		self.leaf_id += 1
			

	def create_spider(self):
		if self.spider_num <= 0:
			return
		w, h = (self.width, self.high)
		if randint(0, 4) == 1:
			spider_location = Vector2(0, randint(0, h-20))
		elif randint(0, 4) == 2:
			spider_location = Vector2(w-20, randint(0, h-20))
		elif randint(0, 4) == 3:
			spider_location = Vector2(randint(0, w-20), 0)
		elif randint(0, 4) == 4:
			spider_location = Vector2(randint(0, w-20), h-20)
		else:
			return
		spider = Spider(self.spider_id, pygame.image.load(self.spider_image), self)
		spider.location = spider_location
		# spider.destination = Vector2(randint(0, w-20), randint(0, h-20))
		self.entities.append(spider)
		self.entities_id += 1
		self.spider_id += 1
		self.spider_num -= 1
		#TODO
		
	def del_ant(self):
		#TODO
		pass
		
	def del_leaf(self):
		#TODO
		pass
		
	def del_spider(self):
		#TODO
		pass
		