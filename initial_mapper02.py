
#!/usr/bin/env python

import os
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
            c = 0
            cwd = os.getcwd()
            if l.query_alignment_length > 1000:
                c = c + 1
                if c > 0:
                    os.chdir("/home/ubuntu/pysam_streaming/f_BamFiles")
                    outfile = pysam.AlignmentFile(a_name, "w", template=samfile)
                    os.chdir(cwd)
                    outfile.write(l)
                    print c

print("--- %s seconds ---" % (time.time() - start_time))
