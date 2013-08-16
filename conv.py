#!/usr/bin/python

import struct
import sys
import getopt
import os
import glob
import csv

from itertools import zip_longest

def write_to_file(xdata,ydata,outputfile) :
#Writes output to file
    fileName, fileExtension = os.path.splitext(outputfile)
    
    fout = open(outputfile,'w');
    print(str(len(xdata)))
    print(str(len(ydata)))

    fp = open(outputfile,'w',newline='')
    a = csv.writer(fp,delimiter=',')
    #Writes header
    h = [fileName + ' x',fileName + ' y']
    a.writerow(h)
    for i in range(0,len(xdata)) :
        s1 = xdata[i];
        s2 = ydata[i];
        r = [s1,s2];
        a.writerow(r)
        
    return

def generate_ydata(inputfile) :
#Extracts the y axis data from the input file
    toggle = 2;
    ydata = [];
    fin = open(inputfile,'rb');
        
    with open(inputfile,'rb') as inh:
        indata = inh.read()
    for i in range(0,len(indata),8) :
        pos = struct.unpack('>d',indata[i:i+8])           
        ydata.append(pos[0]);
    fin.close()
    return ydata

def generate_xdata(paramfile) :
#Extracts the x axis data from the parameter file
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
      #  print(xdata[k-1])

    return xdata


def test_files(inputfile,outputfile) :
    errors = 0;
    #Test if input and output files have been specified properly
    if inputfile == '' :
        print("Oh no! You haven't specified an input file!")
        print("conv.py -i inputfile -o outputfile")
        sys.exit(2)
        errors = 1;
    elif outputfile == '' :
        print("Oh no! You haven't specified an output file!")
        print("conv.py -i inputfile -o outputfile")
        sys.exit(2)
        errors = 1;

    #Test if input file exists
    try:
        with open(inputfile) : pass
    except IOError:
        print("input file doesn't exist!")
        sys.exit(2)
        errors = 1;

    fileName, fileExtension = os.path.splitext(inputfile)
    paramfile = fileName + ".DSC";

    #Test if param file exists
    try:
        with open(paramfile) : pass
    except IOError:
        print("parameter file doesn't exist!")
        sys.exit(2)
        errors = 1;

    #Test if is DTA file or not
    if fileExtension != ".DTA" :
        print("Not a DTA file!");
        errors = 1;

    return errors



def main(argv):
    inputfile = ''
    outputfile = ''
    doall = 0

#Get command line arguments
    
    try:
        opts, args = getopt.getopt(argv,"hi:o:a",["ifile=","ofile="])
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
        elif opt in ("-a") :
            doall = 1;
    #Test if user wants to convert all of the files in the folder
    if (doall == 1 ) :

        
        tmpfilenames = []
        #Go through and generate temporary csv files for all DTA files
        for inputfile in glob.glob("*.DTA") :
            
            fileName, fileExtension = os.path.splitext(inputfile)
            tmpfile = fileName + ".tmp";
            tmpfilenames.append(tmpfile)
            
            paramfile = fileName + ".DSC";
            print("\n")
            print(paramfile);
            xdata = generate_xdata(paramfile)     
            ydata = generate_ydata(inputfile)
            write_to_file(xdata,ydata,tmpfile);            


        #Open all of those generated CSV files
        handles = [open(filename,'r') for filename in tmpfilenames]
        readers = [csv.reader(f,delimiter=',') for f in handles]

        
        with open(outputfile,'w',newline='') as h:
            writer = csv.writer(h)
            for rows in zip_longest(*readers,fillvalue=['']*2) :
                combined_row = []
                for row in rows:
                    row = row[:2]
                    if len(row) == 2:
                        combined_row.extend(row)
                    else :
                        combined.extend(['']*2)
                writer.writerow(combined_row)

        for f in handles:
            f.close()


    elif (test_files(inputfile,outputfile) == 0 ) :
        fileName, fileExtension = os.path.splitext(inputfile)
        paramfile = fileName + ".DSC";
        print("\n")
        print(paramfile);

        xdata = generate_xdata(paramfile);     
        ydata = generate_ydata(inputfile);
        write_to_file(xdata,ydata,outputfile);
                

if __name__ == "__main__":
   main(sys.argv[1:])
