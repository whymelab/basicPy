#!/usr/bin/env python

import cPickle as pickle
import subprocess
import sys

def main():
	p = subprocess.Popen(['python','child.py'],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
	sys.stdin=p.stdin
	a = pickle.dump("hello",sys.stdin)	
	#a.sys.stdin.flush()
if (__name__=='__main__'):
	main()
