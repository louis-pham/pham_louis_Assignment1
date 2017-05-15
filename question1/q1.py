#!/usr/local/bin/python

import os
import sys

if len(sys.argv) >= 3:
	argFind = sys.argv[1]
	argReplace = sys.argv[2]
	
	print argFind
	print argReplace

	textFiles = [ f for f in os.listdir(os.getcwd()) if '.txt' in f]
	for filename in textFiles:
		print filename
		textFile = open(filename, 'r')
		fileContents = textFile.read()
		textFile.close()
		if argFind in fileContents:
			print "found string"
			newContents = fileContents.replace(argFind, argReplace)
			newFilename = "replace/" + filename
			if not os.path.exists(os.path.dirname(newFilename)): # original code from http://stackoverflow.com/questions/12517451/
				try:
					os.makedirs(os.path.dirname(newFilename))
				except OSError as exc: # Guard against race condition
					if exc.errno != errno.EEXIST:
						raise
			newFile = open(newFilename, 'w')
			newFile.write(newContents)
			newFile.close()
		else:
			print "didnt find string"
else:
	print "needs more arguments."


