#!/usr/bin/env python

import swiftclient
from swiftclient import service

username = ''
password = ''
tenant_name = ''
#auth_url = ''

conn = swiftclient.client.Connection(auth_version='2',
                                      user=username,
                                      key=password,
                                      tenant_name=tenant_name,
                                      authurl='',
)

#(response, obj) = conn.get_object('GenomeData', 'NA20911.chrom20.ILLUMINA.bwa.GIH.low_coverage.20120522.bam')



ser = swiftclient.service.SwiftService()
obj = ser.download('GenomeData', 'NA20911.chrom20.ILLUMINA.bwa.GIH.low_coverage.20120522.bam')
for i in obj:
        print i
