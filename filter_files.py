import os
import sys
import pysam
import time
import re
from multiprocessing import Pool
from contextlib import closing

FILES_DIR = "/home/ubuntu/data/files/"
RESULTS_DIR = "/home/ubuntu/data/results/"
NUM_OF_PROCESSES = 2

def list_names():
        names = []

        for name in os.listdir(FILES_DIR):
                if name.endswith(".bam"):
                        names.append(name)

        return names

def process_names(a_name):
        info_split = a_name.split('.')
        samfile = pysam.AlignmentFile(FILES_DIR + a_name, "rb")
        list_reads = list(samfile.fetch(until_eof = True))

        matches = 0
        ins = 0
        dels = 0
        snps = 0
        unaligned = 0
        skipped = 0

        for l in list_reads:

                list_cigar = []
                list_tags = []

                if abs(l.template_length) > 1000:

                        list_cigar = l.cigartuples
                        list_tags = l.get_tags()
                        if list_tags:

                                for tag in list_tags:
                                        if tag[0] == 'MD':
                                                MD_tag = tag[1]
                                                seq_matches = map(int, re.findall("\d+", MD_tag))
                                                snps_read = (abs(l.query_alignment_length) - sum(seq_matches))
                                                snps = snps + snps_read
                                                break

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

        if matches + ins + dels + snps + unaligned > 0:
                target = open(RESULTS_DIR + a_name + '.txt', 'w')

                if snps > 0:
                        target.write("%s.%s.%s\t%s\n" % (info_split[0], info_split[4], "SNPs", snps))
                if matches > 0:
                        target.write("%s.%s.%s\t%s\n" % (info_split[0], info_split[4], "Matches", matches))
                if ins > 0:
                        target.write("%s.%s.%s\t%s\n" % (info_split[0], info_split[4], "Insertions", ins))
                if dels > 0:
                        target.write("%s.%s.%s\t%s\n" % (info_split[0], info_split[4], "Deletions", dels))
                if unaligned > 0:
                        target.write("%s.%s.%s\t%s\n" % (info_split[0], info_split[4], "Soft_clips", unaligned))

                target.close()

def main():
        start_time = time.time()

        with closing(Pool(processes = NUM_OF_PROCESSES)) as pool:
                try:
                        pool.map(process_names, list_names())
                        pool.close()
                except KeyboardInterrupt:
                        print "Caught KeyboardInterrupt, terminating workers"
                        pool.terminate()
                finally:
                        pool.join()

        print("--- %s seconds ---" % (time.time() - start_time))


if __name__=="__main__":
        main()
