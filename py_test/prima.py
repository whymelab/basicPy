#!/usr/bin/env python

def prima(x):
	i = 1;
	y = 0;
	while i <= x :
		if x%i == 0 :
			print "nilai i : ",i, "nilai mod : ",x%i 
			y+=1 ;
		i+=1
	if y == 2 :
		print "termasuk prima "
	else :
		print "bukan prima "
		
prima(6)
