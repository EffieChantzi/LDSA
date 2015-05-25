#!/usr/bin/env python

from subprocess import call

call(['swift', 'download', 'GenomeData', 'NA20911.chrom20.ILLUMINA.bwa.GIH.low_coverage.20120522.bam'])
