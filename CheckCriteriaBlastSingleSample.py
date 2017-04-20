#!/usr/bin/env python

# Script which test the different filtering thresholds per barcode
# Returns per barcode the detected species which match the criteria

import sys
import os


### Get the OTU abundance from the file (This is per barcode)
def GetOTUabundance(statFile, pOTU):
	# Local variables
	f = open(statFile)
	abundance={}
	#OTUabun=100

	for line in f:
		# Remove the enter from the end of the line
		line = line.rstrip()

		### Get the different barcode from the statistics file
		if (line.startswith("############ Statistics for barcode: ")):
			barcode=line.split("############ Statistics for barcode: ")[1].replace(" ############", "")
			if not(barcode in abundance.keys()):
				abundance[barcode]=1
				#print barcode
		else:
			if (line.startswith("# combined file:	")):
				assignedReads=int(line.split("\t")[1])
				OTUabun=assignedReads*(pOTU/100)
				#print barcode+"\t"+str(assignedReads)+"\t"+str(OTUabun)
				abundance[barcode]=OTUabun
	
	### Close the file and return the dictionary
	f.close()
	return abundance

### Function to retrieve the different organisms from the blast summary
def GetHitsPerBarcode(abundance, InFile, pident, OutFile):
	# Local variables
	f = open(InFile, "r")
	output = open(OutFile, "w")
	CountSpec={}
	OTU=""
	qlen=0
	
	for line in f:
		# Remove the enter from the end of the line
		line = line.rstrip()
	
		### Get barcodes but ignore title lines
		if (line.startswith("#####")):
			if (line.startswith("##### Results for:")):
				output.write("\n"+line+"\n")
				barcode=line.split("##### Results for: ")[1].replace(" #####", "")
				output.write("OTU abun "+barcode+":\t"+str(abundance[barcode])+"\n")
				### Get a different length per barcode
				if ( barcode == "ITS2" ):
					qlen=100
				elif (barcode == "rbcL-mini"):
					qlen=140
				elif ( barcode == "trnL_P6loop" ):
					qlen=10
				else:
					qlen=200
		else:
			### Ignore the blast line of the output
			if (line.startswith("OTU")):

				splitLine = line.split("\t")
				### Check if the size of the OTU is above the OTU abundance
				if (abundance[barcode] <= int(splitLine[0].split("size=")[1].replace(";",""))):

					### Get the top hit (based on bitscore)
					if (OTU == splitLine[0]):
						if not (splitLine[4] < bitscore):
							### Is your line matching the criteria (Query length and percentage of identity)
							if ( (int(splitLine[1] ) >= qlen) and (float(splitLine[3]) >= pident) ):
								output.write(line+"\n")
					else:
						### Get the next values
						OTU=splitLine[0]
						bitscore=splitLine[4]

						### Is your line matching the criteria (Query length and percentage of identity)
						if ( (int(splitLine[1] ) >= qlen) and (float(splitLine[3]) >= pident) ):
							output.write(line+"\n")
			else:
				### Skip the empty lines
				if (line != ""):
					### Only get the title lines from the blast output
					if (line.startswith("qseqid")):
						#print line
						output.write(line+"\n")

	### Close the files
	output.close()
	f.close()


### Retrieve the hits per barcode
def GetAllHitsPerBarcode(abundance, InFile, pident, OutFile):
	# Local variables
	f = open(InFile, "r")
	output = open(OutFile, "w")
	CountSpec={}
	OTU=""
	qlen=0
	
	for line in f:
		# Remove the enter from the end of the line
		line = line.rstrip()
	
		### Get barcodes but ignore title lines
		if (line.startswith("#####")):
			if (line.startswith("##### Results for:")):
				output.write("\n"+line+"\n")
				barcode=line.split("##### Results for: ")[1].replace(" #####", "")
				output.write("OTU abun "+barcode+":\t"+str(abundance[barcode])+"\n")
				### Get a different length per barcode
				if ( barcode == "ITS2" ):
					qlen=100
				elif (barcode == "rbcL-mini"):
					qlen=140
				elif ( barcode == "trnL_P6loop" ):
					qlen=10
				else:
					qlen=200
		else:
			### Ignore the blast line of the output
			if (line.startswith("OTU")):

				splitLine = line.split("\t")
				### Check if the size of the OTU is above the OTU abundance
				if (abundance[barcode] <= int(splitLine[0].split("size=")[1].replace(";",""))):
					if ( (int(splitLine[1] ) >= qlen) and (float(splitLine[3]) >= pident) ):
							output.write(line+"\n")
			else:
				### Skip the empty lines
				if (line != ""):
					### Only get the title lines from the blast output
					if (line.startswith("qseqid")):
						output.write(line+"\n")

	### Close the files
	output.close()
	f.close()


### Check all the input and call all the functions
def main(argv):
	### Check the input
	if (len(argv) == 6 ):

		### Catch the variable files
		statFile=argv[0]
		InFile=argv[1]
		FullInFile=argv[2]
		OutName=argv[3]

		### Variables
		pOTU=float(argv[4])
		pident=int(argv[5])
		
		### Local variables
		OutFile=OutName+"_"+str(pident)+"_"+str(pOTU)+".tsv"
		FullOutFile=OutName+"_"+str(pident)+"_"+str(pOTU)+"_Full.tsv"

		### Call your functions
		abundance=GetOTUabundance(statFile, pOTU)
		GetHitsPerBarcode(abundance, InFile, pident, OutFile)
		GetAllHitsPerBarcode(abundance, FullInFile, pident, FullOutFile)
	else: 
		print "Wrong type of arguments: python CheckCriteriaBlastSingleFile.py <inFile> <OutFile>"




### Call your main function
if __name__ == "__main__":
   main(sys.argv[1:])






