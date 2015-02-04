#!/usr/bin/env python
# -*-coding: utf-8 -*-
# filename:StateMachine.py

class State():
	def __init__(self, name):
		self.name = name
		
	def do_action(self):
		pass
	
	def check_condition(self):
		pass
		
	def entry_action(self):
		pass
		
	def exit_action(self):
		pass
		
class StateMachine():
	def __init__(self, State):
		