#!/usr/bin/env python

def x():
	print 'Hello World'

def y(xx):
	print 'dengan nilai xx : ',xx

def z(xxx=10,yyy=11):
	print 'nilai xxx : ',xxx,' nilai yyy : ', yyy

def c(q,p=111):
	print q , p
def main():
	x()
	y(10)	
	z(10)
	c(100)
if __name__ == '__main__' :
	main()
