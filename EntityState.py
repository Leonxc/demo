#!/usr/bin/env python
# -*-coding: utf-8 -*-
# filename:EntityState.py

import

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
		