#!/usr/bin/env python

class test():
	__private = 10 
	_protected= 5 
	public = 0
	def __init__(self):
		self.__private   = 10
		self._proctected = 5
		self.public = 0
	def methodA(self):
		print "hello"
	def methodCek(self):
		print "nilai __private",self.__private
		print "nilai _proctected",self._protected
		print "nilai public ",self.public

class test2(test):
	def __init__(self):
		#print "nilai __private",self.__private
                print "nilai _proctected",self._protected
                print "nilai public ",self.public

def main():
	#a = test()
	#a.methodA()
	#a.methodCek()
	b = test2()


if __name__ =='__main__' :
	main()
