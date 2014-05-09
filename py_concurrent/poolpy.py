#!/usr/bin/env python

import multiprocessing

def doCalc(year):
	return year*year

yearlist=[1,2,3,4]
print yearlist

if __name__ =='__main__':
	pool = multiprocessing.Pool(4)
	pool.map(doCalc, yearlist)
	print pool
	
