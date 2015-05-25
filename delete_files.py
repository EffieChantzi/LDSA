
#!/usr/bin/env python

import os

myFile = "NA20763.chrom20.ILLUMINA.bwa.TSI.low_coverage.20130415.bam.bas"

## if file exists delete it
if os.path.isfile(myFile):
        os.remove(myFile)
else:    ## Show an error ##
        print("Error: %s file not found" % myFile)
