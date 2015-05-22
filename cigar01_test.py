
#!/usr/bin/env python

import os
import sys
import pysam
import glob

samfile = pysam.AlignmentFile("HG00108.chrom20.ILLUMINA.bwa.GBR.low_coverage.20120522.bam", "rb")
list_reads = list(samfile.fetch(until_eof = True))
for l in list_reads:
    list_cigar = []
    if l.query_alignment_length > 91:
        list_cigar = l.cigartuples
        #print list_cigar

###################
#list_cigar = [(0, 91)]

        if list_cigar:
                new_list = []
                for sublist in list_cigar:
                        for k in sublist:
                                new_list.append(k)


                        #print new_list

                matches = 0
                if len(new_list) > 0:
                        for i in range(len(new_list)-1):
                                if new_list[i] == 0:
                                        matches = matches + new_list[i + 1]
                print matches

