#!/usr/bin/env python
# -*- coding: utf-8 -*-
# filename:World.py

import pygame
from GameEntity import *

class World():
	def __init__(self):
		self.width = 640
		self.high = 480
		self.nest_loaction = (self.width/2, self.high/2)
		self.nest_r = 50
		self.entities = {}
		self.entities_id = 0
		
		self.ant_num = 20
		self.ant_id = 0
		self.ant_image = ''
		
		self.spider_num = 5
		self.spider_id = 0
		self.spider_image = ''
		
		self.leaf_num = 50
		self.leaf_id = 0
		self.leaf_image = ''
		
	def render(self):
		for entity in entities:
			entity.render()
		
	def create_ant(self)
		for event in pygame.event.get():
			if event.type == MOUSEBUTTONDOWN:
				x, y = pygame.event.MOUSEBUTTONDOWN[0]
				if self.ant_num > 0 and x in range(0, self.width) and y in range(0, self.high)
					ant = Ant(self.ant_id, self.ant_image, self, (x, y))
					self.entities[self.entities_id] = ant
					self.entities_id += 1
					self.ant_num -= 1
					self.ant_id += 1
					self.render()
					
	def create_leaf(self):
		while True:
			x, y = (randint(0, self.width), randint(0, self.high))
			if self.nest_loaction[0]-self.nest_r < x < self.nest_loaction[0]+self.nest_r and self.nest_loaction[1]-self.nest_r < y < self.nest_loaction[1]+self.nest_r:
				continue
			elif:	self.leaf_num < 0:
				continue
			else:
				leaf = Leaf(self.leaf_id, self.leaf_image, self)
				self.entities[self.entities_id] = leaf
				self.entities_id += 1
				self.leaf_num -= 1
				self.leaf_id += 1
				self.render()
				
	def create_spider(self):
		if self.spider_num < 0:
			return
		w, h = (self.width, self.high)
		if randint(0, 100) == 1:
			self.location = (0, randint(0, h))
		elif randint(0, 100) == 2:
			self.location = (w, randint(0, h))
		elif randint(0, 100) == 3:
			self.location = (randint(0, w), 0)
		elif randint(0, 100) == 4:
			self.location = (randint(0, w), h)
		else:
			return
		spider = Spider()
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