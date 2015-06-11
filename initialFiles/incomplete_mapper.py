
#!/usr/bin/env python

import os
import sys
import pysam
import glob
import time
import subprocess


start_time = time.time()

																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																																											

start_pos = 300
#list_cigar = [(0, 91)]
#list_cigar = [(4, 29), (0, 57), (1, 2), (4, 5)]
list_cigar = [(0, 5), (1, 2), (0, 3)]
new_list =[]


for sublist in list_cigar:
    for k in sublist:
        new_list.append(k)

print new_list
        
        
pos = start_pos - 1
matches = 0
ins = 0
dels = 0
skipped = 0
unaligned = 0

k = len(new_list)/2
tmp_list = []
c = 0
for j in range(k):
    tmp_list.append(c)
    c = c + 2

print tmp_list
    
for i in tmp_list:
    if new_list[i] == 0:
        pos = pos + 1
        matches = matches + new_list[i + 1]
        #print "%s\t%d(%s: %d)" % ("Matches", matches, "Start_Pos", pos)
        pos = pos + (new_list[i + 1] - 1)
    elif new_list[i] == 1:
        ins = ins + new_list[i + 1]
    elif new_list[i] == 2:
        pos = pos + 1
        dels = dels + new_list[i + 1]
        #print "%s: %d - %s: %d" % ("D", dels, "SP", pos)
        pos = pos + (new_list[i + 1] - 1)
    elif new_list[i] == 3:
        skipped = skipped + new_list[i + 1]
    elif new_list[i] == 4:
        unaligned = unaligned + new_list[i + 1]
        
if matches > 0:
    print "%s\t%d" % ("Matches", matches)        
if ins > 0:
    print "%s\t%d" % ("Insertions", ins)
if dels > 0:
    print "%s\t%d" % ("Deletions", dels)    
if unaligned > 0:
    print "%s\t%d" % ("Soft_clips", unaligned)
if skipped > 0:
    print "%s\t%d" % ("Skipped_regions", skipped)        
        

                                                     
