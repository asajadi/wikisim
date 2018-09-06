"""Utility functions"""
# uncomment

import os
import re
import csv
import itertools
import scipy as sp
import pandas as pd
import cPickle as pickle
import datetime
import sys

__author__ = "Armin Sajadi"
__copyright__ = "Copyright 215, The Wikisim Project"
__credits__ = ["Armin Sajadi"]
__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "Armin Sajadi"
__email__ = "sajadi@cs.dal.ca"
__status__ = "Development"

dirname = os.path.dirname(__file__)

def readds(url, usecols=None):    
    data = pd.read_table(url, header=None, usecols=usecols)
    return data

DISABLE_LOG=False;

def clearlog(logfile):
    with open(logfile, 'w'):
        pass;

def logres(outfile, instr, *params):
    outstr = instr % params;
    with open(outfile, 'a') as f:
        f.write("[%s]\t%s\n" % (str(datetime.datetime.now()) , outstr));          
        
def log(instr, *params):
    if DISABLE_LOG:
        return
    logres(logfile, instr, *params)
    
outdir = os.path.join(dirname, '../out')    
if not DISABLE_LOG:    
    logfile=os.path.join(outdir, 'log.txt');
    if not os.path.exists(logfile):
        if not os.path.exists(outdir):
            os.makedirs(outdir)
        log('log created') 
        os.chmod(logfile, 0777)    
    
    
def timeformat(sec):
    return datetime.timedelta(seconds=sec)

def str2delta(dstr):
    r=re.match(('((?P<d>\d+) day(s?), )?(?P<h>\d+):(?P<m>\d+):(?P<s>\d*\.\d+|\d+)'),dstr)
    d,h,m,s=r.group('d'),r.group('h'),r.group('m'),r.group('s')
    d=int(d) if d is not None else 0
    h,m,s = int(h), int(m), float(s)    
    return datetime.timedelta(days=d, hours=h, minutes=m, seconds=s)


def read_embedding_file(filename, records_number=sys.maxint):
    ''' return a dictinoray {'id': embedding} where each embedding is itself 
        a panda series
        Inputs:
            filename: embedding file name
            records_number: number of the records to be read                
    '''
    prog = re.compile("(^[0-9]+),'([\d\D]*)'\n$");
    embeddings={}
    count=0
    with open(filename,  'rb') as f:
        line = ''
        for l in f:
            line +=l
            if l.endswith('\\\n'):
                continue
            m = prog.match(line)
            assert m is not None
            wid = m.group(1)
            pickle_string = re.sub("\\\\([0\\,\\'\\\\\\\n])",
                                   lambda x:x.group(1) if x.group(1)!='0' else '\0' , m.group(2))
            #embeddings[wid]= pickle_string
            values, index = pickle.loads(pickle_string)
            embeddings[m.group(1)]=pd.Series(values, index=index)

            line=''
            count += 1
            if count >=records_number:
                break
    return embeddings