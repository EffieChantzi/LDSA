#!/usr/bin/env python

import sys
import pysam
import glob
import time

start_time = time.time()


filepath = "/home/ubuntu/pysam_streaming/bam_filenames.txt"
fileurl = open(filepath, "r")
list_names = fileurl.read().splitlines()


for a_name in list_names:
        #print a_name
        print a_name

        #os.chdir("/home/ubuntu/pysam_streaming")
        samfile = pysam.AlignmentFile(a_name, "rb")
        list_reads = list(samfile.fetch(until_eof = True))
        for l in list_reads:
                list_cigar = []
                if l.query_alignment_length > 1000:
                        list_cigar = l.cigartuples

                        if list_cigar:
                                new_list = []
                                for sublist in list_cigar:
                                        for k in sublist:
                                                new_list.append(k)


                                matches = 0
                                for i in range(len(new_list)-1):
                                        if new_list[i] == 0:
                                                matches = matches + new_list[i + 1]
                                print matches

print("--- %s seconds ---" % (time.time() - start_time))
