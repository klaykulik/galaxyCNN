import numpy as np
import pandas as pd
from os import path, makedirs
from subprocess import call
import multiprocessing as mp
from glob import glob
import sys

filters = ['u', 'g', 'r', 'i', 'z']
out_dir = 'raw'+sys.argv[1]+'/'
ds_path = 'merged_dataset-'+sys.argv[1]+'.csv'

def work(config):
    objid, filter_, entry = config
    run, rerun, camcol, field = entry.run, entry.rerun, entry.camcol, entry.field
    req_url = ('http://das.sdss.org/cgi-bin/drC?RUN=%d&RERUN=%d&CAMCOL=%d&FIELD=%d&FILTER=%s.fits'
                    % (run, rerun, camcol, field, filter_))
    file_name = out_dir + ('drC?RUN=%d&RERUN=%d&CAMCOL=%d&FIELD=%d&FILTER=%s.fits'
                    % (run, rerun, camcol, field, filter_))
    retval = call(['wget',req_url, '-P', out_dir, '-q'])
    if retval != 0:
    	print('FAILED:', objid, req_url, out_dir, retval)
    # if path.exists(out_path):
    #     print('skipping', objid, filter_)
    #     continue
    # print(objid, filter_)
    # retval = call(['wget',req_url, '-P', out_dir, '-q'])

    # if retval != 0:
    #     print('FAILED:', objid, req_url, out_dir, retval)




df = pd.read_csv(ds_path).set_index('OBJID')
objids = sorted(list(set(df.index.data)))

configs = [(objid, filter_, df.loc[objid])
                   for objid in objids for filter_ in filters]



print("Number of processors: ", mp.cpu_count())
pool = mp.Pool(processes=mp.cpu_count())
results = pool.map(work, [config for config in configs])

