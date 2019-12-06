import pandas as pd
from os import path, makedirs
from subprocess import call
import multiprocessing as mp
from glob import glob

in_dir = 'resized/'
spi = 'spiral/'
ell = 'elliptical/'
ds_path = 'merged_dataset.csv'



df = pd.read_csv(ds_path).set_index('OBJID')
objids = sorted(list(set(df.index.data)))
print(df.loc[objids[0]].SPIRAL)
files_all = glob(path.join(in_dir, '*.npz'))


def work(infile):
	objid = int(infile.split('/')[-1].split('.')[0])
	if df.loc[objid].SPIRAL == 1:
		retval = call(['mv', infile, spi])
		if retval != 0:
			print('FAILED:', objid, req_url, out_dir, retval)
	elif df.loc[objid].ELLIPTICAL == 1:
		retval = call(['mv', infile, ell])
		if retval != 0:
			print('FAILED:', objid, req_url, out_dir, retval)
	else:
		pass

pool = mp.Pool(mp.cpu_count())
results = pool.map(work, [infile for infile in files_all])