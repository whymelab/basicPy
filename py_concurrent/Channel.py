#!/usr/bin/env python

import cPickle

class Channel(object):
	def __init__(self, OUT, IN):
		self.OUT=OUT
		self.IN=IN
	def send(self, item):
		cPickle.dump(item,self.OUT)
		self.OUT.flush()
	def recv(self):
		return cPickle.load(self.IN)

	
