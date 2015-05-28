#!/usr/bin/env python

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
