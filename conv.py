import codecs
##f = codecs.open('GT192_10_5Kb.DTA','r','utf-32LE');

##f.readline();

##f = open('g.DTA','rb');
##
##try:
##    byte = f.read(1)
##    while byte != "":
##        byte = f.read(1)
##        print(byte);
##finally:
##    f.close()
##        
##import binascii
##print(binascii.crc32("hello"));

import struct

fin = open('V1P45.spc','rb');

fout = open('test.txt','w');

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
