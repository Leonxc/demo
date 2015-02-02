#!/usr/bin/env python
# -*-coding: utf-8 -*-
# filename:EntityState.py

from GameEntity import *
from gameobjects.vector2 import Vector2

class State(object):
	def __init__(self, name):
		self.name = name
	def do_actions(self):
		pass
	def check_conditions(self):
		pass
	def entry_actions(self):
		pass
	def exit_actions(self):
		pass
		
class StateMaching(object):
	def __init__(self):
		self.states = {}
		self.active_state = None
		
	def add_state(self, state):
		self.states[state.name] = state
		
	def think(self):
		if self.active_state is None:
			if self.active_state is None:
				return
			self.active_state.do_actions()
			
	def set_state(self, new_state_name):
		if self.active_state is not None:
			self.active_state.exit_actions[new_state_name]
		self.active_state = self.states[new_state_name]
		self.active_state.entry_actions()
		
class AntStateExploring(State):
	def __init__(self, ant):
		state.__init__(self, "explorint")
		self.ant = ant
		
	def random_destination(self):
		w, h = SCREEN_SIZE
		self.ant.destination = Vector2(randint(0, w), randint(0, h))
		
	def do_actions(self):
		if randint(1, 20) == 1:
			self.random_destination()
			
	def check_conditions(self):
		leaf = self.ant.world.get_close_entity("spider", NEST_POSITION, NEST_SIZE)
		if leaf is not None:
			self.ant.leaf_id = leaf.id
			return "seeking"
		spider = self.ant.world.get_close_entity("spider", NEST_POSITION. NEST_SIZE)
		if spider is not None:
			if self.ant.location.get_distance_to(spider.location) < 100.:
				self.ant.spider_id = spider.id
				return "hunting"
		return None
		
		def entry_actions(self):
			self.ant.speed = 120. + randint(-30, 30)
			self.random_destination()
			
class AntStateDelivering(state):
	def __init__(self, ant):
		State.__init__(self, "delivering")
		self.ant = ant
	def check_conditions(self):
		if Vector2(*NEST_POSITION).get_distance_to(self.ant.location) < NEST_SIZE:
			if (randint(1, 10) == 1):
				self.ant.drop(self.ant.world.background)
				return "exploring"
		return None
	
	def entry_actions(self):
		self.ant.speed = 60.
		random_offset = Vector2(randint(-20, 20), randint(-20, 20))
		self.ant.destination = Vector2(*NEST_POSITION) + random_offset
		
class AntStateHunting(state):
	def __init__(self, ant):
		State.__init__(self, "hunting")
		self.ant = ant
		self.got_kill = False
		
	def do_actions(self):
		spider = self.ant.world.get(self.ant.spider_id)
		if spider is None:
			return
		if self.ant.location.get_distance_to(spider.location) < 15.:
			if randint(1, 5) == 1:
				spider.bitten():
					spider.bitten()
					if spider.health <= 0
						self.ant.carry(spider.image)
						self.ant.world.remove_entity(spider)
						self.got_kill = True
						
	def check_conditions(self):
		if self.got_kill:
			return "delivering"
		spider = self.ant.world.get(self.ant.spider_id)
		if spider is None:
			return "exploring"
		if spider.location.get_distance_to(NEST_POSITION) > NEST_SIZE * 3:
			return "exploring"
		return None
			
	def entry_actions(self):
		self.speed = 160. + randint(0, 50)
				
	def exit_actions(self):
		self.got_kill = False
		
class World(object):
	def __init__(self):
		self.entities = {}
		self.entity_id = 0
		self.background = pygame.surface.Surface(SCREEN_SIZE).convert(0)
		self.background.fill((255, 255, 255))
		pygame.draw.circle(self.background, (200, 255, 200), NEST_POSITION, int(NEST_SIZE))
		
	def add_entity(self, entity):
		self.entities[self.entity_id] = entity
		entity.id = self.entity_id
		self.entity_id += 1
