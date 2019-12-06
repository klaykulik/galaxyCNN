import numpy as np
from skimage.transform import resize
from os import path
from glob import glob
import multiprocessing as mp


## Configs
indir = 'clipped/'
outdir = 'resized/'
tgt_dim = (200, 200)


## Fetch tasks
files_all = glob(path.join(indir, '*.npz'))
#files_todo = [file for file in files_all 
#              if not path.exists(path.join(outdir, path.basename(file)))]
files_todo = files_all
files_todo.sort()


## Work
def work(file):
    in_ds = np.load(file)
    try:
        out_ds = {
            k: resize(in_ds[k].astype('float'), tgt_dim).astype('uint16') 
                for k in in_ds
        }
        out_path = path.join(outdir, path.basename(file))
        np.savez(out_path, **out_ds)
    except Exception as e:
        print('FAILED: %s %s' % (file, str(e)))

print("Number of processors: ", mp.cpu_count())
pool = mp.Pool(mp.cpu_count())
results = pool.map(work, [file for file in files_todo])

