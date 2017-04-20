#!/usr/bin/env python


# Script which removes the strange entities from the nt-database which causes the retrieve taxonomy to fail
# It is about ID;ID. That part needs to be removed
# Example of running:
#	- python RemoveDoubleEntityNCBI.py /home/hagel003/Downloads/CITES/Output/BlastTest/OTU_26.filtered.blast.out /home/hagel003/Downloads/CITES/Output/BlastTest/OTU_26.filtered.noDoubles.blast.out

import sys

def main(argv):
	### Check the input
	if (len(argv) == 2 ):
		### Input
		fileN=argv[0]
		outF=argv[1]
	
		### Open file
		f = open(fileN, "r")
		output = open(outF, "w")

		for line in f:
			# Remove the enter from the end of the line
			line = line.rstrip()
			splitLine=line.split("\t")
			
			# Remove the double entity
			if ";" in splitLine[7]:
				output.write(splitLine[0]+"\t"+splitLine[1]+"\t"+splitLine[2]+"\t"+splitLine[3]+"\t"+splitLine[4]+"\t"+splitLine[5]+"\t"+splitLine[6]+"\t"+splitLine[7].split(";")[0]+"\t"+splitLine[8].split(";")[0]+"\n")
			else:
				output.write(line+"\n")

		### close the line
		output.close()
		f.close()
	else: 
		print "Wrong type of arguments: python RemoveDoubleEntityNCBI.py <inFile> <OutFile>"




### Call your main function
if __name__ == "__main__":
   main(sys.argv[1:])
