#!/usr/bin/env python

# Script to retrieve only the top hit of the blast files

import sys

def main(argv):
	### Check the input
	if (len(argv) == 2 ):
		### Input
		fileN=argv[0]
		outF=argv[1]
		Hit=""

		### Open file
		f = open(fileN, "r")
		output = open(outF, "w")
		
		for line in f:
			# Remove the enter from the end of the line
			line = line.rstrip()
			splitLine=line.split("\t")
			
			if splitLine[0] not in Hit:
				output.write(line+"\n")
				Hit=splitLine[0]
			else:
				pass
		### close the line
		output.close()
		f.close()
	else: 
		print "Wrong type of arguments: python GetTopHits.py <inFile> <OutFile>"

### Call your main function
if __name__ == "__main__":
   main(sys.argv[1:])


