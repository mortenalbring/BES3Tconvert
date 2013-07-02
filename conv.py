#!/usr/bin/python

import struct
import sys
import getopt
import os

def main(argv):
    inputfile = ''
    outputfile = ''

#Get command line arguments
    
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["ifile=","ofile="])
    except getopt.GetoptError:
        print("Oh no! You didn't put in enough arguments or something!")
        sys.exit(2)
    for opt,arg in opts:
        if opt == '-h':
            print("conv.py -i inputfile -o outputfile");
            sys.exit()
        elif opt in ("-i","--ifile"):
            inputfile = arg
        elif opt in ("-o","--ofile"):
            outputfile = arg
#Test if input and output files have been specified properly
            
    if inputfile == '' :
        print("Oh no! You haven't specified an input file!")
        print("conv.py -i inputfile -o outputfile")
        sys.exit(2)
    elif outputfile == '' :
        print("Oh no! You haven't specified an output file!")
        print("conv.py -i inputfile -o outputfile")
        sys.exit(2)

#Test if input file exists
    try:
        with open(inputfile) : pass
    except IOError:
        print("input file doesn't exist!")

#Test if file is DTA
        
    fileName, fileExtension = os.path.splitext(inputfile)
    print(fileExtension)
    if fileExtension == ".DTA" :
        print("Now converting DTA file!");

        fin = open(inputfile,'rb');
        fout = open(outputfile,'w');

        toggle = 1;
        try:
            b = struct.unpack('>f',fin.read(4));
            while b != "":
                b = struct.unpack('>f',fin.read(4));
                if toggle == 1 :
                    print(b[0])
                    print(',')
                    fout.write(str(b[0]));
                    fout.write(',');
                    toggle = 2;
                else :
                    print(b[0])
                    fout.write(str(b[0]));
                    fout.write('\n');
                    toggle = 1;
                    
        finally:
            fin.close()


if __name__ == "__main__":
   main(sys.argv[1:])
