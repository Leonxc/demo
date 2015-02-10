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
		
	def analyze_entities(self):
		for entity in self.world.entities:
			if isinstance(entity, Ant):
				self.ants.append(entity)
			elif isinstance(entity, Leaf):
				self.leafs.append(entity)
		
	def select_state(self):
		for ant in self.ants:
			for leaf in self.leafs:
				distance = (ant.location - leaf.location).get_length()
				distance_to_nest = (ant.location - self.world.nest_location).get_length()
				if distance > ant.senseRange and (ant.state == "explore" or ant.state == "drop_stuff"):
					ant.explore()
					print 1
				elif 10 < distance < ant.senseRange and ant.state == "explore" and leaf.state != "drop_by_ant":
					ant.seeking(leaf)
					print 2
				elif distance_to_nest > self.world.nest_r and distance < 10:
					if ant.state == "seeking":
						ant.carry_stuff()
						leaf.state = "carry_by_ant"
					if leaf.state != "carry_by_ant":
						leaf.carry_by_ant(ant)
					print 3
				elif distance_to_nest < self.world.nest_r - randint(1, self.world.nest_r) and ant.state == "carry_stuff":
					ant.drop_stuff()
					leaf.drop_by_ant()
					print 4
				else:
					ant.explore()