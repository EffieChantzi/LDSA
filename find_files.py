#!/usr/bin/env python

import os
import sys
import pysam
import glob
import time
import subprocess
import signal


start_time = time.time()


filepath = "/home/ubuntu/pysam_streaming/bam_filenames"
fileurl = open(filepath, "r")
list_names = fileurl.read().splitlines()


for a_name in list_names:

        counter = 0
        bai_file = a_name + ".bai"
        cmd1 = "swift download GenomeData " + a_name
        cmd2 = "swift download GenomeData " + bai_file
        #bam_d = subprocess.Popen(cmd1, stdout=subprocess.PIPE, shell=True)
        #bai_d = subprocess.Popen(cmd2, stdout=subprocess.PIPE, shell=True)

        #bam_pro = subprocess.Popen(cmd1, stdout = subprocess.PIPE, shell = True, preexec_fn = os.setsid)
        #bai_pro = subprocess.Popen(cmd2, stdout = subprocess.PIPE, shell = True, preexec_fn = os.setsid)
        bam_d = os.system(cmd1)
        bai_d = os.system(cmd2)
        #bam_d.kill()
        #bai_d.kill()
        #subprocess.call(cmd1, shell=True)
        #subprocess.call(cmd2, shell=True)
        #p1 = subprocess.call(['swift', 'download', 'GenomeData', a_name])
        #p2 = subprocess.call(['swift', 'download', 'GenomeData', bai_file])
        samfile = pysam.AlignmentFile(a_name, "rb")
        list_reads = list(samfile.fetch(until_eof = True))
 for l in list_reads:
                list_cigar = []
                if abs(l.query_alignment_length) > 1000:
                        counter = counter + 1


        if counter > 0:
                print "%s\t%d" %(a_name, counter)


        #os.killpg(bam_pro.pid, signal.SIGTERM)
        #os.killpg(bai_pro.pid, signal.SIGTERM)

        if os.path.isfile(a_name) and os.path.isfile(bai_file):
                os.remove(a_name)
                os.remove(bai_file)

print("--- %s seconds ---" % (time.time() - start_time))
