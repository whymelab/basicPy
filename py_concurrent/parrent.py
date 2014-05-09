#!/usr/bin/env python

import subprocess
from Channel import Channel

def main():
	connect = subprocess.Popen(['python','child.py'],stdin=subprocess.PIPE,stdout=subprocess.PIPE)
	ch = Channel(connect.stdin,connect.stdout)
	ch.send('hello World')
	print ch.recv()

if (__name__=='__main__'):
	main()
