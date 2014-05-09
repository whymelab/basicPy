#!/usr/bin/python
# child.py
#
# A sample child process for receiving messages over a channel
import Channel
import sys
import cPickle
ch = Channel.Channel(sys.stdout,sys.stdin)
while True:
    try:
        item = ch.recv()
	ch.send(('from Child',item))
    except EOFError:
        break

