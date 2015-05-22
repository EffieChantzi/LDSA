
#read names of bam files from a .txt file, and print the number of region reads for each one of them

#!/usr/bin/env python

import os
import sys
import pysam
import glob

filepath = "/home/ubuntu/pysam_streaming/bam_filenames.txt"
fileurl = open(filepath, "r")
list_names = fileurl.read().splitlines()


for a_name in list_names:
        #print a_name
        c = 0
        #os.chdir("/home/ubuntu/pysam_streaming")
        samfile = pysam.AlignmentFile(a_name, "rb")
        #bam_file= sam_file.fetch(until_eof = True)
        c = samfile.count()
        print '%s\t%d' % ('regionReads', c)
