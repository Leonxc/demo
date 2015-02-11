#!/usr/bin/env python
# -*- coding:utf-8 -*-
# filename:StateMachine

from World import *
from GameEntity import *

class StateMachine(object):
	def __init__(self, world):
		self.world = world
		self.ants = []
		self.leafs = []
		self.spiders = []
		
	def analyze_entities(self):
		self.ants = []
		self.leafs = []
		self.spiders = []
		for entity in self.world.entities:
			if isinstance(entity, Ant):
				self.ants.append(entity)
			elif isinstance(entity, Leaf):
				self.leafs.append(entity)
			elif isinstance(entity, Spider):
				self.spiders.append(entity)
		
	def ant_state(self):
		for ant in self.ants:
			for leaf in self.leafs:
				distance = (ant.location - leaf.location).get_length()
				distance_to_nest = (ant.location - self.world.nest_location).get_length()
				if distance > ant.senseRange and (ant.state == "explore" or ant.state == "drop_stuff"):
					ant.explore()
					#print 1
				elif 10 < distance < ant.senseRange and ant.state == "explore" and leaf.state == "":
					ant.seeking(leaf)
					leaf.target = ant
					#print 2
				elif distance_to_nest > self.world.nest_r and distance < 10 and ant.state == "seeking" and leaf.target == ant:
					ant.carry_stuff()
					leaf.state = "carry_by_ant"
					print 333
				elif ant.location == ant.destination and ant.state == "carry_stuff" and leaf.state == "carry_by_ant" and leaf.target == ant:
					ant.drop_stuff()
					leaf.state = "drop_by_ant"
					leaf.drop_by_ant()
					print 444
				elif ant.state == "dead":
					ant.drop_stuff()
					
	def leaf_state(self):
		for leaf in self.leafs:
			if isinstance(leaf, Leaf):
				if leaf.state == "carry_by_ant":
					leaf.carry_by_ant()
					
	def spider_state(self):
		for spider in self.spiders:
			for ant in self.ants:
				distance = (ant.location - spider.location).get_length()
				distance_to_nest = (spider.location - self.world.nest_location).get_length()
				if spider.state == "explore":
					spider.explore()
				elif 10 < distance < spider.senseRange and spider.state == "explore":
					spider.seeking(ant)
				elif distance < 10 and spider.state == "seeking" and self.target == ant:
					spider.eat_ant(ant)
					spider.state = "explore"
				if distance_to_nest < self.world.nest_r and ant.state == "explore":
					ant.attack_spider(spider)
					if spider.health <= 0:
						spider.dead()
				
				# elif 