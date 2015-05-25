#!/usr/bin/env python

import os
import sys
import pysam
import glob
import time
import subprocess


start_time = time.time()


filepath = "/home/ubuntu/pysam_streaming/bam_filenames"
fileurl = open(filepath, "r")
list_names = fileurl.read().splitlines()


for a_name in list_names:

	counter = 0
        bai_file = a_name + ".bai"
        p1 = subprocess.call(['swift', 'download', 'GenomeData', a_name])
        p2 = subprocess.call(['swift', 'download', 'GenomeData', bai_file])
        samfile = pysam.AlignmentFile(a_name, "rb")
        list_reads = list(samfile.fetch(until_eof = True))
	
	for l in list_reads:
                list_cigar = []
                if abs(l.query_alignment_length) > 1000:
                        counter = counter + 1


	if counter > 0:                        
                print "%s\t%d" %(a_name, counter)
          
        if os.path.isfile(a_name) and os.path.isfile(bai_file):
                os.remove(a_name)
                os.remove(bai_file)

print("--- %s min ---" % (time.time() - start_time)/60)
