import os
import sys

os.environ["OS_AUTH_URL"]=""
os.environ["OS_TENANT_ID"]=""
os.environ["OS_TENANT_NAME"]=""
os.environ["OS_USERNAME"]=""
os.environ["OS_PASSWORD"]=""

DATA_DIR = '/home/ubuntu/data/'
FILES_DIR = '/home/ubuntu/data/files/'

filepath = DATA_DIR + 'data.txt'
fileurl = open(filepath, 'r')
list_names = fileurl.read().splitlines()

for a_name in list_names:

        bai_file = a_name + '.bai'
        cmd1 = 'swift download GenomeData ' + a_name
        cmd2 = 'swift download GenomeData ' + bai_file

        try:
                os.chdir(FILES_DIR)
                bam_d = os.system(cmd1)
        except IOError as error:
                print 'Download of bam failed'
        try:
                bai_d = os.system(cmd2)
        except IOError as error:
                print 'Download of bai failed'
