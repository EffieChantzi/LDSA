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
        #print a_name
        #print a_name
        bai_file = a_name + ".bai"
        p1 = subprocess.call(['swift', 'download', 'GenomeData', a_name])
        p2 = subprocess.call(['swift', 'download', 'GenomeData', bai_file])
        #call(['swift', 'download', 'GenomeData', bai_file])
        #os.chdir("/home/ubuntu/pysam_streaming")
        samfile = pysam.AlignmentFile(a_name, "rb")
        list_reads = list(samfile.fetch(until_eof = True))
        total_matches = 0
        total_ins = 0
        total_dels = 0
        total_skipped = 0
        total_unaligned = 0
        flag = 0

        for l in list_reads:
                list_cigar = []
                if abs(l.query_alignment_length) > 1000:
                        flag = flag + 1
                        list_cigar = l.cigartuples
                        list_ref_pos = l.get_reference_positions()
                        
                        if list_cigar:
                                new_list = []
                                for sublist in list_cigar:
                                        for k in sublist:
                                                new_list.append(k)

                                pos = list_ref_pos[0] - 1
                                matches = 0
                                ins = 0
                                dels = 0
                                skipped = 0
                                unaligned = 0
                                for i in range(len(new_list)-1):
                                        if new_list[i] == 0:
                                                pos = pos + 1
                                                matches = matches + new_list[i + 1]
                                                print "%s: %d - %s: %d" % ("M", matches, "SP", pos)
                                                pos = pos + (new_list[i + 1] - 1)
                                        elif new_list[i] == 1:
                                                ins = ins + new_list[i + 1]
                                                print "%s: %d" % ("I", ins)
                                        elif new_list[i] == 2:
                                                pos = pos + 1
                                                dels = dels + new_list[i + 1]
                                                print "%s: %d - %s: %d" % ("D", dels, "SP", pos)
                                                pos = pos + (new_list[i + 1] - 1)
                                        elif                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                if new_list[i] == 3:
                                                skipped = skipped + new_list[i + 1]
                                        elif new_list[i] == 4:
                                                unaligned = unaligned + new_list[i + 1]

                                #print matches
                                total_matches = total_matches + matches
                                total_ins = total_ins + ins
                                total_dels = total_dels + dels
                                total_skipped = total_skipped + skipped
                                total_unaligned = total_unaligned + unaligned
        if flag > 0:                        
                info_split = a_name.split('.')
                print "individual: %s, country: %s, date: %s" % (info_split[0], info_split[4], info_split[6])
                print "TM: %d - TI: %d - TD: %d - TS: %d - TU: %d" % (total_matches, total_ins, total_dels, total_skipped, total_unaligned)
        if os.path.isfile(a_name) and os.path.isfile(bai_file):
                os.remove(a_name)
                os.remove(bai_file)

print("--- %s seconds ---" % (time.time() - start_time))
                                                     
