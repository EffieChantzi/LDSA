#!/usr/bin/env python

import os
import sys
import pysam
import glob
import time
from subprocess import call
import signal

a_name = "NA21144.chrom20.ILLUMINA.bwa.GIH.low_coverage.20130415.bam"
samfile = pysam.AlignmentFile(a_name, "rb")
list_reads = list(samfile.fetch(until_eof = True))

for l in list_reads:
list_cigar = []
                        if abs(l.query_alignment_length) > 1000:
                                counter = counter + 1


                if counter > 0:
                        print "%s\t%d" %(a_name, counter)
