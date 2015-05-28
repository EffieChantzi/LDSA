#!/usr/bin/env python

#HG00096.chrom20.ILLUMINA.bwa.GBR.low_coverage.20120522.bam
#HG00097.chrom20.ILLUMINA.bwa.GBR.low_coverage.20130415.bam
#HG00099.chrom20.ILLUMINA.bwa.GBR.low_coverage.20130415.bam
#HG00100.chrom20.ILLUMINA.bwa.GBR.low_coverage.20130415.bam

import os
import sys




filepath = "bam_filenames"
fileurl = open(filepath, "r")
list_names = fileurl.read().splitlines()


for a_name in list_names:

        counter = 0
        bai_file = a_name + ".bai"
        cmd1 = "swift download GenomeData " + a_name
        cmd2 = "swift download GenomeData " + bai_file

        try:
                bam_d = os.system(cmd1)
        except IOError as error:
                print "Download of bam failed"
        try:
                bai_d = os.system(cmd2)
        except IOError as error:
                print "Download of bai failed"
