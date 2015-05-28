#!/usr/bin/env python

import os
import sys
import pysam
import time

filepath = "bam_filenames"
fileurl = open(filepath, "r")
list_names = fileurl.read().splitlines()


for a_name in list_names:

        info_split = a_name.split('.')
        samfile = pysam.AlignmentFile(a_name, "rb")
        list_reads = list(samfile.fetch(until_eof = True))

        matches = 0
        ins = 0
        dels = 0
        unaligned = 0
        skipped = 0


        for l in list_reads:

                list_cigar = []

                if abs(l.query_alignment_length) > 90:
                        list_cigar = l.cigartuples

                        if list_cigar:
                                for elem in list_cigar:
                                        sublist = elem
                                        if sublist[0] == 0:
                                                matches = matches + sublist[1]
                                        elif sublist[0] == 1:
                                                ins = ins + sublist[1]
                                        elif sublist[0] == 2:
                                                dels = dels + sublist[1]
                                        elif sublist[0] == 3:
                                                skipped = skipped + sublist[1]
                                        elif sublist[0] == 4:
                                                unaligned = unaligned + sublist[1]


        if matches > 0:
                print "%s.%s.%s\t%s" % (info_split[0], info_split[4], "Matches", matches)
        if ins > 0:
                print "%s.%s.%s\t%s" % (info_split[0], info_split[4], "Insertions", ins)
        if dels > 0:
                print "%s.%s.%s\t%s" % (info_split[0], info_split[4], "Deletions", dels)
        if unaligned > 0:
                print "%s.%s.%s\t%s" % (info_split[0], info_split[4], "Soft_clips", unaligned)
