import os
import sys
import time

# os.chdir('/home/ubuntu/faby/')

# Create directories for input data and results on each DataNode
os.system('fab format_data')

# Split the file containing input names, into multiple smaller files according to the number of DataNodes
os.system('fab split_selected_files')

# Distribute files containing filenames to DataNodes
os.system('fab distribute_files')

# Each DataNode downloads the corresponding files locally
start_time = time.time()
os.system('fab get_files')
print("Downloading Duration: %s seconds" % (time.time() - start_time))

# Each DataNode applies filtering function
start_time = time.time()
os.system('fab filter_files')
print("Filtering Duration: %s seconds" % (time.time() - start_time))

# Each DataNode uploads results to HDFS
os.system('fab upload_to_HDFS')
