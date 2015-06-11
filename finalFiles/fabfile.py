#!/usr/bin/env python
# -*- coding: utf-8 -*- #

from __future__ import with_statement
from fabric.api import (
    run, local, parallel, put, env, roles,
    cd, lcd, task, abort, hosts
)
from fabric.tasks import execute
from fabric.contrib.files import exists

# Set the user to use for ssh
env.user = "ubuntu"
env.add_unknown_hosts = True

HADOOP_BIN_DIR = '/usr/local/hadoop/bin/'
HADOOP_CONF_DIR = '/usr/local/hadoop/conf/'
DATA_DIR = '/home/ubuntu/data/'
FILES_DIR = '/home/ubuntu/data/files/'
RESULTS_DIR = '/home/ubuntu/data/results/'
HDFS_RESULTS_DIR = '/results/'

# Build the list of slaves from slaves file
with open(HADOOP_CONF_DIR + "slaves", 'r + ') as f:
        slaves = f.readlines()

f.close()
env.roledefs = {'slave': slaves}

@task
@parallel
@roles('slave')
def format_data():
        try:
                run('hostname -f')
                run('rm -rf ' + DATA_DIR)
                run('mkdir ' + DATA_DIR)
                run('mkdir ' + FILES_DIR)
                run('mkdir ' + RESULTS_DIR)
        except:
                abort('Problem - format_data()')

@task
def split_selected_files():
        sf = open(DATA_DIR + 'selected_files.txt', 'r')
        lines = sf.readlines()
        num_of_lines = len(lines)
        for i in range(0, len(slaves)):
                f = open(DATA_DIR + 'f' + str(i) + '.txt', 'w')
                j = i
                while j < num_of_lines:
                        f.write(lines[j])
                        j = j + len(slaves)
                f.close()
        sf.close()

@task
def distribute_files():
        try:
                for i in range(0, len(slaves)):
                        local('scp ' + DATA_DIR + 'f' + str(i) + '.txt ' + slaves[i].strip('\n') + ':' + DATA_DIR + 'data.txt')
        except:
                abort('Problem - distribute_files()')

@task
@parallel
@roles('slave')
def get_files():
        try:
                run('python get_files.py')
        except:
                abort('Problem - get_files()')

@task
@parallel
@roles('slave')
def filter_files():
        try:
                run('python filter_files.py')
        except:
                abort('Problem - filter_files()')

@task
@parallel
@roles('slave')
def format_results():
        try:
                run('rm -rf ' + RESULTS_DIR)
                run('mkdir ' + RESULTS_DIR)
        except:
                abort('Problem - format_results()')


@task
@parallel
@roles('slave')
def upload_to_HDFS():
        try:
                run(HADOOP_BIN_DIR + 'hadoop dfs -copyFromLocal ' + RESULTS_DIR + '* ' + HDFS_RESULTS_DIR)
        except:
                abort('Problem - upload_to_HDFS()')
