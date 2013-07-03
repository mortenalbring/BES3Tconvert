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

    fileName, fileExtension = os.path.splitext(inputfile)

    paramfile = fileName + ".DSC";
    print("\n")
    print(paramfile);


#Test if input file exists
    try:
        with open(inputfile) : pass
    except IOError:
        print("input file doesn't exist!")
        sys.exit(2)

#Test if param file exists
    try:
        with open(paramfile) : pass
    except IOError:
        print("parameter file doesn't exist!")
        sys.exit(2)



    fin = open(paramfile,'r');
    for line in fin :
        
        p = line[0:4]
        #print(p)
                
        if p == 'XPTS' :
            xpoints = int(line[5:len(line)]);
            print(str(xpoints))
            
        if p == 'XMIN' :
            xmin = float(line[5:len(line)]);
            print(str(xmin))
            
        if p == 'XWID' :
            xwid = float(line[5:len(line)]);
            print(str(xwid))


    xmax = xmin + xwid
    xsampling = xwid / xpoints

    xdata = [];
    for k in range(1,xpoints,1) :
        xdata.append(xmin + (xsampling * (k - 1)))
        print(xdata[k-1])
        



#Test if file is DTA
        
    fileName, fileExtension = os.path.splitext(inputfile)
    print(fileExtension)
    if fileExtension == ".DTA" :
        print("Now converting DTA file!");

        toggle = 2;
        #xdata = [];
        ydata = [];
        l = 1;
        fin = open(inputfile,'rb');
        
        with open(inputfile,'rb') as inh:
            indata = inh.read()
        for i in range(0,len(indata),4) :
            pos = struct.unpack('>f',indata[i:i+4])           
        
            if toggle == 1 :
         #       xdata.append(pos[0]);
                l = l + 1;
                toggle = 2;
            else :
                ydata.append(pos[0]);
                l = l + 1;
                toggle = 1;
        fin.close()


    else :
        print("That's not a DTA file");


#Write stuff to files
    
    fout = open(outputfile,'w');
    print(str(len(xdata)))
    print(str(len(ydata)))

    for i in range(0,len(xdata)):
        fout.write(str(xdata[i]))
        fout.write(",")
        fout.write(str(ydata[i]))
        fout.write("\n");
            

if __name__ == "__main__":
   main(sys.argv[1:])
