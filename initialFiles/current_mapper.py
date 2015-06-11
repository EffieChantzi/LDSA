#!/usr/bin/env python

import os
import sys
import pysam
import glob
import time
from subprocess import call


start_time = time.time()


filepath = "/home/ubuntu/pysam_streaming/bam_filenames"
fileurl = open(filepath, "r")
list_names = fileurl.read().splitlines()


for a_name in list_names:
        #print a_name
        print a_name
        bai_file = a_name + ".bai"
        os.system("swift download GenomeData a_name")
        os.system("swift download GenomeData bai_file")
        #call(['swift', 'download', 'GenomeData', bai_file])
        #os.chdir("/home/ubuntu/pysam_streaming")
        samfile = pysam.AlignmentFile(a_name, "rb")
        print '%s\t%d' % ('regionReads', samfile.count())
        if os.path.isfile(a_name) and os.path.isfile(bai_file):
                os.remove(a_name)
                os.remove(bai_file)

print("--- %s seconds ---" % (time.time() - start_time))
